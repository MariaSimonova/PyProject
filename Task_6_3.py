# Реализовать базовый класс Worker (работник), в котором определить атрибуты:
# name, surname, position (должность), income (доход).
# Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы:
# оклад и премия, например, {"wage": wage, "bonus": bonus}.
# Создать класс Position (должность) на базе класса Worker.
# В классе Position реализовать методы получения полного имени сотрудника (get_full_name)
# и дохода с учетом премии (get_total_income).
# Проверить работу примера на реальных данных
# (создать экземпляры класса Position, передать данные, проверить значения атрибутов,
# вызвать методы экземпляров).

class Worker:
    def __init__(self, name, surname, position, income):
        self.name = name
        self.surname = surname
        self.position = position
        self.income = income
        print(f"Значения атрибутов: name = {name} surname = {surname} position = {position} income = {income}")


class Position(Worker):
    def __init__(self, name, surname, position, income):
        super().__init__(name, surname, position, income)

    def get_full_name(self):
        print(f"Полное имя сотрудника: {self.surname} {self.name}")

    def get_total_income(self):
        print(f"Доход сотрудника: {sum(self.income.values())}")


surname = input("Введите фамилию сотрудника - ")
name = input("Введите имя сотрудника - ")
position = input("Введите должность сотрудника - ")
wage = float(input("Введите оклад сотрудника - "))
bonus = float(input("Введите премию сотрудника - "))
income = {"wage": wage, "bonus": bonus}

employee = Position(name, surname, position, income)
employee.get_full_name()
employee.get_total_income()
