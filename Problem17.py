
from problem import Problem



class Problem17(Problem):

    def __init__(self):
        import random
        n = random.randint(6, 15)
        k = random.randint(1, n)
        datagen = random.sample(range(30), n)
        data = [datagen, k]
        statement = "Primiti un sir de numere naturale.\n"
        statement += "Aplicati o partitionare de la QS pentru a gasi care este al k-lea element, daca vectorul ar\n"
        statement += "fi sortat si exemplificati algoritmul.\n"
        statement += "Ex: 14, 7, 9, 2, 3, 5, 8, 10 si k = 3 => v[3] = 5 (daca v ar fi sortat).\n\n"
        statement += "Sirul de numere primit este:" + str(datagen) + "\n"
        super().__init__(statement, data)

    def solve(self):
        v = self.data[0]
        w = self.data[0]
        k = self.data[1]
        solution = ""
        scris1 = ""
        scris1 += "Sir2 este:\n"
        solution += "Idee de rezolvare:\n"
        solution += "Folosim quicksort, numai ca atunci cand apelam recursiv, ne intrebam in ce parte fata de indexul pivotului se afla k si apelam numai in acea parte.\n\n"
        solution += "Sirul initial este:             " + str(v) + "\n"

        """  # Prima rezolvare, ceva mai inceata
        def partitie1(a, low, high):        #Functia pentru quicksort, doar ca returnam sirul dupa partitionare, nu pozitia pivotului
            pivot = a[high]
            i = low-1
            for j in range(low, high, 1):
                if a[j] <= pivot:
                    i += 1
                    a[i], a[j] = a[j], a[i]
            a[i+1], a[high] = a[high], a[i+1]
            x = [a, i+1]
            return x

        z = partitie1(w, 0, len(w) - 1)
        sir = z[0]
        poz = z[1]
        solution += "Sirul dupa o partitionare de la quicksort arata asa:" + str(sir) + "\n"
        nr = 0
        rasp = -1                                # Rasp este numarul cautat, gasit in urma algoritmului
        while rasp == -1:
            max = 0
            min = 99999
            if k == len(sir):                    #Cazul in care ne trebuie ultimul numar, atunci aflam maximul din sir
                for num in sir:
                    if num > max:
                        max = num
                rasp = max
                break
            if k - 1 == poz:                      #Cazul in care pivotul se afla pe pozitia k
                rasp = sir[poz]
                break
            if k - 1 > poz:                       #Cazul in care elementul cautat se afla in dreapta pivotului
                i = poz + 1
                sir2 = sir[i:len(sir)]
                scris1 += str(sir2) + "\n"
                while nr != len(sir) - k:         #Stergem maximul din sir2 pana ajungem la elementul nostru
                    for c in range(0, len(sir2)):
                        if sir2[c] > max:
                            max = sir2[c]
                            maxi = c
                    nr += 1
                    sir2.pop(maxi)
                    max = 0
                    scris1 += str(sir2) + "\n"
                max = 0
                for c in range(0, len(sir2)):      #Elementul nostru este maximul din ce a mai ramas in sir2
                    if sir2[c] > max:
                        max = sir2[c]
                rasp = max
                break
            else:                                   #Cazul in care elementul cautat se afla in stanga pivotului
                i = poz
                sir2 = sir[0:i]
                scris1 += str(sir2) + "\n"
                while nr != k-1:  # Stergem minimul din sir2 pana ajungem la elementul nostru
                    for c in range(0, len(sir2)):
                        if sir2[c] < min:
                            min = sir2[c]
                            mini = c
                    nr += 1
                    sir2.pop(mini)
                    min = 99999
                    scris1 += str(sir2) + "\n"
                min = 9999
                for c in range(0, len(sir2)):  # Elementul nostru este minimul din ce a mai ramas in sir2
                    if sir2[c] < min:
                        min = sir2[c]
                rasp = min
                break
        """
        def partitie2(a, low, high):        #Functia pentru quicksort..pivotul este mereu ultimul numar
            pivot = a[high]
            i = low-1
            for j in range(low, high, 1):
                if a[j] <= pivot:
                    i += 1
                    a[i], a[j] = a[j], a[i]
            a[i+1], a[high] = a[high], a[i+1]
            return i+1

        def partitie3(vector, low, high, pivotindex):
            pivot = vector[pivotindex]
            vector[pivotindex], vector[high] = vector[high], vector[pivotindex]
            index = low
            for i in range(low, high):
                if vector[i] < pivot:
                    vector[index], vector[i] = vector[i], vector[index]
                    index += 1
            vector[high], vector[index] = vector[index], vector[high]
            return index

        def selecteaza(vector, low, high, k):
            if low == high:
                return vector[low]
            pivotindex = k
            pivotindex = partitie3(vector, low, high, pivotindex)
            if k == pivotindex:
                return vector[k]
            elif k < pivotindex:
                return selecteaza(vector, low, pivotindex-1, k)
            else:
                return selecteaza(vector, pivotindex+1, high, k)

        rasp2 = ""
        rasp2 += "Dupa algoritmul nostru, am gasit elementul:"
        rasp2 += str(selecteaza(v, 0, len(v)-1, k-1)) + "\n"

        def quicksort(a, low, high):        #QuickSort recursiv
            if low < high:
                pi = partitie2(a, low, high)
                quicksort(a, low, pi-1)
                quicksort(a, pi+1, high)
            return a

        v = quicksort(v, 0, len(v)-1)       #Sortez vectorul initial, doar ca sa il afisam si sa vedem ca merge problema
        element = v[k-1]                    #Numarul de pe pozitia k, luat din vectorul sortat

        solution += "Sirul dupa quicksort arata asa: " + str(v) + "\n"
        solution += "K este egal cu " + str(k) + "=> v[" + str(k) + "] = " + str(element) + "\n"
        #solution += scris1  #Sterge # daca ai nevoie sa vezi cum se sterge din sir2
        #solution += "Dupa aplicarea algoritmului, am gasit elementul "
        #solution += str(rasp) + "\n"
        solution += rasp2
        return solution
