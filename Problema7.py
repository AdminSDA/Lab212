from problem import Problem
import random
srd=[]
rsd=[]
sdr=[]
root_index_RSD=0



# SRD - INORDINE
# RSD - PREORDINE
# SDR - POSTORDINE


class Node:  #structura care ajuta la memorarea unui nod si a copiilor - stanga/dreapta
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


"""Functie care insereaza intr-un ABC un nod x"""
def insert(root, x):
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


"""Functie care construieste un arbore binar oarecare in mod recursiv, folosind SRD si RSD"""
def ConstructBT(SRD, RSD, start, end):
    global root_index_RSD
    if (start > end):
        return None

    node = Node(RSD[root_index_RSD]) #nodul curent din parcurgerea preordine
    root_index_RSD += 1

    #daca nu are copii
    if (start == end):
        return node
    #cautam pozitia lui in parcurgerea inordine

    root_index_SRD = search(SRD, start, end, node.data)
    #construim subarborele stang si drept

    node.left = ConstructBT(SRD, RSD, start, root_index_SRD - 1)
    node.right = ConstructBT(SRD,RSD, root_index_SRD + 1, end)

    return node



"""Functie care cauta o valoare intr-un vector intre 2 pozitii"""
def search(v, start, end, x):
    i = 0
    for i in range(start, end + 1):
        if (v[i] == x):
           return i



"""Functie care pune intr-un vector parcurgerea in inordine a unui arbore binar""" #FACE SRD
def inorder(root):
    if root:

        inorder(root.left)
        srd.append(root.data)
        inorder(root.right)


"""Functie care pune intr-un vector parcurgerea in preordine a unui arbore binar"""  #FACE RSD
def preorder(root):
    if root:

        rsd.append(root.data)
        preorder(root.left)
        preorder(root.right)


"""Functie care pune intr-un vector parcurgerea postordine a unui arbore binar""" #FACE SDR
def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        sdr.append(root.data)



class Problem7(Problem):
    def __init__(self):


      statement="Problema 7: RA \n"
      statement+= "Reconstruiti arborele care are parcurgerile RSD si SRD date si afisati parcurgerea SDR\n"


      data = []
      data = random.sample(range(50), random.randint(5, 7))  # vector creat random din care vom face ABC


      self.root = Node(data[0])

      for i in range(1, len(data)):

            insert(self.root, data[i])

      #statement+= "ABC- ul obtinut este:\n"

      self.srd=srd
      self.rsd=rsd
      self.RSD = []
      self.SRD = []

      inorder(self.root)
      preorder(self.root)

      self.reden = {}
      for i in self.rsd:
         self.reden[i] = random.randint(1, 50)  #facem dictionarul prin care redenumim elementele din ABC


      for i in self.rsd:
         self.RSD.append(self.reden[i])

      for i in self.srd:
          self.SRD.append(self.reden[i])  # refacem cele doua parcurgeri in functia de redenumire

      statement+=" Parcurgerea RSD :\n" + str(self.RSD) + "\n"
      statement+=" Parcurgerea SRD :\n" + str(self.SRD) + "\n"

      super().__init__(statement, data)






    def solve(self):


      SRD= self.SRD
      RSD= self.RSD
      n = len(SRD)

      solution="Reconstruim arborele si facem parcurgerile:\n"
      self.radacina = ConstructBT(SRD,RSD,0, n-1)


      #pentru verificare
      inorder(self.radacina)
      solution+="Parcurgerea SRD a arborelui binar creat este:" + str(srd[n:]) + "\n" #in srd e deja o parcurgere si concateneaza, deci ma uit de la jumate


      preorder(self.radacina)
      solution+="Parcurgerea RSD a arborelui binar creat este:" + str(rsd[n:])  + "\n"
      #final de verificare

      postorder(self.radacina)
      solution+="Parcurgerea SDR a arborelui binar creat este: " + str(sdr) + "\n"
      return solution

p = Problem7()
print(p.statement)
print(p.solve())

