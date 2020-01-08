
from problem import Problem
import random
import networkx as nx
import matplotlib.pyplot as plt


solutie = ''
sol = ''
muchii =[]
costuri =[]
result =[]
graph =[]
c=[]
m=[]

def find( parinte, i):
    if parinte[i] == i:
        return i
    a = find(parinte, parinte[i])
    parinte[i] = a
    return a

def union( parinte, rank, x, y):
    xroot = find(parinte, x)
    yroot = find(parinte, y)


    if rank[xroot] < rank[yroot]:
        parinte[xroot] = yroot
    elif rank[xroot] > rank[yroot]:
        parinte[yroot] = xroot


    else:
        parinte[yroot] = xroot
        rank[xroot] += 1



def KruskalMST(graph,V):
    global solutie
    global result

    i = 0
    e = 0
    graph = sorted(graph, key=lambda item: item[2])

    parent = []
    rank = []

    for node in range(V):
        parent.append(node)
        rank.append(0)


    while e < V - 1:


        u, v, w = graph[i]
        i = i + 1
        x = find(parent, u)
        y = find(parent, v)


        if x != y:
            e = e + 1
            result.append([u, v, w])
            union(parent, rank, x, y)



    solutie += "Muchiile arborelui de cost minim obtinut sunt urmatoarele:\n"

    for u, v, weight in result:
        solutie += str(u) + " -- " + str(v) + " == " + str(weight) + '\n'






class Problem42(Problem):

    def __init__(self):
        statement = "Primind urmatorul graf, construiti arborele partial de cost minim (Kruskal):\n\n"
        data = []
        self.ImgName = ["Graf.png", "APM.png"]
        global graph

        self.V = random.randint(6, 9)  # Generez un numar de varfuri intre 6 si 9
          # lista in care stocam graful

        matrice = [[0 for x in range(self.V)] for y in range(self.V)]  # Declar matricea de adiacenta si o initializez cu 0
        for i in range(0, self.V):
            for j in range(i + 1, self.V):   # Pentru fiecare element de deasupra diagonalei principale
                matrice[i][j] = random.randint(0, 1)    # generez 0 sau 1:  1 - exista muchie intre i si j;  0 - nu exista muchie
                matrice[j][i] = matrice[i][j]           # si fac matricea simetrica

        for i in range(0, self.V):
            ok = 0
            for j in range(0, self.V):
                if matrice[i][j] == 1:
                    ok = ok + 1         # Numar cati de 1 sunt pe o linie;
            if ok <= 1:               # daca e cel mult un 1
                for j in range(0, self.V):
                    matrice[i][j] = 1       # populez toata linia cu 0
                    matrice[j][i] = 1


        for i in range(0, self.V):
            matrice[i][i] = 0       # Fac elementele de pe diagonala principala 0


        statement += "Lista de muchii:\n"
        for i in range(0, self.V):
            for j in range(i + 1, self.V):       # Parcurg matricea deasupra diagonalei principale
                if matrice[i][j] == 1:      # daca elementul de pe pozitia [i][j] este 1
                    c = random.randint(1, 30)       # generez un cost intre 1 si 20

                    statement += str(i) + '  ' + str(j) + ' -> ' + str(c) + '\n'
                    graph.append([i, j, c])     # si adaug muchia si costul ei in graf



        super().__init__(statement, data)


    def solve(self):
        global graph
        nr_varfuri = self.V

        def afisare_graf(nr_varfuri):
            global graph
            global m
            global c
            Graph = nx.Graph()
            for u, v, weight in graph:
                Graph.add_node(u)
                Graph.add_node(v)
                edge = (u, v)
                c.append(weight)
                m.append(edge)
                Graph.add_edge(*edge)
            pos = nx.spring_layout(Graph)
            plt.figure()
            nx.draw(Graph, pos, edge_color='black', width=1, linewidths=1, node_size=500, node_color='yellow',
                    alpha=0.9, \
                    labels={node: node for node in Graph.nodes()})
            reden = {}
            for i in range(len(m)):
                reden[m[i]] = c[i]

            nx.draw_networkx_edge_labels(Graph, pos, edge_labels=reden, font_color='red')
            plt.axis('off')
            plt.savefig(self.ImgName[0])
            #plt.show()

        def afisare_APM(nr_varfuri):
            global result
            global muchii
            Arbore = nx.Graph()
            for u, v, weight in result:
                Arbore.add_node(u)
                Arbore.add_node(v)
                edge = (u, v)
                costuri.append(weight)
                muchii.append(edge)
                Arbore.add_edge(*edge)
            pos = nx.spring_layout(Arbore)
            plt.figure()
            nx.draw(Arbore, pos, edge_color='black', width=1, linewidths=1, node_size=500, node_color='purple',
                    alpha=0.9, \
                    labels={node: node for node in Arbore.nodes()})
            reden = {}
            for i in range(len(muchii)):
                reden[muchii[i]] = costuri[i]

            nx.draw_networkx_edge_labels(Arbore, pos, edge_labels=reden, font_color='red')
            plt.axis('off')
            plt.savefig(self.ImgName[1])
            #plt.show()

        solution = "Idee de rezolvare: \n"
        solution += "Pas 1: Sortam muchiile crescator in functie de cost;\n"
        solution += "pas 2: Alegem cea mai mica muchie. Verificam daca inchide un ciclu cu arborele\n"
        solution += "format pana acum. Daca nu inchide un ciclu, includem muchia in arborele de cost minim;\n"
        solution += "Pas 3: Repetam pasul 2 pana cand numarul muchiilor din arbore este cu unu mai putin decat numarul de noduri.\n\n"
        KruskalMST(graph, nr_varfuri)
        afisare_graf(nr_varfuri)
        afisare_APM(nr_varfuri)

        solution += solutie
        return solution



#p = Problem42()
#print(p.statement)
#print(p.solve())