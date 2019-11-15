
from problem import Problem

class Problem2(Problem):
    def __init__(self):

        import random

        data1 = random.sample(range(97, 123), random.randint(7, 10) ) # generam un sir de 5-8 numere din intervalul 97-123 (a-z,lowercase,ASCII)
        for i in range(0,len(data1)):
            data1[i]=chr(data1[i]) # convertim numerele in echivalentul lor din codul ASCII

        data2=[]
        data2.extend(data1) # adaugam literele in lista
        random.shuffle(data2) # randomizam lista

        data1_string=""

        for i in data1:
            data1_string+=" "+str(i)

        data2_string=""

        for i in data2:
            data2_string+=" "+str(i)

        statement = "<br><br>Problema 2 - 2C:<br><br>"
        statement += "Aveti la dispozitie 2 cozi. Introduceti elementele " + str(data1_string) + " in aceasta ordine, obtinand la final "
        statement += str(data2_string) + ".\n\n"
        statement += "Operatii: <br><br> 'caracter' -> se introduce caracterul in prima coada <br><br>"
        statement += "1 -> se scoate din prima coada si se introduce in a doua coada <br><br>"
        statement += "2 -> se scoate din a doua coada si se introduce in prima coada <br><br>"
        statement += "I_1 se extrage un element din coada 1 si se afiseaza <br><br>"
        statement += "I_2 se extrage un element din coada 2 si se afiseaza <br><br>"

        data = (data1, data2)

        super().__init__(statement, data)

    def solve(self):
        shuffled_data=self.data[0]
        data=self.data[1]


        class Node(object):  # clasa care defineste elemente din coada
            def __init__(n, x = None): # structura care defineste campurile elementelor
                n.value=x # valoarea elementului
                n.next=None # succesorul


        class Queue(object): # clasa care defineste coada
            def __init__(q):
                q.size=0 # lungimea
                q.front=None # primul element
                q.rear=None # ultimul element
            
            def Push(q, x): # adauga un element in coada
                n = Node(x)
                if q.size==0: # daca coada e goala, elementul adaugat este singurul, primul si ultimul
                    q.front=q.rear=n
                else:
                    q.rear.next=n # cream legatura catre noul nod
                    q.rear=n # noul nod devine noul ultim element
                q.size+=1 #lungimea cozii creste
            
            def Pop(q): # stergem un element din coada
                x = q.front.value # luam valoarea primului element
                q.front=q.front.next # al doilea element din coada devine primul element
                q.size-=1 # lungimea cozii scade
                if q.size==0: # daca coada e goala, front devine None automat, dar trebuie sa testam pentru rear
                    q.rear=None
                return x # daca se da print, functia returneaza valoarea stearsa din coada

            def q_front(q): # returneaza primul element din coada
                if q.size==0:
                    return None
                return q.front.value

            def q_rear(q): # returneaza ultimul element din coada
                if q.size==0:
                    return None
                return q.rear.value



        q1=Queue() # declaram cozile 1 si 2
        q2=Queue()

        step_Q1=""
        step_Q2=""
        
        solution="<br><br>Idee de rezolvare:<br><br>"
        solution+="Initial, avem doua liste: shuffled_data si data. Trebuie sa ""ordonam"" elementele din shuffled_data "
        solution+="in ordinea pe care o au in data. Pentru simplitate, prima coada va fi numita in continuare Q1, iar a doua coada Q2. "
        solution+="Introducem elementele din shuffled_data in Q1, si parcurgem lista data cu un contor, verificand la fiecare pas "
        solution+="daca elementul curent din data este egal cu front-ul lui Q1; daca da, il eliminam din Q1 si il punem in vectorul "
        solution+="de solutii si trecem la urmatorul element din data; daca nu, il eliminam din Q1 si il adaugam in Q2, la final. "
        solution+="Repetam aceeasi pasi pentru Q2: comparam front-ul lui Q2 cu elementul curent din data, daca sunt egale, scoatem "
        solution+="elementul din Q2, il punem in vectorul de solutii si trecem la urmatorul element din data; daca nu, scoatem elementul "
        solution+="din Q2 si il adaugam la final in Q1. Pentru optimizare, putem incepe algoritmul dupa adaugarea primului element in coada "
        solution+="Q1, nu este nevoie sa adaugam intai toate elementele pentru ca algoritmul sa functioneze, insa avem nevoie de verificari "
        solution+="suplimentare pentru a nu adauga/sterge elemente inexistente(nule) din cozi."
        solution+="<br><br>Secventa finala este: "

        k=0 # contor care se "plimba" prin lista data
        l=0 # contor care se "plimba" prin lista shuffled_data

        # Idee de rezolvare: Adaugam elementele lui data in prima coada,si parcurgem circular utilizand cele doua cozi aflate la dispozitie,
        # comparand constant primul element din coada 1 si coada 2 cu elementul l din shuffled_data; daca sunt egale, il scoatem din coada
        # si il afisam. Ciclarea se repeta pana cand l este egal cu lungimea lui shuffled_data

        while l<len(data):

            if k<len(shuffled_data):
                q1.Push(shuffled_data[k])
                solution+=str(shuffled_data[k])+" "
                step_Q1 += "<strike>" + str(shuffled_data[k]) + "</strike> "
                k+=1
                
            if q1.q_front()==data[l]:
                l+=1
                q1.Pop()
                solution+="I_1 "
            else:
                if q2.q_front()==data[l]:
                    l+=1
                    q2.Pop()
                    solution+="I_2 "
                else:
                    if q1.q_front()==None and q2.q_front()!=None:
                        y=q2.Pop()
                        q1.Push(y)
                        solution+="2 "
                        step_Q1 += "<strike>" + str(y) + "</strike> "
                    else:
                        if q2.q_front()==None and q1.q_front()!=None:
                            y=q1.Pop()
                            q2.Push(y)
                            solution+="1 "
                            step_Q2 += "<strike>" + str(y) + "</strike> "

                        else:
                            if q2.q_front()!=None and q1.q_front()!=None:
                                y=q1.Pop()
                                q2.Push(y)
                                solution+="1 "
                                step_Q2 += "<strike>" + str(y) + "</strike> "


        solution = solution + "<br>" + step_Q1 + "<br>" + step_Q2 + "<br>"
        return solution

