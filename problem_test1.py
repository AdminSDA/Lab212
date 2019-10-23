from problem import Problem
import random

class ProblemTest1(Problem):
    def __init__(self):
        data = random.sample(range(100), random.randint(5, 9))
        data = sorted(data)

        statement = '0. Se primesc numerele: ' + ', '.join(map(str, data)) + '. '
        statement += 'Sortati numerele folosind metoda bulelor.'

        super().__init__(statement, data)

    def solve(self):
        return '0. Numerele sortate: ' + str(sorted(self.data))
