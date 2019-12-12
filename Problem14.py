from problem import Problem
import random
from random import randint
class Node:
    def __init__(self,val):
        self.value=val
        self.leftChild=None
        self.rightChild=None
    def insert(self,data):
        if self.value==data:
            return False
        elif self.value>data:
            if self.leftChild:
                return self.leftChild.insert(data)
            else:
                self.leftChild=Node(data)
                return True
        else:
            if self.rightChild:
                return self.rightChild.insert(data)
            else:
                self.rightChild=Node(data)
                return True
    def find(self,data):
        if(self.value==data):
            return True
        elif self.value > data:
            if self.leftChild:
                return self.leftChild.find(data)
            else:
                return False
        else:
            if self.rightChild:
                return self.rightChild.find(data)
            else:
                return False
    def postorder(self,nodeStr):
        if self:
            if self.leftChild:
                self.leftChild.postorder(nodeStr)
            if self.rightChild:
                self.rightChild.postorder(nodeStr)
            #print(str(self.value))
            nodeStr.append(self.value);

    def _display_aux(self):
        # No child.
        if self.rightChild is None and self.leftChild is None:
            line = '%s' % self.value
            width = len(line)
            height = 1
            middle = width // 2
            return [line], width, height, middle

        # Only left child.
        if self.rightChild is None:
            lines, n, p, x = self.leftChild._display_aux()
            s = '%s' % self.value
            u = len(s)
            first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
            second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
            shifted_lines = [line + u * ' ' for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

        # Only right child.
        if self.leftChild is None:
            lines, n, p, x = self.rightChild._display_aux()
            s = '%s' % self.value
            u = len(s)
            first_line = s + x * '_' + (n - x) * ' '
            second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
            shifted_lines = [u * ' ' + line for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

        # Two children.
        left, n, p, x = self.leftChild._display_aux()
        right, m, q, y = self.rightChild._display_aux()
        s = '%s' % self.value
        u = len(s)
        first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s + y * '_' + (m - y) * ' '
        second_line = x * ' ' + '/' + (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '
        if p < q:
            left += [n * ' '] * (q - p)
        elif q < p:
            right += [m * ' '] * (p - q)
        zipped_lines = zip(left, right)
        lines = [first_line, second_line] + [a + u * ' ' + b for a, b in zipped_lines]
        return lines, n + m + u, max(p, q) + 2, n + u // 2

class Tree:
    def __init__(self):
        self.root=None
        self.size=0
    def insert(self,data):
        if self.root:
            return self.root.insert(data)
        else:
            self.root=Node(data)
            return True
    def find(self,data):
        if self.root:
            return self.root.find(data)
        else:
            return False
    def postorder(self,nodeStr):
        self.root.postorder(nodeStr)

    def display(self):
        lines, _, _, _ = self.root._display_aux()
        linesStr = "";
        for line in lines:
            abc = Tree()
            #print(line)
            linesStr += line + "\n";
        return linesStr;
abc = Tree()
data=[]
class Problem14(Problem):
    def __init__(self):
        statement = "Avem secventa:"
        for i in range(10):
            data.append(randint(1, 100))
        statement += str(data)
        statement +="\n Se va afisa parcurgerea in postordine a arborelui si un exemplu de o secventa care nu poate fi "
        statement +="parcurgerea in postordine a unui arbore si un motiv pentru care nu poate fi SDR"
        super().__init__(statement, data)

    def solve(self):
        for i in range(10):
            abc.insert(self.data[i])
        solution ="Idee de rezolvare:\n"
        solution +="Arborele binar de cautare se construieste pe principiul: un element mai mic decat tatal lui merge in stanga, iar elementul mai mare decat tatal lui merge in dreapta"
        solution += "\n Arborele binar de cautare construit pe baza secventei este:\n"
        solution += str(abc.display())
        solution +="\nParcurgere in postordine inseamna: elementul din stanga, elementul din dreapta,radacina"
        solution += "\n Parcurgerea in postordine este:"
        nodeStr = [];
        abc.postorder(nodeStr);
        solution += str(nodeStr);
        return solution

p = Problem14()
print(p.statement)
print(p.solve())