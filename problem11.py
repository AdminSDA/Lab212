from problem import Problem
import random


class Problem11(Problem):
    def __init__(self):


        ls = random.randint(1,5)

        if ls == 1:
            data = random.sample(range(100),random.randint(5, 9))  # din numerele mai mici decat 100, alegem intre 5 si 9
            pivot = random.choice(data)
            data = [data, pivot]
            sir = data[0]  # retin sirul generat din numere la intamplare in sir
            u = len(sir)  # lungimea sirului, in cazul nostru este len(sir)
            p = 0
            v = [0 for i in range(1,101)]
            nr = 0
            piv = 0
            for i in range(p, u - 1):
                v[sir[i]] = 1
            for i in range(0, 99):
                if v[i] == 1:
                    nr = nr + 1
                    if nr == u//2:
                        piv = i
                        break
            portie = nr
            sir[portie], sir[u - 1] = sir[u - 1], sir[portie]
            i = p - 1
            for j in range(p, u):
                if sir[j] > piv:
                    i = i + 1  # daca valoarea elementului este mai mica decat cea a pivotului, crestem valoarea indexului i
                    sir[i], sir[j] = sir[j], sir[i]

            statement = "11. Partitionati Lomuto urmatorul vector: " + str(sir) + " folosind pivotul: " + str(
                piv) + "\n"

            sir[i + 1], sir[u - 1] = sir[u - 1], sir[i + 1]
        else:
            data = random.sample(range(100), random.randint(5, 9))  # din numerele mai mici decat 100, alegem intre 5 si 9
            pivot = random.choice(data)
            data = [data, pivot]  # in data retin vectorul si valoarea pivotului
            statement = "11. Partitionati Lomuto urmatorul vector: " + str(data[0]) + " folosind pivotul: " + str(pivot) + "\n"


        super().__init__(statement, data)

    def solve(self):
        solution ="Idee de rezolvare:\n"
        solution += "Partitionarea Lomuto are ca scop alegerea unui element dintr-un vector de numere, care se va numi\n"
        solution += "pivot si modificarea pozitiilor elementelor din vector astfel incat, la finalul algoritmului,\n"
        solution += "elementele cu valoare mai mica decat pivotul se vor afla la stanga sa, iar cele mai mari decat\n"
        solution += "pivotul, in dreapta acestuia, pivotul ajungand pe pozitia in care ar sta daca am sorta vectorul.\n"

        data = self.data
        sir = data[0]  # retin sirul generat din numere la intamplare in sir
        u = len(sir)  # lungimea sirului, in cazul nostru este len(sir)
        i = -1
        p = 0
        piv = data[1]  #valoare pivotului
        pozitie = sir.index(piv)
        sir[pozitie], sir[u - 1] = sir[u - 1], sir[pozitie]
        solution += "\n"
        for j in range(p, u):
            if sir[j] < piv:
                i = i + 1  # daca valoarea elementului este mai mica decat cea a pivotului, crestem valoarea indexului i
                solution += "Interschimbam " + str(sir[j]) + " cu " + str(sir[i]) + " iar i devine " + str(i) + "\n"
                sir[i], sir[j] = sir[j], sir[i]
                solution += "Sirul devine:" + str(sir) + '\n'
                solution += "\n"

        solution +="Trecem la urmatorul element din sir.\n"

        sir[i + 1], sir[u - 1] = sir[u - 1], sir[i + 1]  # adresa i+1 este adresa corecta a pivotului, deci interschimbam cele doua elemente
        solution += "Am ajuns la capatul sirului. In final, avem vectorul partitionat: " + str(sir)
        return solution





