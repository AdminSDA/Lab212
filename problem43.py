from problem import Problem
import networkx as nx
import matplotlib.pyplot as plt
import random
import heapq

matrice = []
lista_muchii = []
distante = {}
costuri = []
muchii = []
anterior = {}
graf = {}


def dijkstra(graph, nod_start):
    global distante
    global anterior
    distante = {nod: float('infinity') for nod in graph}
    anterior = {nod: -1 for nod in graph}
    distante[nod_start] = 0  # distanta[A] = 0
    anterior[nod_start] = nod_start
    pq = [(0, nod_start)]  # priority queue #deci intai adaug 0,A
    while len(pq) > 0:
        distanta_curenta, nod_curent = heapq.heappop(pq)  # extragem de fiecare data nodul cu distanta minima


        for vecin, cost in graph[nod_curent].items():  # fiecare vecin si costul
            distanta = distanta_curenta + cost  # calculam noua distanta

            # Luam in considerare noua distanta doar daca e mai scurta decat ce gasisem anterior

            if distanta < distante[vecin]:
                distante[vecin] = distanta
                anterior[vecin] = nod_curent
                heapq.heappush(pq, (distanta, vecin))


def construct_graf(nr_noduri):
    global graf
    global matrice
    matrice = [[0 for i in range(nr_noduri)] for j in range(nr_noduri)]

    for i in range(nr_noduri):
        for j in range(i + 1, nr_noduri):
            matrice[i][j] = random.randint(0, 1)

    global lista_muchii

    for i in range(nr_noduri):
        for j in range(i + 1, nr_noduri):
            graf[str(chr(65 + i))] = {}
            graf[str(chr(65 + j))] = {}

    for i in range(nr_noduri):
        for j in range(i + 1, nr_noduri):
            if matrice[i][j] == 1:
                cost = random.randint(1, 15)
                costuri.append(cost)
                lista_muchii.append([chr(65 + i), chr(65 + j), cost])
                # lista_muchii.append([chr(65 + i), chr(65 + j), cost])
                graf[str(chr(65 + i))][str(chr(65 + j))] = cost
                graf[str(chr(65 + j))][str(chr(65 + i))] = cost


class Problem43(Problem):

    def __init__(self):
        self.nr_vf = random.randint(5, 7)
        self.ImgName = ["graph.png"]

        construct_graf(self.nr_vf)
        statement = "43 (DC) Primind urmatorul graf (neorientat):\n"
        statement += str(graf) + "\n"

        statement += "Lista de muchii:\n"
        for i in range(len(lista_muchii)):
            statement += str(lista_muchii[i]) + "\n"

        statement += "Aplicati algoritmul lui Dijkstra (pe heap-uri) pornind din nodul 1 pentru a gasi distanta minima"
        statement += "de la acesta catre oricare alt nod din graf.\n"
        statement += "\nIdee de rezolvare:\n"
        statement += "Construim un dictionar pentru distante si atribuim infinit tuturor nodurilor, cu exceptia nodului de start, care va primi 0\n"
        statement += "Construim o coada de prioritate/heap in care adaugam initial nodul de start cu distanta 0. \n" \
                     "Calculam distantele de la nodul de start la toti vecinii sai, pe care ii adaugam in heap, cu distantele respective.\n" \
                     "Extragem din heap nodul cu distanta cea mai mica si verificam daca distantele de la nodul de start prin\n" \
                     "acest nod sunt mai mici decat ceea ce aveam deja, caz in care actualizam dictionarul de distante si adaugam" \
                     "in heap distantele mai bune si nodurile corespunzatoare.\n" \
                     "Repetam ultimul pas pana coada de prioritate este vida\n"
        data = []
        super().__init__(statement, data)

    def solve(self):
        n = self.nr_vf

        def afisareGraf(nr_noduri):
            G = nx.Graph()
            for i in range(nr_noduri):
                for j in range(i + 1, nr_noduri):
                    if matrice[i][j] == 1:
                        G.add_node(str(chr(65 + i)))
                        G.add_node(str(chr(65 + j)))
                        edge = (str(chr(65 + i)), str(chr(65 + j)))
                        muchii.append(edge)
                        G.add_edge(*edge)
            pos = nx.spring_layout(G)
            plt.figure()
            nx.draw(G, pos, edge_color='black', width=1, linewidths=1, node_size=500, node_color='green', alpha=0.9, \
                    labels={node: node for node in G.nodes()})
            reden = {}
            for i in range(len(muchii)):
                reden[muchii[i]] = costuri[i]
            # print(reden)
            nx.draw_networkx_edge_labels(G, pos, edge_labels=reden, font_color='red')
            plt.savefig(self.ImgName[0])
            plt.axis('off')
            # plt.show()

        dijkstra(graf, 'A')
        afisareGraf(n)
        solution = "Distanta minima de la nodul A catre oricare alt nod din graf este: \n"
        solution += str(distante) + "\n"
        solution += "Nodul anterior fiecarui nod este:\n"
        solution += str(anterior)
        return solution

# p = Problem43()
# print(p.statement)
# print(p.solve())
