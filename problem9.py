from problem import Problem
import random


class Problem9(Problem):
    def __init__(self):
        data = random.sample(range(100), random.randint(5, 9))

        statement = 'Problema 9: Se primesc numerele: ' + ', '.join(map(str, data)) + '.\n'
        statement += 'Verificati daca:\n'

        # alegem pivotul si pasii de selection (maxim) si insertion
        pivot = random.choice(data)
        pasi_selection = random.randint(2, len(data) - 1)
        pasi_insertion = random.randint(2, len(data) - 1)

        data = [data, pivot]

        data = [data, pasi_selection]
        statement += '1. Vectorul a rezultat in urma aplicarii a ' + str(pasi_selection) + ' pasi din Selection Sort (Maxim).\n'

        data = [data, pasi_insertion]
        statement += '2. Vectorul a rezultat in urma aplicarii a ' + str(pasi_insertion) + ' pasi din Insertion Sort.\n'

        statement += '3. Vectorul a rezultat in urma unei partitionari folosind pivotul ' + str(pivot) + '.\n'

        statement += 'Exemplificati sortarea sirului folosind Bubble Sort si Selection Sort (Maxim).\n'
        super().__init__(statement, data)

    def solve(self):
        solution = '9. Solutia problemei: \n'
        data = self.data

        # scoatem pivotul si variabilele pentru pasi din vector
        pasi_insertion = data[1]
        data.pop(1)
        data = data[0].copy()

        pasi_selection = data[1]
        data.pop(1)
        data = data[0].copy()

        pivot = data[1]
        data.pop(1)
        data = data[0].copy()
        data2 = data.copy()  # salvam o copie a vectorului pentru a il sorta de 2 ori

        # verificare selection sort (maxim)
        ok = 1
        n = pasi_selection
        solution += 'Trebuie sa aflam daca este adevarat sau fals ca vectorul ' + str(data) + ' rezulta din ' + str(n) + ' pasi de Selection Sort (Maxim) : \n'
        solution += 'Pentru asta trebuie sa verificam daca primele ' + str(n) + ' elemente sunt in ordine descrescatoare \n'
        for i in range(0, n):
            if data2[i + 1] > data2[i]:
                solution += str(data2[i + 1]) + ' > ' + str(data2[i]) + ' => Afirmatia este falsa \n'
                ok = 0
                break
            else:
                solution += str(data2[i + 1]) + ' < ' + str(data2[i]) + '\n'
        if ok == 1:
            solution += '(ADEVARAT) Vectorul a rezultat in urma aplicarii a ' + str(n) + ' pasi din Selection Sort (Maxim)\n\n'
        else:
            solution += '(FALS) Vectorul nu a rezultat in urma aplicarii a ' + str(n) + ' pasi din Selection Sort (Maxim)\n\n'

        # verificare insertion sort
        ok = 1
        n = pasi_insertion
        solution += 'Trebuie sa aflam daca este adevarat sau fals ca vectorul ' + str(data) + ' rezulta din ' + str(n) + ' pasi de Insertion Sort : \n'
        solution += 'Pentru asta trebuie sa verificam daca primele ' + str(n) + ' elemente sunt deja sortate in ordine crescatoare \n'
        for i in range(1, n):
            if data2[i] < data2[i - 1]:
                ok = 0
                solution += str(data2[i]) + ' < ' + str(data2[i - 1]) + ' => Afirmatia este falsa \n'
                break
            else:
                solution += str(data2[i]) + ' > ' + str(data2[i - 1]) + '\n'
        if ok == 1:
            solution += '(ADEVARAT) Vectorul a rezultat in urma aplicarii a ' + str(n) + ' pasi din Insertion Sort \n\n'
        else:
            solution += '(FALS) Vectorul nu a rezultat in urma aplicarii a ' + str(n) + ' pasi din Insertion Sort \n\n'

        # verificare pivot
        n = len(data2)
        solution += 'Verificam partitionarea pentru Quicksort cu pivotul ' + str(pivot) + '. Vectorul ' + str(data2) + ' are ' + str(n) + ' elemente \n'
        ok1 = 1
        ok2 = 1
        solution += 'Pentru a verifica daca vectorul este partitionat in functie de un anumit pivot vom face urmatoarele: \n'
        for i in range(0, n):
            if data2[i] == pivot:
                poz_pivot = i
                solution += 'Identificam ca pivotul se afla pe pozitia ' + str(i + 1) + '\n'
        solution += 'Verificam daca elementele care se afla la stanga pivotului sunt mai mici decat acesta \n'
        for i in range(0, poz_pivot):
            if data2[i] > pivot:
                ok1 = 0
                solution += str(data2[i]) + ' >= ' + str(pivot) + ' => Afirmatia este falsa \n'
                break
            else:
                solution += str(data2[i]) + ' <= ' + str(pivot) + '\n'
        solution += 'Verificam daca elementele care se afla la dreapta pivotului sunt mai mari decat acesta \n'
        for j in range(poz_pivot + 1, n):
            if data2[j] < pivot:
                ok2 = 0
                solution += str(data2[j]) + ' <= ' + str(pivot) + ' => Afirmatia este falsa \n'
                break
            else:
                solution += str(data2[j]) + ' >= ' + str(pivot) + '\n'
        if ok1 == 1 and ok2 == 1:
            solution += '(ADEVARAT) Vectorul a rezultat in urma unei partirionari folosind pivotul ' + str(pivot) + '\n\n'
        else:
            solution += '(FALS) Vectorul nu a rezultat in urma unei partitionari folosind pivotul ' + str(pivot) + '\n\n'

        # bubble sort
        solution += 'Vom exemplifica modalitatea de functionare a Bubble sort-ului: \n'
        solution += 'Aflam dimensiunea vectorului ' + str(data) + ' pe care vom aplica algoritmul \n'
        n = len(data)
        solution += 'Vectorul nostru are ' + str(n) + ' elemente \n'
        solution += 'Vom folosi o variabila booleana pentru a verifica daca am facut interschimbari \n'
        reverse = True
        solution += 'Cat timp vom face interschimbari iar variabila bool va fi adevarata, algoritmul nu se termina iar vectorul nu este complet sortat \n'
        while reverse == True:
            reverse = False
            solution += 'Vom parcurge vectorul \n'
            for i in range(0, n - 1):
                if data[i + 1] < data[i]:
                    data[i], data[i + 1] = data[i + 1], data[i]
                    solution += str(data[i + 1]) + ' < ' + str(data[i]) + ' => elementele nu sunt sortate asa ca vom face o interschimbare \n'
                    reverse = True
        solution += 'Daca nu s-a mai facut nicio interschimbare la pasul anterior, atunci vectorul este sortat si il afisam: ' + str(data) + '\n\n'

        # selection sort (maxim)
        solution += 'Vom exemplifica modalitatea de functionare a Selection Sort(Maxim): \n'
        solution += 'Aflam dimensiunea vectorului ' + str(data2) + ' pe care vom aplica algoritmul \n'
        n = len(data2)
        solution += 'Vectorul nostru are ' + str(n) + ' elemente \n'
        solution += 'Vom parcurge vectorul nesortat pentru a gasi elementul maxim si vom face o interschimbare astfel incat vom avea vectorul partitionat in 2: partea ordonata descrescator la stanga si cea neordonata la dreapta \n'
        for i in range(0, n):
            poz_max = i
            elem_max = data2[i]
            solution += 'Selectam elementul de pe pozitia ' + str(i + 1) + ' si consideram ca elementul ' + str(elem_max)+ ' este maxim \n'
            solution += 'Vom parcurge vectorul la dreapta elementului maxim \n'
            for j in range(i, n):
                if data2[j] > elem_max:
                    solution += str(data2[j]) + ' > ' + str(elem_max) + ' => am gasit un element mai mare decat cel maxim in partitia neordonata a vectorului asa ca salvam elementul ca fiind noul maxim \n'
                    elem_max = data2[j]
                    poz_max = j
            data2[i], data2[poz_max] = data2[poz_max], data2[i]
            if i != poz_max:
                solution += 'Interschimbam elementele ' + str(data2[i]) + ' si ' + str(data2[poz_max]) + '\n'
        solution += 'Dupa ce terminam parcurgerea intregului vector si am terminat sortarea, il afisam: ' + str(data2) + '\n \n'

        return solution
