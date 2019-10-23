from problem import Problem
import random

class ProblemTest2(Problem):
    def __init__(self):
        data = random.sample(range(100), random.randint(5, 9))

        statement = '0\'. Se primesc numerele: ' + ', '.join(map(str, data)) + '. '
        statement += 'Gasiti elementul maxim.'

        super().__init__(statement, data)

    def solve(self):
        solution = '0\'. Parcurgem sirul si folosim o variablia pentru a retine maximul curent.\n'
        solution += 'Presupunem ca primul element este maximul.\n'

        maxim = self.data[0]

        solution += 'La fiecare pas verificam daca elementul curent e mai mare si modificam variabila.\n'
        for item in self.data:
            solution += '\tElementul curent este: ' + str(item) + " "
            if item > maxim:
                solution += '==> Elementul este mai mare decat maximul (' + str(maxim) +  ') '
                maxim = item
                solution += '-> maximul devine ' + str(maxim) + '.'
            solution += '\n'

        solution += 'Elementul maxim este: ' + str(maxim) + '.'
        return solution
