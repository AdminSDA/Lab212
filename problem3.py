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
                        stack_out.append(
                            stack.pop())  # scoatem ultimul nr din stiva si il punem in alta stiva in cazul in care pica p
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
                        stack_out.append(
                            stack.pop())  # scoatem ultimul nr din stiva si il punem in alta stiva in cazul in care pica p
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


    # def solve(self):
        # a = self.data[0]
        # b = self.data[1]
        # n = len(a)
        # nrp = 0
        # nr = 0
        # i = 0
        # j = 0
        # m = 0
        # operatii = ""
        # s = []  # stiva

        # solution = "Idee de rezolvare: Comparam elementele din vetorul a cu elementul selectat din vectorul b.\n"
        # solution += "Selectam " + str(b[0]) + " primul element din b. Parcurgem a pana gasim un element egal cu " + str(b[0]) + "\n"

        # while j != n:
            # if nr != n:
                # if a[i] != b[j]:
                    # operatii +='n '
                    # solution += a[i] + " este diferit de elementul curent din," + str(b[j]) + ". In stiva introducem numarul " + \
                                # a[i] + "\n"
                    # nr += 1
                    # m += 1
                    # s.append(a[i])
                    # i += 1
            # else:
                # solution += a[i] + " este  egal cu elementul curent din b," + str(b[j]) + ".\n"
                # solution += "Verificam daca am ajuns in capetele lui a, respectiv sfarsitul lui b.\n"
                # if j < n - 1 and i > 0 and i < n - 1:
                    # solution += "Nu trebuie sa fim in capetele lui a, respectiv sfarsitul lui b.\n"
                    # if a[i - 1] != b[j + 1] and a[i + 1] != b[j + 1] and s[-1] != b[j + 1]:
                        # solution += "Elementele dinainte si de dupa " + a[i] + " si ultimul element din stiva," + s[
                            # m] + ",sunt diferite de " + b[j + 1] + ".\n"
                        # solution += "Ne oprim.\n"
                        # operatii = "Nu se poate poate"
                        # j = n
                    # else:
                        # operatii +='n '
                        # nr += 1
                        # operatii +='p '
                        # nrp += 1
                        # j += 1
                        # if s[m] == b[j]:
                            # while len(s) > 0 and s[-1] == b[j]:
                                # operatii +='p '
                                # nrp += 1
                                # j += 1
                                # m -= 1
                        # i += 1
                        
        # print(operatii)
        # return solution   

    def solve(self):
        print('-'*20)
        a=self.data[0]
        b=self.data[1]
        operatii=""
        s = []
        solution=""
        solution += "Idee de rezolvare: Luam fiecare element din vectorul a si il introducem in stiva s.\n"
        solution +="Daca stiva nu este goala si ultimul element din stiva este egal cu elementul de pe pozitia i din b, atunci il scoatem,afisam p si trecem mai departe in b.\n"
        solution+="Cat timp stiva nu e vida si ultimul element din stiva este egal cu elementul curent din b \n"
        i=0
        for lit in a:
            s.append(lit)
            operatii+='n '
            solution+= "\tAdaugam n la operatii si adaugam elementul "+ str(lit) + " in stiva\n"
            
            while len(s)>0 and s[-1] == b[i]:
                solution+="\tAdaugam p la operatii si scoatem elementul " + str(s[-1]) + " din stiva\n"
                operatii+='p '
                del s[-1]
                i+=1
        if len(s)>0:
            operatii="Nu se poate"
        else:
            solution+= 'Operatiirle necesare aplicate:\n'
        solution+=operatii
        return  solution;