from problem import Problem
import random


def vrvz(vr, n):  # verific daca exista macar vreun fiu nevizitat
    for i in range(n):
        if vr[i] == 0:
            return 1
    return 0


COUNT = [10]
afis = ""


def afisare(k, space, fii, n):
    global afis
    space += COUNT[0]

    nr_fii = 0
    for p in range(n):
        if fii[k][p]:
            nr_fii = nr_fii + 1

    if nr_fii == 0 or nr_fii > 1:
        for j in range(int(n/2)):
            if fii[k][j]:
                afisare(j, space, fii, n)

        afis += '\n'
        for m in range(COUNT[0], space):
            afis += " "
        afis += str(k) + '\n'

        for l in range(int(n/2), n):
            if fii[k][l]:
                afisare(l, space, fii, n)
    else:
        if nr_fii == 1:
            for a in range(n):
                if fii[k][a]:
                    fiu = a
                    fii[k][a] = 0
            afis += '\n'
            for m in range(COUNT[0], space):
                afis += " "
            afis += str(k)
            afisare(fiu, space, fii, n)


class Problem12(Problem):
    def __init__(self):
        statement = "Problema 12:\n"

        n = random.randrange(8, 13)

        v = [0] * n  # vector de vizite
        v2 = [0] * n  # vector de tati
        v1 = [0] * n  # vector de verificare pentru tati in crearea lui v2

        radin = random.randrange(0, n - 1)
        k1 = n
        k1 = k1 - 1
        t = 0
        for i in range(0, n):
            v1[i] = -2
        for i in range(0, n):
            v2[i] = -2
        v2[radin] = 100
        # in acest while se umple random vectorul de tati
        while k1 and (t < 30):
            t = t + 1
            nivel = random.randint(1, 4)
            if nivel > k1:
                nivel = random.randint(0, k1)
            for i in range(0, n):
                if (v2[i] != -2) and (v1[i] == -2):
                    r = i
                    v1[i] = 1
                    break
            i = random.randint(0, n - 1)
            while nivel != 0:
                while v2[i] != -2 and k1 != 0:
                    i = random.randint(0, n - 1)
                v2[i] = r
                nivel = nivel - 1
                k1 = k1 - 1

        v2[radin] = -1

        r = radin
        data = []
        # in acest while fac DF continuu

        t = 0
        while vrvz(v, n) and (t < 30):
            t = t + 1
            ok = 0
            data.append(r)
            v[r] = 1
            for i in range(0, n):
                if (v[i] == 0) and (v2[i] == r):
                    r = i
                    ok = 1
                    break

            if not ok:
                r = v2[r]

        t = 0

        while (v2[r] != radin) and (v2[r] != -1):
            t = t + 1
            data.append(r)
            r = v2[r]
            if t > 30:
                break

        data.append(r)
        if r != radin:
            data.append(radin)

        statement += "Reconstruiti un arbore oarecare, primind urmatoarea parcurgere continua in adancime a arborelui, pornind din radacina: " + ', '.join(map(str, data)) + "\n"
        data = [data, n]
        super().__init__(statement, data)

    def solve(self):
        solution = '12. Solutia problemei: \n'
        data = self.data

        n = data[1]
        data.pop(1)
        data = data[0].copy()
        print(data)

        tata = [-1] * n
        fii = [[0 for x in range(n)] for y in range(n)]
        i = 1
        rad = data[0]
        while i < len(data):
            if tata[data[i]] == -1 and data[i] != rad:
                tata[data[i]] = data[i - 1]  # la afisare tatal lui data[i] este data[i-1]
                fii[data[i - 1]][data[i]] = 1
                i = i + 1
            else:
                if tata[data[i]] != -1:
                    while tata[data[i]] != -1:
                        i = i + 1
                        if data[i] == rad:
                            i = i + 1
                        if i >= len(data):
                            break
                else:
                    i = i + 1

        for i in range(n):
            if tata[i] == -1:
                afisare(i, 0, fii, n)
                solution += afis
                break
        print(afis)
        solution += "Vectorul de tati: " + str(tata)  # in loc de vectorul tata trebuie afisat arborele
        return solution
