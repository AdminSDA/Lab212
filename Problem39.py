from problem import Problem
import random


class Problem39(Problem):

    def __init__(self):
        def prim(n):
            if n == 1:
                return 0
            for d in range(2, (n // 2) + 1):
                if n % d == 0:
                    return 0
            return 1

        def initializare():
            n = random.choice(primes)
            while n < len(data):
                n = random.choice(primes)
            return n

        data = random.sample(range(100), random.randint(4, 6))
        primes = [i for i in range(7, 20) if prim(i)]
        statement = 'Construiti un hash folosind valorile:'
        statement += str(data) + '\n'

        global na
        na = random.choice(primes)
        statement += f'a). liste simplu inlantuite: h(x) = x % {na}' + '\n'

        global nb
        nb = initializare()
        statement += f'b). open adressing (linear probing): h(x, i) = (x + i) % {nb}' + '\n'

        global nc
        global a
        global b
        global c
        nc = initializare()
        a = random.randint(1, 9)
        b = random.randint(0, 9)
        c = random.randint(0, 9)
        statement += f'c).quadratic probing:h(x, i) = (x + {a}*i^2 + {b}*i + {c} ) % {nc} \n'

        global n1
        global n2
        global nd
        n1 = random.choice(primes)
        n2 = random.choice(primes)
        nd = initializare()
        statement += f'd).double hashing: h(x, i) = (x % {n1} + i * ({n2}-x % {n2} )) % {nd}\n'

        super().__init__(statement, data)

    def solve(self):

        data = self.data

        """
        Punctul a) liste simplu inlantuite
                   h(x)= x % prim
        """

        solution = "Lista simplu inlantuita este:\n"

        hash = [[] for i in range(na)]
        for x in data:
            i = x % na
            if hash[i] in hash:
                hash[i].append(x)
            else:
                hash[i] = [x]

        for i in range(na):
            solution += '\n' + str(i) + ': '
            for j in hash[i]:
                solution += ' ' + str(j)
        solution += '\n\n'

        """ 
            b)open adressing (linear probing)
                       h(x,i)=( x + i ) % prim
        
        """
        solution += 'linear probing:\n'
        hash = [None] * nb
        """solution += str(hash) + '\n\n'"""

        for x in data:
            i = 0
            while hash[(x + i) % nb] is not None:
                i += 1
            hash[(x + i) % nb] = x

        for i in range(0, len(hash)):
            if(hash[i] is None):
                solution += str(i) + ' : ' + ' ' + '\n'
            else:
                solution += str(i) + ' : ' + str(hash[i]) + '\n'
        solution += '\n\n'
        """
            c)quadratic probing: 
                h(x, i) = (x + ai^2 + bi + c ) % prim
        """
        solution += "quadratic probing:\n"
        hash = [None] * nc
        """solution += str(hash) + '\n\n'"""
        for x in data:
            i = 0
            while hash[(x + a * (i ^ 2) + b * i + c) % nc] is not None:
                i += 1
            hash[(x + a * (i ^ 2) + b * i + c) % nc] = x
        for i in range(0, len(hash)):
            if (hash[i] is None):
                solution += str(i) + ' : ' + ' ' + '\n'
            else:
                solution += str(i) + ' : ' + str(hash[i]) + '\n'
        solution += '\n\n'


        """ 
            d)double hashing: 
                 h(x, i) = (x % 5 + i * (x % 7 + 1)) % 17
        """
        solution += 'double hashing:\n'
        hash = [None] * nd

        for x in data:
            i = 0
            while hash[(x % n1 + i * (n2 - x % n2)) % nd] is not None:
                i += 1
            hash[(x % n1 + i * (n2 - x % n2)) % nd] = x
        for i in range(0, len(hash)):
            if (hash[i] is None):
                solution += str(i) + ' : ' + ' ' + '\n'
            else:
                solution += str(i) + ' : ' + str(hash[i]) + '\n'
        solution += '\n\n'

        return solution
