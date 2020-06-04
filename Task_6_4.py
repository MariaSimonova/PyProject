# Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты:
# speed, color, name, is_police (булево).
# А также методы: go, stop, turn(direction), которые должны сообщать,
# что машина поехала, остановилась, повернула (куда).
# Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
# Добавьте в базовый класс метод show_speed, который должен показывать
# текущую скорость автомобиля. Для классов TownCar и WorkCar переопределите
# метод show_speed. При значении скорости свыше 60 (TownCar) и 40 (WorkCar)
# должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов.
# Выполните доступ к атрибутам, выведите результат.
# Выполните вызов методов и также покажите результат.

from random import randint


class Car:
    def __init__(self, speed, color, name, is_police, direction):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police
        self.direction = direction

    def go(self):
        print(f"Машина {self.name} поехала")

    def stop(self):
        print(f"Машина {self.name} остановилась")

    def turn(self):
        if self.direction == "r":
            print(f"Машина {self.name} поворачивает направо")
        elif self.direction == "l":
            print(f"Машина {self.name} поворачивает налево")
        else:
            print(f"Машина {self.name} разворачивается")

    def show_speed(self):
        print(f"текущая скорость автомобиля: {self.speed}")


class TownCar(Car):
    def show_speed(self):
        print(f"текущая скорость автомобиля: {self.speed}")
        if self.speed > 60:
            print(f"текущая скорость для данного типа автомобиля превышает допустимое значение = 60")
        else:
            print(f"Данная скорость для этого типа автомобиля разрешена")


class WorkCar(Car):
    def show_speed(self):
        print(f"текущая скорость автомобиля: {self.speed}")
        if self.speed > 40:
            print(f"текущая скорость для данного типа автомобиля превышает допустимое значение = 40")
        else:
            print(f"Данная скорость для этого типа автомобиля разрешена")


class SportCar(Car):
    pass


class PoliceCar(Car):
    pass


def my_func(i):
    print(f"\n\nНазвание машины: {i.name}\nЦвет машины: {i.color}\nЭто полицейская машина: {i.is_police}")
    i.go()
    i.turn()
    i.show_speed()
    i.stop()


car_type = input("Укажите тип машины: TownCar, SportCar, WorkCar, PoliceCar - ")
speed = randint(0, 130)
direction = input(
    "Укажите направление машины:\nПоврот направо - нажмите 'r'\nПоврот налево - нажмите 'l'\nРазворот - нажмите 'u' ")

if car_type == "TownCar":
    t = TownCar(speed, "красный", "TownCar", False, direction)
    my_func(t)
elif car_type == "WorkCar":
    w = WorkCar(speed, "синий", "WorkCar", False, direction)
    my_func(w)
elif car_type == "SportCar":
    s = SportCar(speed, "желтый", "SportCar", False, direction)
    my_func(s)
else:
    p = PoliceCar(speed, "синий", "PoliceCar", True, direction)
    my_func(p)
