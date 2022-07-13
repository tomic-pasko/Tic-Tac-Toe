
class Playground:
    def __init__(self):
        self.grid = ['1 | 2 | 3', '--|---|--', '4 | 5 | 6', '--|---|--', '7 | 8 | 9']

    def draw_grid(self):
        for i, line in enumerate(self.grid):
            print(line)

    def refresh_grid(self, number, x):
        if x:
            self.grid = list(map(lambda st: str.replace(st, number, "x"), self.grid))
        else:
            self.grid = list(map(lambda st: str.replace(st, number, "o"), self.grid))

