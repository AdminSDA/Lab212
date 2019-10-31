from Node import Node

# Orice are "pass" este de implementat
# + afisarea
class Tree:
    def __init__(self):
        self.root = None

    def search(self, value):
        return self.search_helper(self.root, value) 

    def search_helper(self, current_node, value):
        # la fel ca pseudocodul de la search_list_helper
        # dar fara partea cu liste (returnam valoarea/nodul, nu lista)
        pass

    def search_list(self, value):
        # returneaza o lista de noduri prin care trecem
        # pana cand ajungem la nodul cu valoarea value
        # asemanator cu inord cu liste
        return self.search_list_helper(self.root, value, [])

    def search_list_helper(self, current_node, value, search_nodes):
        # daca introducem nodurile 7, 5, 1, 6, 4 in ordine in ABC
        # si cautam nodul 4, functia returneaza:
        # [Node(7), Node(5), Node(1), Node(4)] 

        # Pseudocod:
        #   - de adaugat nodul curent in lista
        #   - daca nodul are valoarea cautata sau e None
        #       -> returnam lista curenta
        #
        #   - daca value < nodul_crt:
        #       -> returnam apelul recursiv in partea stanga
        #   - altfel:
        #       -> returnam apelul recursiv in partea dreapta
        pass

    def insert(self, value):
        self.root = self.insert_helper(self.root, value)

    def insert_helper(self, node, value):
        if node == None:
            return Node(value)
        else:
            if value < node.value:
                node.left = self.insert_helper(node.left, value)
            else:
                node.right = self.insert_helper(node.right, value)
            return node

    def predecesor(self, value):
        node = self.search(value)
        if node != None:
            return self.predecesor_helper(node)

    def predecesor_helper(self, node):
        # de gasit cel mai mare nod din subarborele stang
        # daca exista subarbore stang, daca nu ^^^
        pass

    def succesor(self, value):
        node = self.search(value)
        if node != None:
            return self.succesor_helper(node)

    def succesor_helper(self, current_node):
        # de gasit cel mai mic nod din subarborele drept 
        # daca exista subarbore drept, daca nu ^^^
        pass
    
    def delete(self, value):
        pass

    def preord(self):
        # asemanator cu inord
        pass

    def postord(self):
        # asemanator cu inord
        pass

    def inord(self):
        # trebuie sa apelam inordine pe radacina si sa pasam
        # o lista vida, pe care o vom modifica pe parcurs
        return self.inord_helper(self.root, [])

    def inord_helper(self, current_node, inord_list):
        if current_node is None:
            return

        self.inord_helper(current_node.left, inord_list)
        inord_list.append(current_node.value)
        self.inord_helper(current_node.right, inord_list)

        return inord_list

    def __str__(self):
        # Afisare desen arbore, nu parcurgerea in inordine...
        return "Parcurgerea in inordine: " + str(self.inord())

t = Tree()
t.insert(7)
t.insert(5)
t.insert(1)
t.insert(6)
t.insert(4)

print(t)
