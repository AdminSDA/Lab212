from problem import Problem


class Problem3(Problem):
    def __init__(self):

        import random

        statement = '1. Sa se gaseasca o succesiune de mutari astfel incat introducant elementele:  '
        data = list(range(1, random.randint(5, 10)))
        random.shuffle(data)
        statement += str(data)
        statement += " in stiva, la final sa se afiseze: "
        r = random.randint(1, 10)
        i = 0
        stack = []
        stack.append(data[i])
        i += 1
        op = []
        nr = 1
        nrn = 1
        stack_out = []
        if r < 8:  # alegem in cate cazuri formam secventa sau alegem o permutare
            while i + nrn < 2 * len(data) or nr > 0:
                L = random.randint(1, 10)
                if L < 7:  # probabilitatea in care pica n (60%) sau p (40%)
                    if nrn == len(data):
                        op.append('p')
                        stack_out.append(stack.pop())
                        # scoatem ultimul nr din stiva si il punem in alta stiva in cazul in care pica p
                        nr -= 1
                    else:
                        op.append('n')
                        stack.append(data[i])  # baga nr de pe pozitia i din vector, in stiva
                        nr += 1
                        i += 1
                        nrn += 1
                else:
                    if nr == 0:
                        stack.append(data[i])  # baga nr de pe pozitia i din vector, in stiva
                        nr += 1
                        i += 1
                        op.append('n')
                        nrn += 1
                    else:
                        op.append('p')
                        stack_out.append(stack.pop())
                        # scoatem ultimul nr din stiva si il punem in alta stiva in cazul in care pica p
                        nr -= 1
            data = [data, stack_out]
        else:
            stack_out = random.sample(data, len(data))
            data = [data, stack_out]

        statement += str(stack_out)
        statement += "\nPentru rezolvare avem nevoie de operatiile: \n"
        statement += "    'n'-> inserarea numarului in stiva\n"
        statement += "    'p'-> extragerea unui numar din stiva si afisarea\n"

        super().__init__(statement, data)

    def solve(self):
        print('-' * 20)
        a = self.data[0]
        b = self.data[1]
        operatii = ""
        s = []
        stiva = []
        solution = " "
        solution += "Idee de rezolvare: Selectam primul element din vectorul b. " \
                    "Punem elementele din vectorul a in stiva pana gasim un numar egal cu cel selectat din vectorul b.\n" \
                    "Cat timp stiva nu este goala si ultimul element din stiva este egal cu elementul curent din b, " \
                    "scoatem ultimul element din stiva, afisam p si trecem mai departe in b. \n" \
                    "Se repeta procedeul pana cand toate elementele lui a au fost introduse in stiva.\n"
        i = 0
        for lit in a:
            s.append(lit)
            operatii += str(lit)+" "
            solution += "\tAdaugam " + str(lit) + " la operatii si adaugam elementul " + str(lit) + " in stiva\n"
            stiva.append(str(lit))
            solution += "\t<table border=1><tr>"
            for lit in stiva:
                solution += "<td>" + lit + "</td>"
            solution += "</tr></table>\n"

            while len(s) > 0 and s[-1] == b[i]:
                solution += "\tAdaugam p la operatii si scoatem elementul " + str(s[-1]) + " din stiva\n"
                stiva[-1] = "<strike>" + str(s[-1]) + "</strike> "
                solution += "\t<table border=1><tr>"
                for lit in stiva:
                    solution += "<td>" + lit + "</td>"
                solution += "</tr></table>\n"
                operatii += 'p '
                del stiva[-1]
                del s[-1]
                i += 1

        if len(s) > 0:
            operatii = "Nu se poate"
        else:
            solution += 'Operatiile necesare aplicate:\n'
        solution += operatii
        return solution