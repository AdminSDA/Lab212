import sys
import random
from random import randint
from problem import Problem

solution = ""


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
        else:il punem in vectorul de solutii si trecem la urmatorul element din data; daca nu, scoatem elementul din Q2 si il adaugam la final in Q1. Pentru optimizare, putem incepe algoritmul dupa adaugarea primului element in coada Q1, nu este nevoie sa adaugam intai toate elementele pentru ca algoritmul sa functioneze, insa avem nevoie de verificari suplimentare pentru a nu adauga/sterge elemente inexistente(nule) din cozi.<br><br>Secventa finala este: f 1 u I_1 j I_2 o 1 c 1 i 1 v 1 d 1 r I_1 1 2 1 2 1 2 I_2 I_2 1 2 I_2 I_2 I_1 I_2 <br><strike>f</strike> <strike>u</strike> <strike>j</strike> <strike>o</strike> <strike>c</strike> <strike>i</strike> <strike>v</strike> <strike>d</strike> <strike>r</strike> <strike>j</strike> <strike>o</strike> <strike>c</strike> <strike>r</strike> <br><strike>f</strike> <strike>j</strike> <strike>o</strike> <strike>c</strike> <strike>i</strike> <strike>v</strike> <strike>r</strike> <strike>j</strike> <strike>o</strike> <strike>c</strike> <br>
</pre>
<pre id="1" onclick="afisare(1)">

Problem3
 Idee de rezolvare: Selectam primul element din vectorul b. Luam fiecare element din vectorul a si il introducem in stiva.
Cat timp stiva nu este goala si ultimul element din stiva este egal cu elementul curent din b, atunci il scoatem, afisam p si trecem mai departe in b.
	Adaugam 4 la operatii si adaugam elementul 4 in stiva
	<table border=1><tr><td>4</td></tr></table>
	Adaugam p la operatii si scoatem elementul 4 din stiva
	<table border=1><tr><td><strike>4</strike> </td></tr></table>
	Adaugam 2 la operatii si adaugam elementul 2 in stiva
	<table border=1><tr><td>2</td></tr></table>
	Adaugam 5 la operatii si adaugam elementul 5 in stiva
	<table border=1><tr><td>2</td><td>5</td></tr></table>
	Adaugam p la operatii si scoatem elementul 5 din stiva
	<table border=1><tr><td>2</td><td><strike>5</strike> </td></tr></table>
	Adaugam 3 la operatii si adaugam elementul 3 in stiva
	<table border=1><tr><td>2</td><td>3</td></tr></table>
	Adaugam p la operatii si scoatem elementul 3 din stiva
	
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
        if pct != None:
            sys.stdout.write(indent)
            if last:
                sys.stdout.write("R----")
                indent += "     "
            else:
                sys.stdout.write("L----")
                indent += "|    "
            print(pct.key)
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


print("Arborele creat:")
myTree = AVL()
data = []


class Problem33(Problem):
    def __init__(self):
        statement = "Avem secventa:"
        for i in range(8):il punem in vectorul de solutii si trecem la urmatorul element din data; daca nu, scoatem elementul din Q2 si il adaugam la final in Q1. Pentru optimizare, putem incepe algoritmul dupa adaugarea primului element in coada Q1, nu este nevoie sa adaugam intai toate elementele pentru ca algoritmul sa functioneze, insa avem nevoie de verificari suplimentare pentru a nu adauga/sterge elemente inexistente(nule) din cozi.<br><br>Secventa finala este: f 1 u I_1 j I_2 o 1 c 1 i 1 v 1 d 1 r I_1 1 2 1 2 1 2 I_2 I_2 1 2 I_2 I_2 I_1 I_2 <br><strike>f</strike> <strike>u</strike> <strike>j</strike> <strike>o</strike> <strike>c</strike> <strike>i</strike> <strike>v</strike> <strike>d</strike> <strike>r</strike> <strike>j</strike> <strike>o</strike> <strike>c</strike> <strike>r</strike> <br><strike>f</strike> <strike>j</strike> <strike>o</strike> <strike>c</strike> <strike>i</strike> <strike>v</strike> <strike>r</strike> <strike>j</strike> <strike>o</strike> <strike>c</strike> <br>
