from problem import Problem
import random


class Problem8(Problem):
    def __init__(self):
        self.randA = random.randint(1, 4)
        self.randB = random.randint(1, 4)
        self.randC = random.randint(1, 4)
        self.randD = random.randint(2, 4)
        #self.randA = 2
        #self.randB = 3
        #self.randC = 3
        #self.randD = 2
        #data = [8, 2, 7, 4, 5, 13, 9, 1, 17]
        data = random.sample(range(100), random.randint(5, 9))
        statement = f'8. Primiti sirul: {data}. '

        statement += 'Rezolvati urmatoarele cerinte:\n'
        statement += f'\t- aplicati {self.randA} pasi din alg. de sort. prin insertie urmat de {self.randB} pasi din alg. de sort. prin metoda bulelor;\n'
        statement += f'\t- aplicati {self.randC} pasi din alg. de sort. prin selectia maximului urmat de {self.randD} pasi din alg. de sort. prin selectia minimului\n'
        statement += '\t- ce elemente ar putea fi considerate pivoti a.i. la finalul unei partitionari a alg. Quicksort sa avem primele 3 elemente sortate si specificati partitionarea folosita (Hoare/Lomuto/etc.)\n'
        statement += '\t- exemplificati sortarea sirului folosind Insertion Sort si Selection Sort (Minim)\n'

        super().__init__(statement, data)

    def insertionAndBubbleSort(self, v, n):
        solution = '============================= \n\n'

        # selection sort
        solution += f'a) - Aplicam {self.randA} pasi din Insertion Sort vectorului {v}: \n'
        for i in range(1, self.randA + 1):
            j = i
            solution += f'\t pasul {j}: \n'
            solution += f'\t cat timp j > 0:\n'
            while j:
                if v[j] < v[j - 1]:
                    solution += f'\t\t > Interschimbam {v[j]} cu {v[j - 1]} \n'
                    v[j], v[j - 1] = v[j - 1], v[j]
                    solution += f'\t\t\t vectorul devine {v} \n'
                    j = j - 1
                else:
                    break

        solution += f'\t Dupa Selection Sort, vectorul devine: {v} \n\n'
        solution += f' - Aplicam {self.randB} pasi din Bubble Sort vectorului {v}: \n'

        # bubble sort
        change = True
        j = 0
        while change == True:
            change = False
            solution += f'\t pasul {j + 1}: \n'
            for i in range(0, n - 1):
                if v[i] > v[i + 1]:
                    solution += f'\t\t > Interschimbam {v[j]} cu {v[j - 1]} \n'
                    v[i], v[i + 1] = v[i + 1], v[i]
                    solution += f'\t\t\t vectorul devine {v} \n\n'
                    change = True
            j = j + 1
            if j == self.randB:
                break

        solution += f'\t Dupa Bubble Sort, vectorul devine: {v} \n\n'

        solution += f'Rezultat: {v}'
        solution += '\n\n'
        return solution

    def maxAndMinSelectionSort(self, v, n):
        solution = '============================= \n\n'

        # selection sort
        solution += f'b) - Aplicam {self.randC} pasi din Maximum Selection Sort vectorului {v}: \n'
        for i in range(n - 1, n - self.randC - 1, -1):
            solution += f'\t pasul {n - i}: \n'
            maxIndex = i;
            maximum = v[i]
            solution += f'\t\t > presupunem ca elementul situat pe pozitia {i} este maxim\n'
            solution += f'\t\t > cautam maximul pe intervalul [0, {i}], de la dreapta la stanga, din vectorul {v}\n'
            for j in range(i, 0, -1):
                if (maximum < v[j]):
                    solution += f'\t\t\t {maximum} este mai mic decat {v[j]}\n'
                    maximum = v[j]
                    maxIndex = j
            solution += f'\t\t > maximul gasit este {v[maxIndex]}\n'
            solution += f'\t\t > interschimbam elementul de pe pozitia {maxIndex} cu elementul de pe pozitia {i}\n'
            solution += f'\t\t > vectorul devine {v}\n'
            v[maxIndex], v[i] = v[i], v[maxIndex]

        solution += f'- Aplicam {self.randD} pasi din Minimum Selection Sort vectorului {v}: \n'
        for i in range(0, self.randD + 1):
            solution += f'\t pasul {i + 1}: \n'
            minIndex = i
            minimum = v[i]
            solution += f'\t\t > presupunem ca elementul situat pe pozitia {i} este minim\n'
            solution += f'\t\t > cautam minimul pe intervalul [{i}, n], de la stanga la dreapta, din vectorul {v}\n'
            for j in range(i, n):
                if (minimum > v[j]):
                    solution += f'\t\t\t > {minimum} este mai mare decat {v[j]}\n'
                    minimum = v[j]
                    minIndex = j
                    solution += f'\t\t\t\t indicele minimului devine {minIndex}\n'
            solution += f'\t\t > minimul gasit este {v[minIndex]}, aflat pe pozitia {minIndex}\n'
            solution += f'\t\t > interschimbam elementul de pe pozitia {minIndex} cu elementul de pe pozitia {i}\n'
            v[minIndex], v[i] = v[i], v[minIndex]
            solution += f'\t\t > vectorul devine {v}\n'

        solution += f'Rezultat: {v}'
        solution += '\n\n'
        return solution

    def InsertionSort(self, v, n):
        solution = '============================= \n\n'
        solution += 'd)exemplific Insertion Sort\n'
        # insertion sort
        for i in range(1, n):
            j = i
            solution += f'\t pasul {j}: \n'
            while j:
                if v[j] < v[j - 1]:
                    solution += f'\t\t* vectorul curent: {v}\n'
                    solution += f'\t\t > Interschimbam {v[j]} cu {v[j - 1]} \n'
                    v[j], v[j - 1] = v[j - 1], v[j]
                    solution += f'\t\t\t vectorul devine {v} \n'
                    j = j - 1
                else:
                    break
        solution += f'\t Dupa Selection Sort, vectorul este sortat : {v} \n\n'
        return solution

    def SelectionSort_min(self, v, n):
        solution = 'Exemplific Selection Sort (minim)\n'
        for i in range(0, n):
            solution += f'\t pasul {i + 1}: \n'
            minIndex = i
            minimum = v[i]
            solution += f'\t\t > presupunem ca elementul situat pe pozitia {i} este minim\n'
            solution += f'\t\t > cautam minimul pe intervalul [{i}, n], de la stanga la dreapta, din vectorul {v}\n'
            for j in range(i, n):
                if (minimum > v[j]):
                    solution += f'\t\t\t > {minimum} este mai mare decat {v[j]}\n'
                    minimum = v[j]
                    minIndex = j
                    solution += f'\t\t\t\t indicele minimului devine {minIndex}\n'
            solution += f'\t\t > minimul gasit este {v[minIndex]}, aflat pe pozitia {minIndex}\n'
            solution += f'\t\t > interschimbam elementul de pe pozitia {minIndex} cu elementul de pe pozitia {i}\n'
            v[minIndex], v[i] = v[i], v[minIndex]
            solution += f'\t\t > vectorul devine {v}\n'
        solution += f'Vectorul este sortat : {v}'
        solution += '\n'
        return solution

    def quickHoare(self, v, p, n):
        pivot = v[p]
        solution = f'\t Aleg {pivot} drept pivot\n'
        begin = 0
        end = n - 1
        while begin <= end:
            while v[begin] < pivot:
                begin += 1
            while v[end] > pivot:
                end -= 1
            if begin <= end:
                v[begin], v[end] = v[end], v[begin]
                begin += 1
                end -= 1
        solution += f'\tDupa pivotare vectorul devine: {v}\n'
        return solution

    def Pivotare(self, v, n):
        solution = '========================\n\n'
        solution += f'c) Aplic partitionare Hoare punand fiecare element al vectorului ca pivot\n '
        for i in range(0, n):
            v = self.data[:]
            solution += self.quickHoare(v, i, n)
            solution+=f'\t\tVerific daca primele {self.randD} elemente sunt sortate\n'
            for j in range(0, self.randD - 1):
                if v[j] > v[j + 1]:
                    solution += f'\t\t *Nu-l putem folosi drept pivot\n'
                    break
                solution += f'\t\t*Putem sa-l folosi drept pivot\n'
        solution += '\n\n'
        return solution

    def solve(self):
        v = self.data[:]
        n = len(v)
        solution = ''

        solution += self.insertionAndBubbleSort(v, n)
        v = self.data[:]
        solution += self.maxAndMinSelectionSort(v, n)
        v = self.data[:]
        solution += self.Pivotare(v, n)
        v = self.data[:]
        solution += self.InsertionSort(v, n)
        v = self.data[:]
        solution += self.SelectionSort_min(v, n)
        return solution


p = Problem8()
print(p.statement)
print(p.solve())
