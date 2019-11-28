from problem import Problem
sdr = []
index = 0
sol = ''
desen = ''
class Node:  #structura care ajuta la memorarea unui nod si a copiilor - stanga/dreapta

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def insert(root, x): #functie care construieste un ABC

    node = Node(x)
    if root.data >= node.data: #daca radacina e mai mare decat nodul pe care il inserez
        if root.left is None:
            root.left = node #daca e liber pe stanga, inseram in stanga
        else:
            insert(root.left, node.data) #daca nu e liber pe stanga, repet procedeul considerand ca radacina fiul stg
    else: #daca radacina e mai mica decat nodul pe care il inserez (STG<R<DR in ABC)
        if root.right is None:
            root.right = node  #daca e liber pe dreapta, inseram in dreapta
        else:
            insert(root.right, node.data) #daca nu e liber pe dreapta, repet procedeul considerand ca radacina fiul drept

def postorder(root): #FACE SDR
    if root:
        postorder(root.left)
        postorder(root.right)
        sdr.append(root.data)

def constructABC(SDR, start, end):
        global index
        node = Node(SDR[end])
        if start > end:
            return None
        for i in range(end, start - 1, -1):
            index = i - 1
            if SDR[i] < node.data:
                index = i
                node.left = constructABC(SDR, start, index)

                break
            else:
                node.right = constructABC(SDR, index + 1, end - 1)
        return node

#tree = ''

def draw1(root, space):
        global tree
        if root is None:
            return None
        draw1(root.right, space + 7)
        tree += ' ' * (space - 3) + str(root.data)
        tree += '\n'
        draw1(root.left, space + 7)


def draw(root, nrSpatii, nrMinus):
    global desen
    if (root):
        draw(root.right, nrSpatii + 8, nrMinus - 2)
        desen += "\n" + (nrSpatii) * " "
        desen += str(root.data) + " " + "-" * nrMinus + "\n"
        desen += nrSpatii * " " + "|\n"
        draw(root.left, nrSpatii + 8, nrMinus - 2)

def printTree(root):  # Asta trebuie sa afiseze in program si nush cum inca
    global sol
    if root:

        sol += "Nod: " + str(root.data)
        if root.left:

            sol += "; Fiu stanga: " + str(root.left.data)

        if root.right:

            sol += "; Fiu dreapta: " + str(root.right.data)

        sol += "\n"
        printTree(root.left)
        printTree(root.right)


class Problem13(Problem):
    def __init__(self):
        statement = "RAP: Primind parcurgerea in postordine (SDR) a unui arbore binar, reconstruiti arborele\n"
        data = []
        import random
        from random import randint
        data = random.sample(range(50), randint(7, 9))  # vector random din care fac ABC
        root = Node(data[0])
        for i in range(1, len(data)):  # face ABC
            insert(root, data[i])

        postorder(root)  # parcurgere pt ABC ul construit

        statement += "SDR: " + str(sdr) + "\n"
        super().__init__(statement, data)

    def solve(self):
        n = len(sdr)
        radacina = constructABC(sdr, 0, n - 1)
        solution = "Idee de rezolvare: \n"
        solution += "Deoarece deja stim ca se cere un Arbore Binar de Cautare, fixam ultimul element din parcurgere ca fiind radacina si o impartim in doua intervale: \n"
        solution += "\t-prima parte contine numere mai mici decat radacina si setul de elemente va merge in stanga acesteia \n"
        solution += "\t-a doua parte contine numere mai mari decat radacina si setul de elemente va merge in dreapta acesteia \n"
        solution += "Repetam recursiv pentru fiecare nod.\n"
        solution += "Arborele construit este:\n\n\n"
        printTree(radacina)
        solution += sol
        #draw1(radacina,0)
        #print(tree)
        draw(radacina, 0, 7)
        solution += desen

        return solution

p = Problem13()
print(p.statement)
print(p.solve())
