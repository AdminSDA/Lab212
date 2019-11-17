from problem import Problem
import random
from random import randint

class Problem1(Problem):
    def __init__(self):
        statement = 'SS. Avand stiva: '
        data = []
        s = range(1, 11)#[1,2,3,4,5,6,7,8,9,10]
        k= random.randint(7,10)
        data = random.sample(s, k)
        l = len(data)
        statement += str(data)
        self.nr_de_sters= random.choice(data[1:(int(l/2))])
        statement += " gasiti o succesiune de mutari a.i. sa stergeti din stiva elementul " + str(self.nr_de_sters) + " avand la dispozitie 2 cozi si operatiile:\n"
        statement += "P -> se extrage un el. din stiva, se introduce in prima coada\n"
        statement += "S -> se sterge un element din stiva\n"
        statement += "1 -> se extrage un el. din coada 1 si se introduce in coada 2\n"
        statement += "2 -> se extrage un el. din coada 2 si se introduce in coada 1\n"
        statement += "I_1 -> se extrage un el. din coada 1 si se introduce in stiva\n"
        statement += "I_2 -> se extrage un el. din coada 2 si se introduce in stiva\n"

        super().__init__(statement, data)

    def solve(self):
        succ=""
        solution = "Idee de rezolvare: Mutam elementele din stiva in prima coada pana la elementul cautat, pe care il  stergem. Mutam elem. din prima coada in cealalta pana cand in prima coada ramane un singur element,pe care il adaugam in stiva. Repetam procedeul pentru fiecare coada alternativ, pana cand acestea devin vide si astfel elementele sunt adaugate in ordinea corecta in stiva\n"
        stiva = self.data
        coada1 = []
        coada2 = []
        a = self.nr_de_sters
        ls = len(stiva)
        i = len(stiva)
        i = i - 1
        solution+="\nStiva este: " + str(stiva)
        solution += "\nRezolvare: Mutam elementele din stiva in coada 1, pana gasim elementul de sters, adica " + str(a) + "\n"
        while i >= 0:
            if a != stiva[i]:
                solution += "P: Mutam elementul " + str(stiva[i]) + " in coada 1\n"
                succ+="P, "
                coada1.append(stiva.pop())
                i = len(stiva) - 1

            else:
                stiva.pop()
                solution +="S: Stergem elementul " + str(a) + " din stiva\n"
                succ += "S, "
                break
        solution += "\n"
        solution += "Stiva devine: " + str(stiva) + ", prima coada devine: " + str(coada1) + " a doua coada devine " + str(coada2) +"\n"
        solution += "\n"
        j = len(coada1)
        k = len(coada2)
        l = len(stiva)

        if k != 0 or j!=0:
            solution += "Mutam cate un element din coada nevida in coada vida pana cand in coada din care se face extragerea ramane un singur el.,pe care il adaugam in stiva:\n"
            while ls != l + 1:
                j = len(coada1)
                k = len(coada2)
                l = len(stiva)
                if k == 0 and j !=0 :

                    while j > 1:
                        coada2.append(coada1.pop(0))
                        lu = len(coada2)-1
                        j = len(coada1)
                        solution += "1: Mutam din coada 1 elem. " + str(coada2[lu]) + " in coada 2\n"
                        succ += "1, "
            
                    if j == 1:
                        solution += "I_1: Stergem elementul " + str(coada1[0]) + " din coada 1 si apoi il adaugam in stiva\n"
                        succ += "I_1, "
                        stiva.append(coada1.pop())
                        j = len(coada1)
                    solution += "\n"
                    solution += "Stiva devine: " + str(stiva) + ", prima coada devine: " + str(coada1) + ", a doua coada devine: " + str(coada2) + "\n"
                    solution += "\n"

                if j == 0 and k !=0 :

                    while k > 1:
                        coada1.append(coada2.pop(0))
                        lun = len(coada1)-1
                        k = len(coada2)
                        solution += "2: Mutam din coada 2 elem " + str(coada1[lun]) + " in coada 1\n"
                        succ += "2, "

                    if k == 1:
                        solution += "I_2: Stergem elementul " + str(coada2[0]) + " din coada 2 si apoi il adaugam in stiva\n"
                        succ += "I_2, "
                        stiva.append(coada2.pop())
                        k = len(coada2)
                    solution += "\n"
                    solution += "Stiva devine" + str(stiva) + ", prima coada devine:" + str(coada1) + ", a doua coada devine:" + str(coada2) + "\n"
        solution += "Succesiunea operatiilor este: "
        succ = succ[:-2]
        solution = solution + succ
        solution += "\n"
        return solution