</pre>
<pre id="1" onclick="afisare(1)">

Problem3
 Idee de rezolvare: Selectam primul element din vectorul b. Luam fiecare element din vectorul a si il introducem in stiva.
Cat timp stiva nu este goala si ultimul element din stiva este egal cu elementul curent din b, atunci il scoatem, afisam p si trecem mai departe in b.
	Adaugam 4 la operatii si adaugam elementul 4 in stiva
	<table border=1><tr><td>4</td></tr></table>
	Adaugam p la operatii si scoatem elementul 4 din stiva
	<table border=1><tr><td><strike>4</strike> </td></tr></table>
	Adaugam 2 la operatii si adaugam elementul 2 in stiva
	<table border=1><tr><td>2</td></tr></table>
	Adaugam 5 la operatii si adaugam elementul 5 in stiva
	<table border=1><tr><td>2</td><td>5</td></tr></table>
	Adaugam p la operatii si scoatem elementul 5 din stiva
	<table border=1><tr><td>2</td><td><strike>5</strike> </td></tr></table>
	Adaugam 3 la operatii si adaugam elementul 3 in stiva
	<table border=1><tr><td>2</td><td>3</td></tr></table>
	Adaugam p la operatii si scoatem elementul 3 din stiva
	
            data.append(randint(1, 100))
        statement += str(data)
        root = None
        for j in data:
            root = myTree.insertNode(root, j)
        myTree.printTree(root, "", True)
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


#p = Problem33()
#print(p.statement)
#il punem in vectorul de solutii si trecem la urmatorul element din data; daca nu, scoatem elementul din Q2 si il adaugam la final in Q1. Pentru optimizare, putem incepe algoritmul dupa adaugarea primului element in coada Q1, nu este nevoie sa adaugam intai toate elementele pentru ca algoritmul sa functioneze, insa avem nevoie de verificari suplimentare pentru a nu adauga/sterge elemente inexistente(nule) din cozi.<br><br>Secventa finala este: f 1 u I_1 j I_2 o 1 c 1 i 1 v 1 d 1 r I_1 1 2 1 2 1 2 I_2 I_2 1 2 I_2 I_2 I_1 I_2 <br><strike>f</strike> <strike>u</strike> <strike>j</strike> <strike>o</strike> <strike>c</strike> <strike>i</strike> <strike>v</strike> <strike>d</strike> <strike>r</strike> <strike>j</strike> <strike>o</strike> <strike>c</strike> <strike>r</strike> <br><strike>f</strike> <strike>j</strike> <strike>o</strike> <strike>c</strike> <strike>i</strike> <strike>v</strike> <strike>r</strike> <strike>j</strike> <strike>o</strike> <strike>c</strike> <br>
</pre>
<pre id="1" onclick="afisare(1)">

Problem3
 Idee de rezolvare: Selectam primul element din vectorul b. Luam fiecare element din vectorul a si il introducem in stiva.
Cat timp stiva nu este goala si ultimul element din stiva este egal cu elementul curent din b, atunci il scoatem, afisam p si trecem mai departe in b.
	Adaugam 4 la operatii si adaugam elementul 4 in stiva
	<table border=1><tr><td>4</td></tr></table>
	Adaugam p la operatii si scoatem elementul 4 din stiva
	<table border=1><tr><td><strike>4</strike> </td></tr></table>
	Adaugam 2 la operatii si adaugam elementul 2 in stiva
	<table border=1><tr><td>2</td></tr></table>
	Adaugam 5 la operatii si adaugam elementul 5 in stiva
	<table border=1><tr><td>2</td><td>5</td></tr></table>
	Adaugam p la operatii si scoatem elementul 5 din stiva
	<table border=1><tr><td>2</td><td><strike>5</strike> </td></tr></table>
	Adaugam 3 la operatii si adaugam elementul 3 in stiva
	<table border=1><tr><td>2</td><td>3</td></tr></table>
	Adaugam p la operatii si scoatem elementul 3 din stiva
	print(p.solve())

