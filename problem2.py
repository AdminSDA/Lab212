
from problem import Problem

class Problem2(Problem):
    def __init__(self):
        statement = '2. Textul problemei 2'
        data = 'Date'

        super().__init__(statement, data)

    def solve(self):
        data = self.data

        return "2. Problema 2 nu este rezolvata. Datele de intrare: " + data
