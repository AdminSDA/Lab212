import sys
import random
from random import randint
from problem import Problem

solution = ""
statement = ""

class Node(object):
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1


class AVL(object):
    def insertNode(self, root, key):
        if not root:
            return Node(key)
        elif key < root.key:
            root.left = self.insertNode(root.left, key)
        else:
            root.right = self.insertNode(root.right, key)
        root.height = 1 + max(self.Height(root.left), self.Height(root.right))

        balance = self.Balance(root)
        if balance > 1:
            if key < root.left.key:
                return self.rightRotate(root)
            else:
                root.left = self.leftRotate(root.left)
                return self.rightRotate(root)

        if balance < -1:
            if key > root.right.key:
                return self.leftRotate(root)
            else:
                root.right = self.rightRotate(root.right)
                return self.leftRotate(root)

        return root

    def leftRotate(self, x):
        if x == None:
            return None
        y = x.right
        if y == None:
            return None
        z = y.left
        y.left = x
        x.right = z
        x.height = 1 + max(self.Height(x.left), self.Height(x.right))
        y.height = 1 + max(self.Height(y.left), self.Height(y.right))
        return y

    def rightRotate(self, x):
        if x == None:
            return None
        y = x.left
        if y == None:
            return None
        z = y.right
        y.right = x
        x.left = z
        x.height = 1 + max(self.Height(x.left), self.Height(x.right))
        y.height = 1 + max(self.Height(y.left), self.Height(y.right))
        return y

    def Height(self, root):
        if not root:
            return 0
        return root.height

    def Balance(self, root):
        if not root:
            return 0
        return self.Height(root.left) - self.Height(root.right)

    def preorder(self, root):
        if not root:
            return
        print("{0} ".format(root.key), end="")
        self.preorder(root.left)
        self.preorder(root.right)

    def printTree2(self, pct, indent, last):
        global solution
        if pct != None:
            solution += indent
            if last:
                solution += "R----"
                indent += "     "
            else:
                solution += "L----"
                indent += "|    "
            solution += str(pct.key) + "\n"
            self.printTree2(pct.left, indent, False)
            self.printTree2(pct.right, indent, True)

    def printTree(self, pct, indent, last):
        global statement
        if pct != None:
            statement += indent
            if last:
                statement += "R----"
                indent += "     "
            else:
                statement += "L----"
                indent += "|    "
            statement += str(pct.key) + "\n"
            self.printTree(pct.left, indent, False)
            self.printTree(pct.right, indent, True)

    def find(self, root, val):
        if not root:
            return root
        elif val < root.key:
            root.left = self.find(root.left, val)
        elif val > root.key:
            root.right = self.find(root.right, val)
        else:
            if root.left is None:
                temp = root.right
                root = None
                return temp

            elif root.right is None:
                temp = root.left
                root = None
                return temp
            temp = self.getMinValueNode(root.right)
            root.key = temp.key
            root.right = self.find(root.right, temp.key)

    def getMinValueNode(self, root):
        if root is None or root.left is None:
            return root
        return self.getMinValueNode(root.left)

    def anotherfind(self, root, val):

        if root == None:
            return None
        if root.key == None:
            return None
        while (root.key != val):
            if (val < root.key):
                root = root.left
            else:
                root = root.right
        return root



myTree = AVL()
data = []


class problem33(Problem):
    def __init__(self):
        global statement
        statement = "Avem secventa:"
        for i in range(8):
            data.append(randint(1, 100))
        statement += str(data)
        root = None
        for j in data:
            root = myTree.insertNode(root, j)
        statement+="\nPe baza secventei vom crea un AVL" + "\n"
        myTree.printTree(root, "", True)
        statement+="\nAcest arbore va fi dezechilibrat prin rotatii random ale unor noduri alese tot aleatoriu"
        statement+="\nIn cazul in care nodul ales nu are un vecin la stanga sau dreapta, rotatiile nu vor avea loc si se va alege alt nod\n"
        self.root = root

        super().__init__(statement, data)

    def solve(self):
        global solution
        i = 0
        while i < 3:
            x = self.root.key
            while x == self.root.key:
                x = random.choice(self.data)
            solution += "Am ales nodul "
            m = None
            while m == None:
                m = myTree.anotherfind(self.root, x)
            solution += str(x)
            solution += " pentru a dezechilibra arborele\n"
            b = random.choice([0, 1])
            if b == 0:
                if m.left:
                    myTree.leftRotate(m)
                    if not m.left:
                        solution += "Nu putem sa rotim la stanga nodul\n"
                    solution += "Dupa rotatia la stanga, arborele este:\n"

                    myTree.printTree2(self.root, "", True)
                else:
                    solution += "Nu putem sa rotim la stanga nodul\n"
            else:
                if m.right:
                    myTree.rightRotate(m)
                    if not m.right:
                        solution += "Nu putem sa rotim la dreapta nodul\n"
                    solution += "Dupa rotatia la dreapta, arborele este:\n"

                    myTree.printTree2(self.root, "", True)
                else:
                    solution += "Nu putem roti la dreapta nodul\n"
            i += 1
        return solution



