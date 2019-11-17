from problem import Problem
import random


class Problem9(Problem):
    def __init__(self):
        pasi_selection = random.randint(2, 4)
        pasi_insertion = random.randint(2, 4)
        data = random.sample(range(100), random.randint(6, 10))
        x = random.randint(0, 2)

        # 33% din cazuri ne asiguram ca prima cerinta e adevarata
        reverse = True
        if x == 2:
            while reverse:
                reverse = False
                for i in range(0, pasi_selection):
                    if data[i + 1] > data[i]:
                        data[i], data[i + 1] = data[i + 1], data[i]
                        reverse = True
        # 33% din cazuri ne asiguram ca a doua cerinta e adevarata
        if x == 1:
            while reverse:
                reverse = False
                for i in range(0, pasi_insertion):
                    if data[i - 1] > data[i]:
                        data[i], data[i - 1] = data[i - 1], data[i]
                        reverse = True

        # incercam sa alegem un pivot bun
        n = len(data)
        for k in range(0, n):
            ok1 = 1
            ok2 = 1
            pivot = data[k]
            poz_pivot = k
            for i in range(0, poz_pivot):
                if data[i] > pivot:
                    ok1 = 0
                    break
            for j in range(poz_pivot + 1, n):
                if data[j] < pivot:
                    ok2 = 0
                    break
            if ok1 == 1 and ok2 == 1:
                break
            else:
                pivot = -1

        if pivot == -1:
            pivot = random.choice(data)

        statement = 'Problema 9: Se primesc numerele: ' + ', '.join(map(str, data)) + '.\n'
        statement += 'Raspundeti cu adevarat sau fals:\n'
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
        solution += '1. A/F ca ' + str(data) + ' rezulta din ' + str(n) + ' pasi de Selection Sort (Maxim) : \n'
        for i in range(0, n):
            if data2[i + 1] > data2[i]:
                solution += str(data2[i + 1]) + ' > ' + str(data2[i]) + ' => (FALS) \n\n'
                ok = 0
                break
            else:
                solution += str(data2[i + 1]) + ' < ' + str(data2[i]) + '\n'
        if ok == 1:
            solution += '(ADEVARAT)\n\n'

        # verificare insertion sort
        ok = 1
        n = pasi_insertion
        solution += ' 2. A/F ca ' + str(data) + ' rezulta din ' + str(n) + ' pasi de Insertion Sort : \n'
        for i in range(1, n):
            if data2[i] < data2[i - 1]:
                ok = 0
                solution += str(data2[i]) + ' < ' + str(data2[i - 1]) + ' => (FALS) \n\n'
                break
            else:
                solution += str(data2[i]) + ' > ' + str(data2[i - 1]) + '\n'
        if ok == 1:
            solution += '(ADEVARAT) \n\n'

        # verificare pivot
        n = len(data2)
        solution += '3. A/F partitionat pentru Quicksort cu pivotul ' + str(pivot) + ' \n'
        ok1 = 1
        ok2 = 1
        for i in range(0, n):
            if data2[i] == pivot:
                poz_pivot = i
                solution += 'i. Pozitia pivotului = ' + str(i + 1) + '\n'
        solution += 'ii. Vf. elementele de la stanga sunt mai mici \n'
        for i in range(0, poz_pivot):
            if data2[i] > pivot:
                ok1 = 0
                solution += str(data2[i]) + ' >= ' + str(pivot) + ' => (FALS) \n\n'
                break
            else:
                solution += str(data2[i]) + ' <= ' + str(pivot) + '\n'
        solution += 'iii. Vf elementele de la dreapta mai mari\n'
        for j in range(poz_pivot + 1, n):
            if data2[j] < pivot:
                ok2 = 0
                solution += str(data2[j]) + ' <= ' + str(pivot) + ' => (FALS) \n\n'
                break
            else:
                solution += str(data2[j]) + ' >= ' + str(pivot) + '\n'
        if ok1 == 1 and ok2 == 1:
            solution += '(ADEVARAT)\n\n'

        # bubble sort
        solution += '4. Exemplificam Bubble sort: \n'
        n = len(data)
        solution += 'i.Vectorul are ' + str(n) + ' elemente \n'
        reverse = True
        solution += 'ii.Cat timp facem interschimbari = > nu am terminat \n'
        k = 0
        while reverse == True:
            solution += str(k) + ': ' + str(data) + '\n'
            k = k + 1
            reverse = False
            for i in range(0, n - 1):
                if data[i + 1] < data[i]:
                    data[i], data[i + 1] = data[i + 1], data[i]
                    reverse = True
        solution += '\n'

        # selection sort (maxim)
        solution += '5.Exemplificam Selection Sort(Maxim): \n'
        n = len(data2)
        solution += 'i.Vectorul are ' + str(n) + ' elemente \n'
        k = 0
        for i in range(0, n):
            solution += str(k) + ': ' + str(data2) + '\n'
            k = k + 1
            poz_max = i
            elem_max = data2[i]
            for j in range(i, n):
                if data2[j] > elem_max:
                    elem_max = data2[j]
                    poz_max = j
            data2[i], data2[poz_max] = data2[poz_max], data2[i]
        solution += '\n'

        return solution
