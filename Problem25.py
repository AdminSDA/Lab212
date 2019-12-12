from problem import Problem
import random

class Problem25(Problem):

    def __init__(self):
        data = random.sample(range(100), random.randint(7, 10))

        statement = '1. Sa presupunem ca am vrea sa implementam un heap ternal (fiecare nod are 3 fii). \n'
        statement += '2. Introduceti elementele: ' + str(data) + ' intr-un max heap ternal si decapitati heap-ul. \n'

        super().__init__(statement, data)

    def solve(self):
        data = self.data
        global solution
        solution = '3. Solutia problemei: \n'
        solution += '\t0.Vectorul este: ' + str(data) + '\n'
        solution += '\t1.Adaugam noduri in heap: \n'

        def sift_up(heap, idx):
            if idx == 0:
                return
            father = int((idx - 1) / 3)
            global solution
            if heap[idx] >= heap[father]:
                solution += '\t\t\t'+ str(heap[idx]) + " >= " + str(heap[father]) + ' : ' + 'Swap\n'
                heap[father], heap[idx] = heap[idx], heap[father]
                sift_up(heap, father)

        def sift_down(heap, idx):
            k = 1
            n = len(heap)
            swap_son = idx
            left_son = 3 * idx + 1
            middle_son = 3 * idx + 2
            right_son = 3 * idx + 3
            global solution
            if left_son < n and heap[left_son] > heap[swap_son]:
                solution += '\t\t4.' + str(k) + ' : ' + str(heap[left_son]) + " > " + str(heap[swap_son]) + ' : ' + str(heap) + '\n'
                k += 1
                swap_son = left_son
            if middle_son < n and heap[middle_son] > heap[swap_son]:
                solution += '\t\t4.' + str(k) + ' : ' + str(heap[middle_son]) + " > " + str(heap[swap_son]) + ' : ' + str(heap) + '\n'
                k += 1
                swap_son = middle_son
            if right_son < n and heap[right_son] > heap[swap_son]:
                solution += '\t\t4.' + str(k) + ' : ' + str(heap[right_son]) + ' > ' + str(heap[swap_son]) + ' : ' + str(heap) + '\n'
                k += 1
                swap_son = right_son

            heap[idx], heap[swap_son] = heap[swap_son], heap[idx]
            if swap_son != idx:
                sift_down(heap, swap_son)

        heap = []
        j = 1

        for i in range(len(data)):
            solution += "\t\t" + str(1) + "." + str(j) + " : "
            j += 1
            heap.append(data[i])
            solution += str(heap) + '\n'
            sift_up(heap, i)

        solution += '\t2.Arborele in heap : ' + str(heap) + '\n'

        solution += '\t3.Pentru decapitare interschimbam : ' + str(heap[0]) + ' si ' + str(heap[len(heap) - 1]) + '\n'
        heap[0], heap[len(heap) - 1] = heap[len(heap) - 1], heap[0]
        heap.pop()
        solution += '\t4.Arborele decapitat ' + str(heap) + '\n'
        sift_down(heap, 0)
        solution += '\t5.Arborele rearanjat ' + str(heap) + '\n'

        return solution
