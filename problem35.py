from problem import Problem
import random
from idlelib import tree
from graphics import *

class Problem35(Problem):
    def __init__(self):
        limit = random.randint(5,10)
        data = [random.randint(0, 100) for _ in range(1, limit)]
        data = list(set(data))

        statement = '1. Avem urmatoarele elemente : ' + ', '.join(map(str, data)) + '.\n'
        statement += '2. Introduceti valorile precedente intr-un AVL.\n'

        super().__init__(statement, data)

    def solve(self):
        data = self.data
        statement = 'Idee de rezolvare :\n'
        statement +=  '= inserarea se bazeaza pe cea de la BST, cu anumite modificări;\n'
        statement +=  '= după ce am inserat un element în BST trebuie să parcurgem arborele începând de la noul nod adăugat;\n'
        statement +=  '= parcurgem arborele până găsim un nod care are factorul de echilibru mai mic decât -1 sau mai mare decât 1;\n'
        statement +=  '= după ce am găsit acest nod vedem în ce caz de neechilibru ne aflăm: (RR); (LL); (RL); (LR);\n'
        statement +=  '= primul pas este sa vedem ce factor de neechilibru are nodul.' 
        statement +=  ' Dacă factorul este mai mare decât 1 atunci ne alfăm în două cazuri posibile:\n'
        statement +=  ' (LL) și (LR). Dacă factorul este mai mic decât -1 atunci ne aflăm în celelalte două cazuri :'
        statement +=  ' cazul dreapta dreapta (RR) și cazul dreapta stânga (RL);\n'
        statement +=  '= acum trebuie să facem distincția între cele două cazuri rezultate din pasul precedent;\n'
        statement +=  '= după ce am aflat în ce caz ne aflăm aplicam rotația asociată ;\n'
        statement +=  '= vom avea patru functii, fiecare va reprezenta o rotație ;\n'
        statement +=  '= după aplicarea rotației BST-ul devine echilibrat, deci devine un AVL;\n'
        statement +=  '= reluam algoritmul pentru următoarea valoarea introdusă\n'

        preorder_list = list()
        inorder_list = list()

        class Node():
            def __init__(self, value):
                self.right = None
                self.left = None
                self.value = value
                self.height = 1

        class AVL(object) :

            def inorder(self,root):
                if root:
                    self.inorder(root.left)
                    inorder_list.append(root.value)
                    self.inorder(root.right)
            
            def preorder(self,root):
                if root:
                    preorder_list.append(root.value)
                    self.preorder(root.left)                    
                    self.preorder(root.right)
                
            #functie pentru calcularea nivelului unui nod
            def height_node(self, root):
                if root is None: 
                    return 0
                return root.height

            #functie pentru calcularea factorului de echilibru
            def Verifybalance_factor(self, root):
                if root is None:
                    return 0
                    
                return self.height_node(root.left) - self.height_node(root.right)

            #functie pentru rotatia la stanga
            def leftRotation(self, x):
                y = x.right
                Sub_Tree1 = y.left

                y.left = x
                x.right = Sub_Tree1

                x.height = max(self.height_node(x.left), self.height_node(x.right)) + 1
                y.height = max(self.height_node(y.left), self.height_node(y.right)) + 1

                return y

            #functie pentru rotatia la dreapta
            def rightRotation(self, y):
                x = y.left
                Sub_Tree2 = x.right

                x.right = y
                y.left = Sub_Tree2

                x.height = max(self.height_node(x.left), self.height_node(x.right)) + 1
                y.height = max(self.height_node(y.left), self.height_node(y.right)) + 1
                    
                return x

            def insert(self, root, key):

                #introducerea valorilor intr-un BST
                if not root: 
                    return Node(key) 
                elif key < root.value: 
                    root.left = self.insert(root.left, key) 
                else: 
                    root.right = self.insert(root.right, key) 

                #calcularea valorii inaltimii arborelui
                root.height = max(self.height_node(root.left), self.height_node(root.right)) + 1

                #calcularea facorului de echilibru 
                balanca_factor = self.Verifybalance_factor(root)

                #cazul - LL
                if balanca_factor > 1 and key < root.left.value:
                    return self.rightRotation(root)

                #cazul - LR
                if balanca_factor > 1 and key > root.left.value:
                    root.left = self.leftRotation(root.left)
                    return self.rightRotation(root)

                #cazul - RR
                if balanca_factor <-1 and key > root.right.value:
                    return self.leftRotation(root)

                #cazul - RL
                if balanca_factor < -1 and key < root.right.value:
                    root.right = self.rightRotation(root.right)
                    return self.leftRotation(root)

                return root
            
            #functie care va returna parcurgerea in inorder si preorder
            def show(self, root): 
        
                if not root: 
                    return
        
                sta = ''
                self.inorder(root)
                sta += '3. Elementele sortate in inordine sunt: ' + str(inorder_list) + '\n'

                self.preorder(root)
                sta += '4. Elementele sortate in preordine sunt: ' + str(preorder_list) + '\n'

                return sta

        def insert_bst(root, value):
            node = Node(value)
            if root is not None:
                if node.value < root.value:
                    root.left = insert_bst(root.left, value)
                if node.value > root.value:
                     root.right = insert_bst(root.right, value)
            else:
                root = node
            return root

        AVLTree = AVL()

        r = None
        for i in range(0, len(data)):
            r = AVLTree.insert(r, data[i])

        global tree
        tree = ''
        def draw(root, space):
            global tree
            if root is None:
                return None
            
            space += 10
            draw(root.right, space)
            tree += '\n'
            tree += ' ' * space + str(root.value)
            draw(root.left, space)

        statement += AVLTree.show(r)
        R = Node(preorder_list.pop(0))
        for i in range(0, len(preorder_list)):
            insert_bst(R,preorder_list.pop(0))
        draw(R, -8)
        statement_draw_tree = tree
        statement += '5. Arborele AVL are urmatoarea forma : ' + statement_draw_tree + '\n'
        solution = statement 
        return solution
