from problem import Problem
#import random
class Problem23(Problem):

    def __init__(self):
        import random
        # data = [8, 5, 3, 9, 2, 1, 7, 6]
        # n = len(data)
        n = random.randint(8, 12)
        data = random.sample(range(12), n)
        statement = f'Problema 23:\n'
        statement += f'Primiti vectorul: { str(data) }. \n'
        statement += f'Faceti din acest vector un min-ansamblu folosind un numar\n'
        statement += f'minim de operatii si demonstrati complexitatea. \n'
        
        super().__init__(statement, data)

    def shiftDown(self, H, n, index):

        l = 2 * index + 1
        r = 2 * index + 2
        newIndex = index

        if l < n and H[l] < H[newIndex]:
            newIndex = l

        if r < n and H[r] < H[newIndex]:
            newIndex = r


        H[index], H[newIndex] = H[newIndex], H[index]

        if(newIndex != index):
            self.shiftDown(H, n, newIndex)



    def solve(self):
        v = self.data
        solution ="Ideea de rezolvare:\n"
        solution +="Aplicam shiftDown pentru nodurile de la [n/2,0] (in ordinea asta).\n"
        solution +="Shiftdown compara recursiv un nod i cu cei 2 copii si se interschimba\n"
        solution +="cu cel mai mic si aplicam algoritmul pana ajungem la o frunza.\n"

        n = len(self.data)
        for i in range(int(n / 2), -1, -1):
            self.shiftDown(self.data, n, i)
            solution +="Dupa pasul " + str((n//2)-i+1) + " sirul nostru arata astfel:\n" +str(self.data) + "\n"
        #return self.data
        solution +="In final vom obtine min-ansamblul: \n"
        solution +="" + str(self.data) + "\n"
        solution += "Complexitatea algoritmului este O(n)."
        return solution


# todo: delete this
obj = Problem23()
print(obj.statement)
print(obj.solve())