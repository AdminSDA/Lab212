
from problem import Problem
from itertools import permutations
import math
import random
import heapq
class Problem22(Problem):
    def __init__(self):
        data = random.sample(range(100), random.randint(4, 5))
        ls = len(data)
        heapq.heapify(data)
        statement = f'\tCerinta:\n22. Sa presupunem ca exista un min-heap care contine exact {ls} noduri care au prioritatile: {data}\n'
        statement +=" Scrieti toate modurile in care puteti insera elementele, astfel incat, la finalul inserarilor, sa aveti un heap diferit."
        
        super().__init__(statement, data)

    def solve(self):
        data = self.data
        solution = '============================================\n'
        solution+= '\tRezolvare:\n'
        solution+= 'Idee de rezolvare: Permutam toate elementele din heap-ul initial, in afara de radacina, iar dupa aceea\n am adaugat radacina la fiecare permutare si dupa am facut cate un min-heap.'
        solution+= 'Apoi am memorat min-heap-ul\n gasit, diferit de min-heap-ul initial si de toate min-heap-urile gasite precedent.\n'
        v=self.data
        perm = []
        perm = list(permutations(v[1:]))
        l = len(v)
        aux = []
        solution += f' Min-heap initial : {v} \n'
        gasite = []
        for i in range(len(perm)):
            aux = list (perm[i])
            heapq.heapify(aux)
            aux.insert(0, v[0])
            if (aux != v and aux not in gasite):
                gasite.append(aux)
        solution+= 'Alte min-heap-uri fata de cel initial:\n'
        solution+= f'{gasite}'
        return solution

p=Problem22()
print(p.statement)
print(p.solve())
