from problem import Problem
import random
import networkx as nx
import matplotlib.pyplot as plt
import heapq
# class Node:
#     def __init__(self, )

graf = []
class Problem41(Problem):
    def __init__(self):
        statement = 'Primind urmatorul graf, construiti arborele partial de cost minim folosind algoritmul lui Prim cu heap-uri.\n'
        statement += "Nod1 Nod2 -> cost"
        numberOfNodes = random.randint(5, 9)
        
        for i in range(numberOfNodes):
            graf.append([])
        
        adiacente = [[0 for x in range(numberOfNodes)] for y in range(numberOfNodes)]
         
        def genereazaMatrice():
            for i in range(numberOfNodes):
                for j in range(i + 1, numberOfNodes):
                    muchie = random.randint(0, 2)
                    adiacente[i][j] = muchie
                    adiacente[j][i] = muchie
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
        for i in range(len(adiacente)):
            for j in range(len(adiacente)):
                print(adiacente[i][j], end=" ")
            print("")
        adiacente.clear()

        data = str(numberOfNodes)
        listaMuchii = []

        def construiesteListaMuchii():
            for i in range (len(graf)):
                for elem in graf[i]:
                    listaMuchii.append((i, elem[0], elem[1]))
        
        global dictionarMuchii
        dictionarMuchii = {}
        def construiesteDictionarMuchii():
            construiesteListaMuchii()
            for elem in listaMuchii:
                dictionarMuchii[(elem[0], elem[1])] = elem[2]
            #print(dictionarMuchii)
        
        global afiseazaGraf
        def afiseazaGraf():
            construiesteDictionarMuchii()
            G = nx.Graph()
            nodes = [elem for elem in range(len(graf))]
            weightedEdges = []
            G.add_nodes_from(nodes)
            for i in range(len(graf)):
                for elem in graf[i]:
                    G.add_edge(i, elem[0])
            
            pos = nx.spring_layout(G)
            plt.figure()    
            nx.draw(G,pos,edge_color='black',labels={node:node for node in G.nodes()})
            nx.draw_networkx_edge_labels(G,pos,edge_labels=dictionarMuchii)
            plt.axis('off')
            plt.savefig("Graf.png")
            plt.show()
            plt.close()
    
        super().__init__(statement, data)

    def solve(self):
        data = self.data
        solution = ""
        solution += data
        numberOfNodes = len(graf)
        for i in range(numberOfNodes):
           print(i, ":",graf[i])
        
        
        tata = [0 for i in range(numberOfNodes)]
        listaMuchiiArbore = []
        def prim(nod):
            vizitat = [0 for i in range(numberOfNodes)]
            coada = []
            heapq.heappush(coada, (nod, (nod, -1)))
            pas = 1
            e = coada[0]
            while(len(coada) != 0):
                p = e[0]
                v = e[1][0]
                u = e[1][1]

                #print(e, "cu v = ", v)
                if(not vizitat[v]):
                    if (u != -1):
                        listaMuchiiArbore.append((v, u, p))
                    vizitat[v] = 1
                    tata[v] = u
                    for elem in graf[v]:
                        heapq.heappush(coada, (elem[1], (elem[0], v)))
                
                # print("La pasul ", pas, "coada initiala era:")
                # print(coada)
                e = heapq.heappop(coada)
                # print("Dupa stergere:")
                # print(coada)
                # print("")
        prim(0)
        print("Tata:")
        for i in range(len(tata)):
                print(tata[i], " ")
        
        print(listaMuchiiArbore)
        def afiseazaArbore():
            dictionarMuchiiArbore = {}
            for elem in listaMuchiiArbore:
                dictionarMuchiiArbore[(elem[0], elem[1])] = elem[2]
            G = nx.Graph()
            nodes = [elem for elem in range(len(graf))]
            weightedEdges = []
            G.add_nodes_from(nodes)
            for elem in listaMuchiiArbore:
                G.add_edge(elem[0], elem[1])
            
            pos = nx.spring_layout(G)
            plt.figure()    
            nx.draw(G,pos,edge_color='black',labels={node:node for node in G.nodes()})
            nx.draw_networkx_edge_labels(G,pos,edge_labels=dictionarMuchiiArbore)
            plt.axis('off')
            plt.savefig("Arbore.png")
            plt.show()
            plt.close()

        afiseazaGraf()
        afiseazaArbore()

        return solution

