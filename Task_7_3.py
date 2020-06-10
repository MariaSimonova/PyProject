class Cell:
    def __init__(self, n):
        self.n = n

    def __add__(self, other):
        return f"Увеличение клеток: {Cell(self.n + other.n)}"

    def __sub__(self, other):
        if self.n < other.n:
            return f"Действие произвести невозможно"
        else:
            return f"Уменьшение клеток: {Cell(self.n - other.n)}"

    def __mul__(self, other):
        return f"Умножение клеток: {Cell(self.n * other.n)}"

    def __truediv__(self, other):
        if self.n < other.n:
            return f"Действие произвести невозможно"
        else:
            return f"Деление клеток: {Cell(round(self.n / other.n))}"

    def __str__(self):
        return f"{self.n}"

    def make_order(self, i):
        self.i = i
        while self.n >= 0:
            if self.n >= self.i:
                q = "*" * self.i
                print(f"{q}")
            else:
                q = "*" * self.n
                print(f"{q}")
            self.n = self.n - self.i


cell_1 = Cell(5)
cell_2 = Cell(3)
print(cell_1 + cell_2)
print(cell_1 - cell_2)
print(cell_1 * cell_2)
print(cell_1 / cell_2)
print()
print(cell_1.make_order(3))
print()
print(cell_2.make_order(3))
