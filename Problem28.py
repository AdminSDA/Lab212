from problem import Problem
import random
import heapq


class Problem28(Problem):
    def __init__(self):
        statement = "Primiti numere naturale > 0 si atunci cand primiti 0,\n"
        statement += "trebuie sa afisati valoarea mediana din vector. \n"
        statement += "Valoarea mediana este v[mij] daca v este sortat si len e impar,\n"
        statement += "altfel e (v[mij1] + v[mij2]) / 2 daca e par.\n"
        n = random.randint(5, 17)
        vect = random.sample(range(1, 20), n)
        vect2 = sorted(vect)
        numof0 = random.randint(1, 5)
        for i in range(numof0):
            vect.insert(random.randint(2, len(vect)-1), 0)
        vect.append(0)
        data = [vect, vect2]

        super().__init__(statement, data)

    def solve(self):
        vect = self.data[0]
        vect2 = self.data[1]
        solution = "Vectorul primit este: " + str(vect) + "\n"
        solution += "Vectorul sortat, fara 0, arata asa: " + str(vect2) + "\n"
        if len(vect2) % 2 == 0:
            valmed = (vect2[int(len(vect2)/2)-1] + vect2[int(len(vect2)/2)]) / 2
        else:
            valmed = vect2[int(len(vect2)/2)]
        solution += "Valoarea mediana trebuie sa fie: " + str(valmed) + "\n\n"

        heap1 = []
        heap2 = []
        mediana = 0
        for num in vect:
            if num == 0:
                if len(heap1) > len(heap2):
                    valm = heap1[0]
                elif len(heap1) < len(heap2):
                    valm = -heap2[0]
                else:
                    nr1 = heap1[0]
                    nr2 = -heap2[0]
                    valm = (nr1 + nr2) / 2
                solution += "min_heap este: " + str(heap1) + "\n"
                solution += "max_heap este: " + str(heap2) + "\n"
                solution += "valoarea mediana este: " + str(valm) + "\n\n"
            else:
                if num > mediana:
                    heapq.heappush(heap1, num)
                else:
                    heapq.heappush(heap2, -num)

                if len(heap1) - len(heap2) > 1:
                    heapq.heappush(heap2, -heapq.heappop(heap1))
                elif len(heap2) - len(heap1) > 1:
                    heapq.heappush(heap1, -heapq.heappop(heap2))

                if len(heap1) > len(heap2):
                    mediana = heap1[0]
                elif len(heap1) < len(heap2):
                    mediana = -heap2[0]
                else:
                    mediana = (heap1[0] + (-heap2[0])) / 2


        return solution