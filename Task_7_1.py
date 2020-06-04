class Matrix:
    def __init__(self, my_list, i):
        self.my_list = my_list
        self.i = int(i)
        self.p_1 = my_list[self.i][0]
        self.p_2 = my_list[self.i][1]

    def __add__(self, other):
        return Matrix(self.p_1 + other.p_1, self.p_2 + other.p_2)

    def __str__(self):
        return f"{self.p_1} {self.p_2}"

matrix_1 = [[1, 2], [2, 3], [4, 5]]
for i in range(len(matrix_1)):
    q = str(i)
    print(Matrix(matrix_1, q))

print()
matrix_2 = [[6, 7], [8, 9], [10, 11]]
for i in range(len(matrix_2)):
    q = str(i)
    print(Matrix(matrix_2, q))

print()
for i in range(len(matrix_2)):
    q = str(i)
    print(Matrix(matrix_1, q) + Matrix(matrix_2, q))



