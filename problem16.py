
from problem import Problem
import random


class Problem16(Problem):
    def __init__(self):
        data = [random.randint(0, 5) for i in range(10)]
        x = random.choice(data)
        data = [data, x]
        statement = "Partitionati urmatorul vector, folosind pivotul " + str(data[1]) + " "
        statement += "si partitionarea de la QS pe care o folosim cand avem multe duplicate: "
        statement += str(data[0])
        statement += "\nScrieti numarul de interschimbari."
        super().__init__(statement, data)

    def partition(self, v, left, right, Ipiv):
        # v - vector
        # left, right - capetele
        # Ipiv - indexul pivotului
        v[Ipiv], v[right] = v[right], v[Ipiv]  # punem pivotul ultimul;
        Ipiv = right
        nr = 0;
        # vom exclude toate elementele egale cu pivotul de la capatul sirului

        i = -1  # pleaca de la incepu1
        p = right; # pozitia elementelor egale cu pivotul
        # j pleaca de la sfarsit
        # print(v);
        for j in range(left, right + 1):
            while (v[j] == v[p]):
                if (j < p):
                    p-=1;
                    v[j], v[p] = v[p], v[j];
                    nr+=1;

                else:
                    break
            if (v[j] < v[Ipiv]):
                i += 1
                v[i], v[j] = v[j], v[i];
                nr+=1;
            # print(j)
            # print(v);
        # i se opreste la ultimul element mai mic decat pivotul
    
        # acum mutam pivotul si toate elementele...
        print("");
        j = i+1;
        while(p<=right):
            v[j], v[p] = v[p], v[j];
            j+=1;
            p+=1;
            # print(v)
        self.nr = nr;
        return i + 1  # pozitia pivotului

    def verificare(self, v, Ipiv):
        for i in range(0, Ipiv):
            if v[i] > v[Ipiv]:
                print("aiurea")
                return
        for i in range(Ipiv, len(v) - 1):
            if (v[i] < v[Ipiv]):
                print("aiurea")
                return

    def solve(self):
        solution = "<br><br>Idee de rezolvare:<br><br>"
        solution += "Initial, avem vectorul v, indexul pivotului Ipiv si capetele vectorului: left si right."
        solution += "Primul pas este sa punem pivotul pe ultima pozitie prin interschimbare si "
        solution += "sa se initieze numarul interschimbarilor cu 0."
        solution += "Parcurgem vectorul de la stanga la dreapta si cat timp valoarea elementului de pe pozitia j este egala cu valoarea pivotului, "
        solution += "testam daca pozitia j este mai mica decat capatul din dreapta al vectorului, daca da, "
        solution += "scad valoarea indicelui capatului de interval cu 1, interschimb valoarea curenta cu "
        solution += "valoarea noului capat de interval cu indicele decrementat mai sus si valoarea lui nr "
        solution += "se incrementeaza cu 1. "
        solution += "Daca pozitia j este mai mare decat capatul din dreapta al vectorului, se trece la "
        solution += "urmatorul element din vector dupa ce se testeaza pasul urmator. "
        solution += "Testam daca valoarea curenta este mai mica decat cea a pivotului si daca da se "
        solution += "interschimba valoarea curenta cu valoarea indicelui i+1, astfel toate numerele mai "
        solution += "mici decat pivotul sunt plasate la inceputul vectorului."
        solution += "Valoarea i se opreste la ultimul element mai mic sau egal decat pivotul si mutam "
        solution += "pivotul dupa valoarea din sir cu indicele i."
        solution += "Se parcurge sirul si se muta elementele mai mici sau egale cu pivotul inaintea "
        solution += "pivotului si cele mai mari dupa el."
        solution += "Se muta elementele la inceputul vectorului pana la pozitia i+1. <br><br>"
        solution += "<br><br>Secventa finala este: "



        # print(self.data)
        v = self.data[0]
        Ipiv = v.index(self.data[1])
        self.nr = 0;
        Ipiv = self.partition(v, 0, len(v) - 1, Ipiv)
        self.verificare(v, Ipiv)
        for i in range(len(v)):
              y =  str(v[i])
              solution += y +" "
        solution +="<br><br> Numarul de interschimbari este:"
        solution +=str(self.nr)
        return solution

