# Реализовать класс Stationery (канцелярская принадлежность).
# Определить в нем атрибут title (название) и метод draw (отрисовка).
# Метод выводит сообщение “Запуск отрисовки.”
# Создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер).
# В каждом из классов реализовать переопределение метода draw.
# Для каждого из классов метод должен выводить уникальное сообщение.
# Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.

class Stationery:
    title = ""

    def draw(self):
        print("Запуск отрисовки.")


class Pen(Stationery):
    def draw(self):
        Stationery.title = "Pen"
        print(f"Отрисовка с помощью {Stationery.title}")


class Pencil(Stationery):
    def draw(self):
        Stationery.title = "Pencil"
        print(f"Отрисовка с помощью {Stationery.title}")


class Handle(Stationery):
    def draw(self):
        Stationery.title = "Handle"
        print(f"Отрисовка с помощью {Stationery.title}")


s = Stationery()
s.draw()
p = Pen()
p.draw()
pn = Pencil()
pn.draw()
h = Handle()
h.draw()
