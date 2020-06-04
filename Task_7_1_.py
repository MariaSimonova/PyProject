class Matrix:
    def __init__(self, a):
        self.b = '\n'.join(['\t'.join([str(j) for j in i]) for i in a])
        List = []
        for i in a:
            List.append([j for j in i])
        self.a = List

    def __str__(self):
        self.c = str(self.b)
        return self.c

    def __add__(self, other):
        NumStr = len(self.a)
        NumCol = len(other.a[0])
        for i in range(NumStr):
            for j in range(NumCol):
                self.a[i][j] = self.a[i][j] + other.a[i][j]
            Result = self.a
        return Matrix(Result)


m1 = Matrix([[1, 2], [3, 4], [5, 6]])
m2 = Matrix([[7, 8], [9, 10], [11, 12]])
print(m1)
print()
print(m2)
print()
print(m1 + m2)
