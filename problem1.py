from problem import Problem
import random
import string
 
 
def random_string_generator(str_size, allowed_chars):
    return ''.join(random.choice(allowed_chars) for x in range(str_size))
 
 
class Problem1(Problem):
    def __init__(self):
        chars = string.ascii_letters
        size1 = random.randrange(1, 10)
        size2 = random.randrange(1, 10)
        size3 = random.randrange(1, 10)
        data1 = random_string_generator(size1, chars)
        data2 = random_string_generator(size2, chars)
        data3 = random_string_generator(size3, chars)
        statement = 'Aveti la dispozitie 3 SD: \n'
        statement += '1 -> stiva\n'
        statement += '2 -> coada\n'
        statement += '3 -> stiva\n'
        statement += 'Operatii:\n'
        statement += 'caracter -> se introduce caracterul in prima stiva\n'
        statement += '1 -> se scoate din structura 1 se introduce in structura 2\n'
        statement += '2 -> se scoate din structura 2 se introduce in structura 3\n'
        statement += '3 -> se scoate din structura 3 se introduce in structura 1\n'
        statement += 'Scrieti un sir de operatii pentru a avea la sf.\n'
        statement += '1 -> ' + data1
        statement += '\n2 -> ' + data2
        statement += '\n3 -> ' + data3
        data = data1 + ' ' + data2 + ' ' + data3
        super().__init__(statement, data)
 
    def solve(self):
        # implementare stiva
        class Stack:
            def __init__(self):
                self.items = []
                self.v = []
 
            def isEmpty(self):
                return self.items == []
 
            def push(self, item):
                self.items.append(item)
 
            def pop(self):
                return self.items.pop()
 
            def peek(self):
                return self.items[len(self.items) - 1]
 
            def size(self):
                return len(self.items)
 
            def show(self):
                print(self.items)
 
            def toArray(self):
                v = []
                while self.isEmpty() == False:
                    x = self.pop()
                    v.append(x)
                x = len(v)-1
                while x>=0:
                    self.push(v[x])
                    x = x-1
                self.v = list(reversed(v))
 
        stack1 = Stack()
        stack2 = Stack()
 
        # implementare coada
        class Node(object):
 
            def __init__(self, item=None):
                self.item = item
                self.next = None
                self.previous = None
 
        class Queue(object):
 
            def __init__(self):
                self.size = 0
                self.front = None
                self.rear = None
                self.v = []
 
            def isEmpty(self):
                return self.size == 0
 
            def Push(self, x):
                newNode = Node(x)
                if self.isEmpty():
                    self.front = self.rear = newNode
                else:
                    self.rear.next = newNode
                newNode.previous = self.rear
                self.rear = newNode
                self.size += 1
 
            def Pop(self):
                item = self.front.item
                self.front = self.front.next
                self.size -= 1
                if self.isEmpty():
                    self.rear = None
                return item
 
            def toArray(self):
                v = []
                while self.isEmpty() == False:
                    x = self.Pop()
                    v.append(x)
                for x in v:
                    self.Push(x)
 
                self.v = v
 
        queue = Queue()
        s = self.data
        sol = "\n"
        solutie = '\nInitial propozitia este: ' + '"' + str(s) + '"'
        s = s.split(" ")
        solutie += '\nSe imparte propozitia in cuvinte intr-un vector.'
        solutie += '\nAstfel vectorul devine:  ' + str(s)
 
        solutie += "\nUrmeaza sa verificam daca propozitia are 3 cuvinte.\n"
        if len(s) != 3:
            print("Nu sunt 3 cuvinte\n")
 
        else:
            solutie += 'Daca indeplineste conditia introducem primul cuvant in stiva 1 astfel:\n'
 
            a = list(s[0])
            solutie += 'Se imparte primul cuvant in litere (ex. afara) si la fiecare pas:\n'
            for x in a:
                stack1.push(x)
                sol += "'" + str(x) + "'" + " "
                solutie += '\n\t\t\t\tSe foloseste doar operatia "x" si se adauga litera: ' + str(x)
                stack1.toArray()
                solutie += '\n\t\t\t\tStiva 1: ' + ' ' + str(stack1.v) + '\n'
 
            a = list(s[2])
            solutie += '\nVrem sa introducem in stiva 1 cel de-al treilea cuvant (pe litere), apoi il introducem in coada, apoi in stiva 2.'
            solutie += "\nSe imparte al treilea cuvant in litere (ex. soare) si la fiecare pas:\n"
 
            for x in a:
                stack1.push(x)
                sol += "'" + str(x) + "'" + " "
                solutie += '\n\t\t\t\tSe foloseste operatia "x" si se adauga in stiva 1 litera:' + str(x)
                stack1.toArray()
                solutie += '\n\t\t\t\tStiva 1 : ' + ' ' + str(stack1.v)
                queue.Push(stack1.pop())
                sol += "1" + " "
                solutie += '\n\t\t\t\tSe foloseste operatia 1 si se scoate din stiva 1 litera ' + "'" + str(
                    x) + "'" + ' apoi se introduce in coada\n'
                stack1.toArray()
                queue.toArray()
                solutie += '\t\t\t\tStiva 1: ' + str(stack1.v)
                solutie+= '\n\t\t\t\tCoada: ' + str(queue.v)
                stack2.push(queue.Pop())
                sol += "2" + " "
                solutie += '\n\t\t\t\tSe foloseste operatia 2 si se scoate din coada litera ' + "'" + str(
                    x) + "'" + ' apoi se introduce in stiva 2\n'
                stack2.toArray()
                queue.toArray()
                solutie += '\t\t\t\tCoada: ' + str(queue.v)
                solutie += '\n\t\t\t\tStiva 2: ' + str(stack2.v) + '\n'
 
 
 
            a = list(s[1])
            solutie += '\n\nVrem sa introducem in stiva 1 cel de-al doilea cuvant (pe litere), apoi il introducem in coada:\n'
            solutie += 'Se desparte al doilea cuvant in litere si la fiecare pas:\n'
            for x in a:
                stack1.push(x)
                sol += "'" + str(x) + "'" + " "
                solutie += '\n\t\t\t\tSe foloseste operatia "x" si se adauga in stiva 1 litera: ' + str(x)
                stack1.toArray()
                solutie += '\n\t\t\t\tStiva 1: ' + str(stack1.v)
                queue.Push(stack1.pop())
                sol+= "1" + " "
                solutie += '\n\t\t\t\tSe foloseste operatia 1 scotandu-se din stiva 1 litera ' "'" + str(
                    x) + "'" + ' apoi se adauga in coada'
                queue.toArray()
                stack1.toArray()
                solutie += '\n\t\t\t\tStiva 1: ' + str(stack1.v)
                solutie += '\n\t\t\t\tCoada: ' + str(queue.v) + '\n'
            solutie += 'La final:\n'
 
            stack1.toArray()
            solutie += "Elementele stivei 1 sunt:\n" + str(stack1.v)
            queue.toArray()
            solutie += "\nElementele cozii sunt:\n" + str(queue.v)
            stack2.toArray()
            solutie += "\nElementele stivei 2 sunt:\n" + str(stack2.v)
            solutie += "\nSecventa de operatii este: " + sol
            return solutie
 
 
p = Problem1()
print(p.statement)
print(p.solve())