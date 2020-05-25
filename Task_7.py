from math import factorial


def fact(m):
    for el in range(1, m + 1):
        yield factorial(el)


while True:
    n = input("Enter the number. It can only be numbers - ")
    if n.isdigit():
        n = int(n)
        break
    else:
        continue

print(fact(n))

for el in fact(n):
    print(el)
