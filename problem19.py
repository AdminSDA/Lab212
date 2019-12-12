
from problem import Problem
import random
import heapq
class Problem19(Problem):
    def __init__(self):
        statement = '19. Construiti un min-heap folosind valorile: '
        data = random.sample(range(100), random.randint(7, 12))
        statement += f'{data} . Decapitati heap-ul.'
        super().__init__(statement, data)

    def solve(self):
        data = self.data
        solution = ''
        v=self.data

        heapq.heapify(v)
        solution+= f'Heap-ul initial este {v}\n'
        while v:
            solution+= f'Scot elementul {v[0]} din heap\n '
            heapq.heappop(v)

            solution +=f'{v} \n'

        return solution

p=Problem19()
print(p.statement)
print(p.solve())
