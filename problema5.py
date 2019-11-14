import random

from problem import Problem


class Problem5(Problem):
    def __init__(self):

        limit = random.randint(2, 30) #generam random numarul de elemente ale arborelui
        data = [random.randint(0, 100) for _ in range(1, limit)] #generam random numerele 
        rand = random.choice(data) #alegem un element random din lista
        data.append(rand) #punem rand ca ultimul element din data, urmand sa il separam

        statement = '1. Inserati urmatoarele valori, pe rand, intr-un arbore binar de cautare: '
        statement2 = '\n2. Scrieti nodurile care se pot sterge in doua moduri. '
        statement3 = '\n3. Stergeti elementul: ' + str(rand)
        
        statement += str(data) + statement2 + statement3


        super().__init__(statement, data)

    def solve(self):

        data = self.data
        statement = self.statement
        rand = data[-1] #ultimul element din data reprezinta valoare pe care o vom sterge mai tarziu din arbore
        data.pop() #scoatem ultimul element din data, ramanem doar cu valorile ce urmeaza sa fie puse in vector

        class Node: #definim clasa unui nod cu referinte in stanga si in dreapta (la cei 2 eventuali copii)
            def __init__(self, value):
                self.right = None
                self.left = None
                self.value = value

        SRD_list = list()

        def SRD(root):  #algoritm care afiseaza arborele in inordine
            if root:
                SRD(root.left) #incepem in stanga, dupa afisam radacina, apoi mergem in dreapta
                SRD(root.right) #punem toate valorile intr-o lista pe care o afisam la final
                SRD_list.append(root.value) 

        RSD_list = list()

        def RSD(root):  #algortim care afiseaza arborele in preordine
            if root:
                RSD_list.append(root.value) #incepem cu radacina, dupa mergem in stanga si apoi in dreapta
                RSD(root.left)
                RSD(root.right) #punem toate valorile intr-o lista pe care o afisam la final

        def insert(root, value): #algoritm de inserare a unui nod in arbore
            node = Node(value)   #creare de nod cu valoarea data
            if root is not None:
                if node.value < root.value: #daca nodul nostru este mai mic decat radacina,facem inserarea in stanga
                    root.left = insert(root.left, value)
                if node.value > root.value: #daca nodul nostru este mai mare decat radacina, facem inserarea in dreapta
                    root.right = insert(root.right, value)
            else:
                root = node   #daca nu exista radacina, o facem noi
            SRD_list.clear()
            RSD_list.clear()
            morechildren_list.clear() #golim listele, deoarece arborele s-a modificat

            return root  #retrunam radacina, deoarece avem nevoie de referinta

        def replacement(node): #functie care gaseste cel mai mic nod din dreapta a unui nod
            current = node.right #luam primul nod din dreapta nodului
                                 #functia va fi folosita doar in cazul in care avem noduri cu 2 copii
                                 #deci node.right exista
            while(current.left):  #cat timp exista un copil in stanga, mergem in stanga
                current = current.left

            return current  

        def children(node):  #returneaza numarul de copii al unui nod
            if node.left and node.right:
                return 2
            elif node.left or node.right:
                return 1
            else:
                return 0
        
        morechildren_list = list()

        def morechildren(root): #pune in lista toate elementele care au 2 copii
            if root:
                morechildren(root.left) #parcurgem tot arborele prin recurenta
                if children(root) > 1:
                    morechildren_list.append(root.value)
                morechildren(root.right)

        def parent(root, value):  #returneaza nodul parinte al unui nod
            if root.value == value: #daca nodul nostru este radacina, nu are parinte 
                return None

            parent = None

            while root.value != value:   #parcurgem arborele pana ajungem la valoarea ceruta
                parent = root            #cand iesim din while, parent va ramane 
                if root.value < value:   #nodul de deasupra nodului cu valoarea noastra
                    root = root.right
                else:
                    root = root.left  

            return parent

        def delete(root, value):

            current = root

            while(current.value != value):
                if current.value < value:
                    current = current.right
                else:
                    current = current.left #parcurgem arborele pana cand ajungem la nodul cu valoarea cautata

            current_parent = parent(root, value) #gasim parintele nodului

            if current and children(current) == 0: #cazul in care nodul nu are copii
                
                if current == root:  # daca e radacina, o stergem
                    current = None

                else:                               #cautam referinta nodului parinte la nod si o stergem
                    if current_parent.left and current.value < current_parent.left.value:
                        current_parent.left = None
                    else:
                        current_parent.right = None 

            if current and children(current) == 1: #daca nodul are 1 copil

                if current == root:              #daca nodul e root, copilul sau va deveni root
                    if current.right:
                        current = current.right
                    else:
                        current = current.left  

                else:                                        
                    if current_parent.right == current:            #cautam referinta nodului parinte la nod
                        if current.right:                          #cautam referinta nodului la copilul sau
                            current_parent.right = current.right   #referinta nodului parinte se va duce la 
                        else:                                      #copilul nodului nostru
                            current_parent.right = current.left
                    else:
                        if current.right:
                            current_parent.left = current.right
                        else:
                            current_parent.left = current.left

            if current and children(current) == 2:  #daca nodul are 2 copii
                current_replacement = replacement(current)  #gasim nodul cu valoarea care poate fi pusa nodul nostru
                temp = current_replacement.value
                delete(root, current_replacement.value)#stergem nodul cu care am inlocuit(va fi ori frunza ori cu 1 copil)
                current.value = temp #punem valoare in nodul nostru

            SRD_list.clear()
            RSD_list.clear()
            morechildren_list.clear()  #golim listele deoarece arborele s-a modificat

        r = Node(data[0]) #inseram radacina 
        for i in range(1, len(data)):
            insert(r, data[i]) #inseram restul valorilor in arbore

        st0 = """\nIdee de rezolvare: Vom insera elemente in arbore folosind o functie prin recurenta care
        returneaza radacina arborelui, deoarece avem nevoie de referinta. Stergerea unui element se va face 
        in functie de caz: daca are 0, 1 sau 2 copii. In primele 2 cazuri gasim parintele, cu ajutorul 
        functiei parent, iar apoi mutam referinta nodului parintelui la None, respectiv la copilul 
        nodului. In al treilea caz, cautam nodul cu care nodul nostru va fi inlocuit cu ajutorul 
        functiei minValue(care ia cel mai mic nod din dreapta), punem valoarea in nodul curent, apoi
        stergem nodul cu care am inlocuit. Elementele care pot fi sterse in 2 moduri sunt cele care au 2 copii,
        iar acestea vor fi gasite cu ajutorul functiilor children(calculeaza numarul de copii) si morechildren
        (gaseste nodurile care au 2 copii)"""
             
            

        SRD(r)
        st1 = "\nELementele arborelui in inordine sunt: " + str(SRD_list)

        RSD(r)
        st2 = "\nELementele arborelui in preordine sunt: " + str(RSD_list)

        morechildren(r)
        st3 = "\nElementele care se pot sterge in 2 moduri sunt: " + str(morechildren_list)

        st4 = "\nElementul care trebuie sters este: " + str(rand)
        delete(r, rand)

        RSD(r)
        st5 = "\nArborele, din care s-a sters " + str(rand) + ': ' + str(RSD_list)

        solution = statement + st0 + st1 + st2 + st3 + st4 + st5

        return solution


problem = ProblemABC()
print(problem.solve())

# returnez tot intr-o var solution + idee de rezolvare
