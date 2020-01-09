from problem import Problem
import random


def semn(f):
    n = 0
    s = 0
    for i in range(len(f)):
        if f[i] == '+' or f[i] == '-' or f[i] == '*':
            s += 1
        else:
            n += 1
    if s < n-1:
        return 1
    else:
        return 0


COUNT = [10]
afis = ""


class Nod:
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None


def afisare(root, space):
    global afis
    if root is None:
        return 0

    space += COUNT[0]

    afisare(root.right, space)

    afis += '\n'
    for i in range(COUNT[0], space):
        afis += " "
    afis += str(root.data)

    afisare(root.left, space)


class Problem31(Problem):
    def __init__(self):
        statement = "Problema 31:\n"

        data = []  # forma postfixata
        nr = random.randint(4, 8)  # nr. de operanzi (frunze)
        s = nr - 1  # nr. de operatii (noduri interne)
        semne = ['+', '-', '*']
        data.append(random.randrange(1, 10))
        data.append(random.randrange(1, 10))
        while data[0] == data[1]:
            data[1] = random.randrange(1, 10)
        nr = nr - 2  # primele doua elemente trebuie sa fie numere
        numere = random.sample(range(1, 10), nr)
        elemente = semne + numere

        while nr > 0 or s > 1:
            if nr > 0 and s > 1:
                data.append(random.choice(elemente))
                if data[-1] == '+' or data[-1] == '-' or data[-1] == '*':
                    s = s - 1
                    if not semn(data):
                        data[-1] = random.randrange(1, 10)
                        s += 1
                        nr -= 1
                else:
                    ok = 0
                    while not ok:
                        ok = 1
                        for i in range(len(data) - 1):
                            if data[i] == data[len(data)-1]:
                                data[len(data) - 1] = random.randrange(1, 10)
                                ok = 0
                    nr = nr - 1
                continue

            if nr > 0:
                data.append(random.choice(numere))
                nr = nr - 1
            if s > 1:
                data.append(random.choice(semne))
                s = s - 1

        data.append(random.choice(semne))  # ultimul element trebuie sa fie un semn

        statement += "Evaluati expresia in forma postfixata si construiti un arbore pentru aceasta expresie: " + ', '.join(map(str, data)) + "\n"
        super().__init__(statement, data)

    def solve(self):
        data = self.data
        solution = '31. Solutia problemei: \n'
        solution += 'Idee de rezolvare: punem numerele din forma postfixata in stiva pana gasim un semn de operatie, apoi scoatem din stiva ultimele doua elemente.\n' \
                    'Primul operand este al doilea numar scos. Facem operatia respectiva si punem rezultatul in stiva.\n' \
                    'Repetam procedeul pana in stiva ramane un singur numar, acela fiind rezultatul expresiei.\n\n'
        noduri = []
        noduri2 = []
        stiva = []
        expr = []  # o folosim pentru expresia matematica
        print(data)
        for elem in data:
            if elem != '+' and elem != '-' and elem != '*':
                noduri.append(Nod(elem))
                noduri2.append(Nod(elem))
                stiva.append(elem)
                expr.append(elem)
                solution += "<table border=1><tr>"
                for el in stiva:
                    solution += "<td>" + str(el) + "</td>"
                solution += "</tr></table>\n"

            else:
                solution += 'Am gasit semnul ' + elem + '\n'
                x = expr.pop()
                y = expr.pop()
                expr.append('(' + str(y) + str(elem) + str(x) + ')')

                x = stiva.pop()
                y = stiva.pop()

                solution += "<table border=1><tr>"
                for el in stiva:
                    solution += "<td>" + str(el) + "</td>"
                solution += "<td><strike>" + str(y) + "<strike></td>"
                solution += "<td><strike>" + str(x) + "<strike></td>"
                solution += "</tr></table>\n"

            if elem == '+':
                solution += 'Scoatem ultimele doua numere si punem in stiva rezultatul adunarii lor'
                r = x + y

                root = Nod(r)
                root2 = Nod(r)

                i = -1
                for node in noduri:
                    i += 1
                    if node.data == x:
                        root.right = node
                        root2.right = noduri2[i]

                j = -1
                for node in noduri:
                    j += 1
                    if node.data == y:
                        root.left = node
                        root2.left = noduri2[j]

                noduri.append(root)
                root2.data = '+'
                noduri2.append(root2)
                stiva.append(r)

            if elem == '-':
                solution += 'Scoatem ultimele doua numere si punem in stiva rezultatul scaderii lor'
                r = y - x

                root = Nod(r)
                root2 = Nod(r)

                i = -1
                for node in noduri:
                    i += 1
                    if node.data == x:
                        root.right = node
                        root2.right = noduri2[i]

                j = -1
                for node in noduri:
                    j += 1
                    if node.data == y:
                        root.left = node
                        root2.left = noduri2[j]

                noduri.append(root)
                root2.data = '-'
                noduri2.append(root2)
                stiva.append(r)

            if elem == '*':
                solution += 'Scoatem ultimele doua numere si punem in stiva rezultatul inmultirii lor'
                r = x * y

                root = Nod(r)
                root2 = Nod(r)

                i = -1
                for node in noduri:
                    i += 1
                    if node.data == x:
                        root.right = node
                        root2.right = noduri2[i]

                j = -1
                for node in noduri:
                    j += 1
                    if node.data == y:
                        root.left = node
                        root2.left = noduri2[j]

                noduri.append(root)
                root2.data = '*'
                noduri2.append(root2)
                stiva.append(r)

                solution += "<table border=1><tr>"
                for el in stiva:
                    solution += "<td>" + str(el) + "</td>"
                solution += "</tr></table>\n"

        r = stiva.pop()
        afisare(root2, 0)
        e = expr.pop()  # in lista expr mai e doar expresia
        e1 = e.replace('(', "", 1)  # sterge prima paranteza
        expresie = e1[:len(e1) - 1]  # sterge ultima paranteza, ia caracterele de la inceputul sirului pana la penultima pozitie
        solution += afis + '\n\n'
        solution += 'Expresia este ' + expresie + '\n'
        solution += "Rezultatul este " + str(r)

        return solution
