from itertools import count, cycle


def my_f(n_1, n_2):
    my_list = []
    try:
        n_1, n_2 = int(n_1), int(n_2)
    except ValueError:
        return "Parameters can only be numbers"
    for i in count(n_1):
        if i == n_2:
            break
        else:
            my_list.append(i)
    return my_list


def my_func(n_1, n_2):
    n_2 = int(n_2)
    z = 0
    for i in cycle(n_1):
        if z == n_2:
            break
        else:
            print(i)
            z += 1


n = input("Enter the number for start - ")
m = input("Enter the number for finish - ")
print(my_f(n, m))

my_list = my_f(n, m)
my_func(my_list, m)
