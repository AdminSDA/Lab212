class Problem:
    def __init__(self, statement, data):
        self.statement = statement
        self.data = data

    def solve(self):
        raise NotImplementedError

    def __str__(self):
        return self.statement

