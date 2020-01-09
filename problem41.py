from problem import Problem
import random
import matplotlib.pyplot as plt
import networkx as nx

import heapq

class Problem41(Problem):
    def __init__(self):
        graf =[]
        statement = 'Primind urmatorul graf, construiti arborele partial de cost minim folosind algoritmul lui Prim cu heap-uri.\n'
        numberOfNodes = random.randint(5, 9)
        self.ImgName = ["Graf.png", "Arbore.png"]
        self.statementPicture = 1
        # self.solvePicture = 2
        for i in range(numberOfNodes):
            graf.append([])
        
        adiacente = [[0 for x in range(numberOfNodes)] for y in range(numberOfNodes)]
        zero = [0 for x in range(numberOfNodes)]
        def umpleLinia(lin):
            for elem in range (numberOfNodes):
                if (elem != lin):
                    adiacente[lin][elem] = random.randint(0, 2) 

        def genereazaMatrice():
            for i in range(numberOfNodes):
                for j in range(i + 1, numberOfNodes):
                    muchie = random.randint(0, 2)
                    adiacente[i][j] = muchie
                    adiacente[j][i] = muchie
                if (zero == [adiacente[i]]):
                    umpleLinia(i)

            for i in range(numberOfNodes):
                for j in range(i + 1, numberOfNodes):
                    if adiacente[i][j]:
                        cost = random.randint(20, 50)
                        adiacente[i][j] = cost
                        adiacente[j][i] = cost

        def construiesteGraf():
            for i in range(numberOfNodes):
                for j in range(numberOfNodes):
                    if adiacente[i][j]:
                        graf[i].append((j, adiacente[i][j]))

        genereazaMatrice()
        construiesteGraf()
        for i in range(numberOfNodes):
           statement += str(i) + ':' + str(graf[i]) + '\n'

        adiacente.clear()
        data = graf
        #data = str(graf)
        #data = str(numberOfNodes)
        
        super().__init__(statement, data)

    def solve(self):
        graf = self.data
        solution = ""
        numberOfNodes = len(graf)
        listaMuchii = []

        def construiesteListaMuchii():
            for i in range (len(graf)):
                for elem in graf[i]:
                    listaMuchii.append((i, elem[0], elem[1]))
        dictionarMuchii = {}
        def construiesteDictionarMuchii():
            construiesteListaMuchii()
            for elem in listaMuchii:
                dictionarMuchii[(elem[0], elem[1])] = elem[2]

        
        def afiseazaGraf():
            construiesteDictionarMuchii()
            G = nx.Graph()
            nodes = [elem for elem in range(len(graf))]
   
            G.add_nodes_from(nodes)
            for i in range(len(graf)):
                for elem in graf[i]:
                    G.add_edge(i, elem[0])
            
            pos = nx.spring_layout(G)
            plt.figure()    
            nx.draw(G,pos,edge_color='black',labels={node:node for node in G.nodes()})
            nx.draw_networkx_edge_labels(G,pos,edge_labels=dictionarMuchii)
            plt.axis('off')
            plt.savefig(self.ImgName[0])
            #plt.savefig("Graf.png")
            #plt.show()
            plt.close()
        afiseazaGraf()
        
        tata = [0 for i in range(numberOfNodes)]
        listaMuchiiArbore = []
        def prim(nod):
            vizitat = [0 for i in range(numberOfNodes)]
            coada = []
            heapq.heappush(coada, (nod, (nod, -1)))
            while(len(coada) != 0):
                e = heapq.heappop(coada)
                p = e[0]
                v = e[1][0]
                u = e[1][1]
                if(not vizitat[v]):
                    if (u != -1):
                        listaMuchiiArbore.append((v, u, p))
                    vizitat[v] = 1
                    tata[v] = u
                    for elem in graf[v]:
                        heapq.heappush(coada, (elem[1], (elem[0], v)))
                
        prim(0)
        solution += "Idee de implemetare:\n"
        solution += "Algorimul lui Prim foloseste un min-Heap in care pune muchiile in functie de cost.\n"
        solution += "La primul pas considera nodul de start ca fiind solutia, adica arborele partial de cost minim.\n"
        solution += "Pentru a adauga noduri in arbore adaugam vecinii nodului de start intr-un heap in functie de cosul muchiei.\n"
        solution += "Ca sa adaugam muchia cu costul cel mai mic vom decapita heapul pentru a obtine muchia minima adiacenta la solutie.\n"
        solution += "Acum consideram solutia formata din cele doua noduri si punem in heap vecinii celui de-al doilea nod.\n"
        solution += "Repetam algoritmul pana cand vizitam toate nodurile din graf.\n"
        solution += "La final vom obtine arborele partial de cost minim.\n"

        
        solution += "\n################################################################################\n"
        solution += "Rezultat:\n"
        solution += "Arborele partial reprezentat prin vectorul de tati este:\n"
        solution += str(tata)
        def afiseazaArbore():
            dictionarMuchiiArbore = {}
            for elem in listaMuchiiArbore:
                dictionarMuchiiArbore[(elem[0], elem[1])] = elem[2]
            G = nx.Graph()
            nodes = [elem for elem in range(len(graf))]
  
            G.add_nodes_from(nodes)
            for elem in listaMuchiiArbore:
                G.add_edge(elem[0], elem[1])
            
            pos = nx.spring_layout(G)
            plt.figure()    
            nx.draw(G,pos,edge_color='black',labels={node:node for node in G.nodes()})
            nx.draw_networkx_edge_labels(G,pos,edge_labels=dictionarMuchiiArbore)
            plt.axis('off')
            #plt.savefig("Arbore.png")
            plt.savefig(self.ImgName[1])
            #plt.show()
            plt.close()

        afiseazaArbore()
        
        return solution