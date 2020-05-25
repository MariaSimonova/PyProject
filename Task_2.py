n = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]

print([i for i in n if i > n[n.index(i) - 1] and i != n[0]])
