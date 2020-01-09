from problem import Problem
import random


class Problem40(Problem):
    def __init__(self):
        data = [random.sample(range(3, 20), 10)]
        for i in range(1, 5):
            v = data[0].copy()
            z = random.randint(1, 9)
            y = random.randint(1, 9)
            v[z], v[y] = v[y], v[z]
            data.append(v)
        h = [None for i in range(0, 12)]
        x = [i for i in range(1, 13)]
        for i in data[0]:
            k = 0
            while h[(i+k) % len(h)] != None:
                k = k + 1
            h[(i+k) % len(h)] = i
        random.shuffle(data)
        data.append(h)
        statement = "Primiti urmatorul hash, carea a fost creat folosind adresarea directa - liniara:\n"
        for i in range(1, 13):
            statement += str(i) + "    "
        statement += "\n"
        for i in h:
            statement += str(i) + "   "
        statement += "\n • in ce ordine ar fi putut fi inserate elementele intr-un hash:"
        statement += "\nA)" + str(data[0])
        statement += "\nB)" + str(data[1])
        statement += "\nC)" + str(data[2])
        statement += "\nD)" + str(data[3])
        statement += "\nE)" + str(data[4])
        statement += "\n • stergeti elementul "
        t = random.choice(data[5])
        while t is None:
            t = random.choice(data[5])
        statement += str(t) + " din hash."
        data.append(t)
        print(data[6])

        super().__init__(statement, data)

    def solve(self):
        solution = "Ideea de rezolvare:"
        solution += "\nSe primeste un hash si se testeaza o secventa de liste, astfel incat ordinea"
        solution += "\nin care ar fi putut fi inserate elemntele in hash sa poata genera o lista identica cu hash-ul."
        solution += "\nPrin adresare elementele sunt puse intr-un tablou alocat static pe pozitiile cheilor lor, astfel incat"
        solution += "\nun element cu cheia k va fi memorat in locatia k."
        
        v = self.data[5]
        h = [None for i in range(0, 12)]
        for i in range(0, 4):
            h = [None for t in range(0, 12)]
            for j in self.data[i]:
                k = 0
                while h[(j+k) % len(h)] != None:
                    k = k + 1
                h[(j+k) % len(h)] = j
            if v == h:
                solution += "\nRezultat:" + str(self.data[i])
                break
        print(self.data[-1])
        v.remove(self.data[-1])
        print(v)
        return solution

p = Problem40()
print(p)
print(p.solve())


