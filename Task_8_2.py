class OwnError(Exception):
    def __init__(self, p_1, p_2=0):
        self.p_1 = p_1
        self.p_2 = p_2


n = input("Введите число 1: ")
m = input("Введите число 2: ")

try:
    n = int(n)
    m = int(m)
    if m == 0:
        raise OwnError("Число 2 НЕ может быть = 0!")
except ValueError:
    print("Вы ввели не число")
except OwnError as err:
    print(err)
else:
    print(f"Результат деления числа 1 на число 2: {n / m}")
