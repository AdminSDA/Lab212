from problem import Problem
import random


class Problem11(Problem):
    def __init__(self):

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
        solution +="\nParcurgem sirul de la primul la ultimul element si comparam valoarea pivotului cu valoarea\n"
        solution +="elementului curent. Cand gasim un element mai mic decat pivotul, il interschimbam cu elementul\n"
        solution +="de pe pozitia i (initial -1), i fiind numarul de elemente mai mici decat pivotul in momentul respectiv\n"
        solution +="La final, i+1 va reprezenta pozitia pe care trebuie dus pivotul\n\n"
        solution +="Incepem partitionarea:\n"
        for j in range(p, u):
            solution += "Este " + str(sir[j]) + " mai mic decat " + str(piv) + "?\n"
            if sir[j] < piv:
                solution += "DA\n"
                i =  i + 1  # daca valoarea elementului este mai mica decat cea a pivotului, crestem valoarea indexului i
                solution += "Interschimbam " + str(sir[j]) + " cu " + str(sir[i]) + " iar i devine " + str(i) + "\n"
                sir[i], sir[j] = sir[j], sir[i]
                solution += "Sirul devine:" + str(sir) + '\n'
            else:
                solution +="NU\n"
            solution +="Este " + str(sir[j]) + " egal cu " + str(piv) + "?\n"
            if sir[j] == piv: # daca am ajuns pe pozitia actuala a pivotului
                solution +="DA\n"
                indexpiv = j # o vom retine pentru a putea, la finalul algoritmului, sa il mutam in pozitia corecta
                solution +="Retinem pozitia pivotului\n"
            if sir[j] > piv:
                solution +="NU\n"
        solution +="Trecem la urmatorul element din sir.\n"

        sir[i + 1], sir[indexpiv] = sir[indexpiv], sir[i + 1]  # adresa i+1 este adresa corecta a pivotului, deci interschimbam cele doua elemente
        solution += "Am ajuns la capatul sirului. In final, avem vectorul partitionat: " + str(sir)
        return solution