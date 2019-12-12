from problem import Problem
import random
rsd = []
index = 0
sol = ""
sol2 = ""
desen = ''


# Structura care ajuta la memorarea unui nod si a copiilor - stanga/dreapta
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


# Functie care construieste un ABC
def insert(root, x):
    node = Node(x)

    if root.data >= node.data:  # daca radacina e mai mare decat nodul pe care il inserez

        if root.left is None:
            root.left = node  # daca e liber pe stanga, inseram in stanga

        else:
            insert(root.left, node.data)  # daca nu e liber pe stanga, repet procedeul considerand ca radacina fiul stg

    else:  # daca radacina e mai mica decat nodul pe care il inserez (STG<R<DR in ABC)

        if root.right is None:
            root.right = node   # daca e liber pe dreapta, inseram in dreapta
        else:
            insert(root.right, node.data)  # daca nu e liber pe dreapta, repet procedeul -> radacina= fiul drept


# Functie care completeaza arborele - unde exista un sigur fiu mai adauga un fiu -1; adauga 2 fii la frunze, ambii -1
def completare(root):
    node = Node(-1)
    if root.data != node.data:
        if root.left is None:
            root.left = node
        if root.right is None:
            root.right = node
        completare(root.left)
        completare(root.right)


# Functie care face RSD
def preorder(root):
    if root:
        rsd.append(root.data)
        preorder(root.left)
        preorder(root.right)


# Functie care construieste in mod recursiv un AB folosind RSD
def construct_ab(RSD):
    global index
    node = Node(None)

    if index > len(RSD) or RSD[index] == "N":
        return None
    else:

        node.data = RSD[index]

        index += 1
        node.left = construct_ab(RSD)
        index += 1
        node.right = construct_ab(RSD)

    return node

def draw(root, nrSpatii, nrMinus):
    global desen
    if (root):
        draw(root.right, nrSpatii + 8, nrMinus - 2)
        desen += "\n" + (nrSpatii) * " "
        desen += str(root.data) + " " + "-" * nrMinus + "\n"
        desen += nrSpatii * " " + "|\n"
        draw(root.left, nrSpatii + 8, nrMinus - 2)



def printtree(root):
    global sol
    if root:

        sol += "Nod: " + str(root.data) + " "
        if root.left:

            sol += "Fiu stanga: " + str(root.left.data) + " "

        if root.right:

            sol += "Fiu dreapta: " + str(root.right.data) + " "

        sol += "\n"
        printtree(root.left)
        printtree(root.right)


class Problem15(Problem):
    import random
    def __init__(self):

        statement = "Problema 15 (PN): Primind parcurgerea in preordine (RSD) a unui arbore binar care contine NULL " \
                    "daca nu exista nod, reconstruiti arborele\n"
        data = []
        data = random.sample(range(0, 50), random.randint(5, 8))  # vector random din care fac ABC
        #statement += "Setul de elemente random din care vom face ABC este: " + str(data) + "\n"

        root = Node(data[0])
        for i in range(1, len(data)):  # face ABC
            insert(root, data[i])

        # Completam ABC
        completare(root)
        # printtree(root)

        preorder(root)   # parcurgere pt ABC ul construit
        # print(rsd)

        self.RSD = []
        lista_random = random.sample(range(0, 50), len(rsd))  # contine elemente random unice
        # print(lista_random)

        # dictionar ca sa devina arbore oarecare - redenumim fiecare elem din parcurgere, -1 devine N
        # ma asigur ca valorile random nu se repeta
        reden = {}
        j = 0
        for i in range(0, len(rsd)):
            if rsd[i] == -1:
                reden[i] = "N"
            else:
                reden[i] = lista_random[j]
                j += 1

         #Asa arata dictionarul:
         #print(reden)

        # parcurgere RSD pt AB oarecare - parcurgerea dupa ce am redenumit
        for i in range(0, len(rsd)):
            self.RSD.append(reden[i])

        statement += "RSD: " + str(self.RSD) + "\n"

        super().__init__(statement, data)

    def solve(self):

        solution = "Idee de rezolvare: Pentru fiecare nod construim intai subarborele stang, apoi subarborele drept.\n"


        RSD = self.RSD
        radacina = construct_ab(RSD)
        solution += "Arborele construit este: \n"
        printtree(radacina)
        solution = solution + sol


        solution += sol2
        draw(radacina, 0, 7)
        solution += desen
        return solution


p = Problem15()
print(p.statement)
print(p.solve())

