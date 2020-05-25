from functools import reduce


def my_f(n_1, n_2):
    return n_1 * n_2


n = [i for i in range(100, 1001, 2)]

print(n)
print(reduce(my_f, n))
