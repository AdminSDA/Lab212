import os
import glob
from problem import Problem

if __name__ == '__main__':
    # List all classes in this directory and
    # import all that are derived from Problem
    for module in os.listdir('.'):
        if module[-3:] == '.py':
            __import__(module[:-3], locals(), globals())

    # For each subclass generate a statement and 
    # the detailed solution for that statement
    statements = []
    solutions = []

    for derived in Problem.__subclasses__():
        p = derived()

        statement = str(p)
        solution = p.solve()

        statements.append(statement)
        solutions.append(solution)


    print('### Test SDA ###')
    print('Cerinte:')
    for statement in statements:
        print(statement)
        print('')
    
    print('')

    print('Rezolvari:')
    for solution in solutions:
        print(solution)
        print('')

