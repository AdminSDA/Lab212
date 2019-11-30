
from problem import Problem

class Problem29(Problem):
    def __init__(self):
        
        import random

        n = random.randint(10, 15)
        k = random.randint(3, 4)
        data = random.sample(range(1, 100), n)
        random.shuffle(data)

        data2=[]

        i=0

        while i<n:
            x=random.randint(1,100)
            if x<=20 and len(data2)>0 and data2[-1]!=0:
                if i<k:
                    if x<=10:
                        data2.append(0)
                        continue
                    else:
                        data2.append(data[i])
                        i+=1
                        continue
                data2.append(0)
            else:
                data2.append(data[i])
                i+=1

        statement="\nPrimiti "+str(n)+" numere naturale si atunci cand primiti 0, trebuie sa afisati cele mai mari "+str(k)+" elemente.\n"
        statement+="\nSirul primit este: "+" ".join([str(i) for i in data2])
        data=[len(data2),k,data2]

        super().__init__(statement, data)

    def solve(self):

        import random

        n=self.data[0]
        k=self.data[1]
        data=self.data[2]

        solution="Idee de rezolvare:\n\n"
        solution+="Inseram intr-un vector v1 primele elemente mai mari decat 0 (daca primim un zero inainte, inseamna ca nu "
        solution+="avem k elemente, deci le afisam pe toate).\n\nAcum in acel vector v1 avem k elemente.\n\nContinuam sa citim "
        solution+="urmatoarele elemente intr-un vector v2. Cand primim 0, punem la gramada elemente lui"
        solution+=" v1 si ale lui v2 si aplicam statistici de ordine ca sa obtinem cele mai mari elemente din v1 si v2. Facem o"
        solution+=" partitionare quicksort cu un pivot ales la intamplare, si verificam daca pivotul este pe a k-a pozitie sau nu; daca"
        solution+=" k > pozitia, partitionam la stanga; daca k < pozitia, partitionam la dreapta; altfel, ne aflam pe pozitia k si acesta "
        solution+="este numarul cautat.\n\n"   

        solution+="Sirul dat : "+" ".join([str(i) for i in data])+"\n"
        solution+="k= "+str(k)+"\n\n"

        v1=[]
        v2=[]

        def partition(data, low, high):
            piv = random.randint(low, high)
            data[piv], data[low] = data[low], data[piv]
            pivot = data[low]
            i = high + 1

            for j in range (high, low, -1):
                if data[j] >= pivot:
                    i = i-1
                    data[j], data[i] = data[i], data[j]
                    
            data[i - 1], data[low] = data[low], data[i - 1]
            return i - 1

        def quickselect(data, low, high, k):
            
            if low < high:
                p = partition(data, low, high)
                if k < p:
                    quickselect(data, low, p-1, k)
                elif k > p:
                    quickselect(data, p+1 , high, k)
                else:
                    pass


        i=0

        while i < n:

            if data[i]==0:

                solution += "v1: " + " ".join([str( i ) for i in v1])+"\n"

                solution += "v2: " + " ".join([str( i ) for i in v2])+"\n"

                solution+= "v: "+ " ".join([str( i ) for i in v1])+" "+" ".join([str( i ) for i in v2])

                if len(v1) <= k and len(v2)==0:
                    solution+=" => nu avem inca k elemente, nu e nevoie de partitionare \n"
                    solution+="Cele mai mari k elemente: "+" ".join([str( i ) for i in v1])+"\n\n"
                else:
                    v1.extend(v2)
                    quickselect(v1, 0, len(v1) - 1, len(v1) - k)   
                    solution+=" => "+ " ".join([str( i ) for i in v1])+"\n"
                    v1 = v1[len(v1) - k:]                             
                    v2 = []
                    solution+="Cele mai mari k elemente: "+" ".join([str( i ) for i in v1])+"\n\n"
            else:
                if len(v1) < k:
                    v1.append(data[i])
                else:
                    v2.append(data[i])
            i+=1
        
        return solution