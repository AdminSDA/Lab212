
from problem import Problem

class Problem1(Problem):
    def __init__(self):
        statement = '1. Textul problemei 1'
        data = 'Date'

        super().__init__(statement, data)

    def solve(self):
        data = self.data

        return "1. Problema 1 nu este rezolvata. Datele de intrare: " + data
