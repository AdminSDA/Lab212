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
        statement +='• radacina are valoarea minima din arbore;\n'
        statement +='• fiecare valoare din sub-arborele st. are o valoare mai mica decat orice valoare din subarborele dr;\n'
        statement +='• sub-arborele stang si sub-arborele drept sunt Prim-Min ABC.\n'
        statement +='Primind un Prim-Min ABC si un numar k, decideti daca k apare in acest arbore.'
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
        v = self.data
        solution = f'•Arborele generat este:\n{v}\n'
        parcurgere = v[0]

        while parcurgere is not None:
            if(parcurgere[0] == self.search):
                solution += f'•Numarul {self.search} se afla in acest arbore\n'
                break
            if (parcurgere[1] is None and parcurgere[2] is None) or (parcurgere[1] is not None and self.search < v[parcurgere[1]][0]):
                solution += f'•Numarul {self.search} NU se afla in acest arbore\n'
                break
            if parcurgere[2] is not None and self.search >= v[parcurgere[2]][0]:
                parcurgere = v[parcurgere[2]]
            elif parcurgere[1] is not None:
                parcurgere = v[parcurgere[1]]
            else:
                solution += f'•Numarul {self.search} NU se afla in acest arbore\n'

                break
        solution += f'•Mergem pe fiecare nivel al arborelui verificand daca\n'
        solution += f' numarul {self.search} apare in acesta, accesand fiecare element al sau.\n'
        solution += f'•Daca numarul cautat este gasit s-a incheiat programul.\n'
        return solution

p = Problem32()
print(p.statement)
print(p.solve())
