from problem import Problem
import random

class Problem32(Problem):
    def __init__(self):

        data = random.sample(range(30), random.randint(7, 15)) # data este un array de numere
        data.sort() # sortez vectorul
        data = list(map(lambda x: [x, None, None], data)) # fiecare numar x din data devine [x, None, None]
        self.search = random.randint(0, 30) # search este numarul cautat, generat random
        # generam un arbore binar Prim Min ABC, functia este recursiva
        self.generatePrimMinABC(data, 0, len(data) - 1)
        statement = 'Un Prim-Min ABC este un arbore cu urmatoarele proprietati:\n'
        statement +='> radacina are valoarea minima din arbore;\n'
        statement +='> fiecare valoare din sub-arborele st. are o valoare mai mica decat orice valoare din subarborele dr;\n'
        statement +='> sub-arborele stang si sub-arborele drept sunt Prim-Min ABC.\n'
        statement += f'Primim numarul {self.search} si Prim-Min ABC-ul dat de lista de copii:\n'
        for element in data:
            stanga = data[element[1]][0] if element[1] else None
            dreapta = data[element[2]][0] if element[2] else None
            
            statement += f'\t{element[0]}: {stanga}, {dreapta}\n'
        statement += f'Cerinta: Decideti daca acesta  apare in acest arbore.\n'
        super().__init__(statement, data)

    def generatePrimMinABC(self, data, start, final):    
        i = start + 1
        j = int((start + final) / 2) + 1

        nodCurent = data[start]
        if i == j and final - start == 1:
            # pozitionez nodul, aleator, la stanga sau la dreapta fata de nodul curent
            nodCurent[ random.choice([1,2]) ] = j
        if i < j:
            nodCurent[1] = i
            nodCurent[2] = j
            self.generatePrimMinABC(data, i, j - 1)
            self.generatePrimMinABC(data, j, final)


    def solve(self):
        solution = ''
        v = self.data
        parcurgere = v[0]
        solution += f'Parcurgem arborele incepand cu radacina pana gasim nodul cautat. De fiecare data cand ne mutam la un nod verificam daca este cel cautat. Altfel, decidem daca mergem la nodul din stanga, respectiv nodul din dreapta\n'
        while parcurgere is not None:      
            if parcurgere[0] is not None and parcurgere[0] == self.search:
                solution += f'\t\tNodul curent este egal cu {self.search}\n'
                solution += f'\nNumarul {self.search} se afla in acest arbore\n'
                break
            else:
                solution += f'\t\tNodul curent nu are valoarea {self.search}\n'

            if (parcurgere[1] is None and parcurgere[2] is None) or (parcurgere[1] is not None and self.search < v[parcurgere[1]][0]):
                solution += f'\nNumarul {self.search} NU se afla in acest arbore\n'
                break
            if parcurgere[2] is not None and self.search >= v[parcurgere[2]][0]:
                solution += f'\t> Numarul cautat {self.search} >= {v[parcurgere[2]][0]}. Ne mutam la nodul din dreapta\n'
                parcurgere = v[parcurgere[2]]
            elif parcurgere[1] is not None:
                solution += f'\t> Numarul cautat {self.search} >= {v[parcurgere[1]][0]}. Ne mutam la nodul din stanga\n'
                parcurgere = v[parcurgere[1]]
            else:
                solution += f'\nNumarul {self.search} NU se afla in acest arbore\n'
                break
                
        return solution

p = Problem32()
print(p.statement)
print(p.solve())