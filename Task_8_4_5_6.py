class Storage:
    def __init__(self, name=None, model=None, amount=0, price=0, i=0):
        self.name = name
        self.model = model
        self.amount = amount
        self.price = price
        self.i = i
        self.storage = {self.i: [["название", self.name], ["модель", self.model], ["количество", self.amount],
                                 ["цена", self.price]]}

    def Item(self, name, model, amount, price, i):
        return self.storage

    def Status(self, products):
        self.products = products
        print(f"Состояние на складе: {self.products}")


class Technique:
    def __init__(self, name=None, model=None, amount=0, price=0):
        self.name = name
        self.model = model
        self.amount = amount
        self.price = price


class Printer(Technique):
    def Status(self, products):
        self.products = products
        print(f"Состояние подразделения 'Принтеры': {self.products}")


class Scanner(Technique):
    def Status(self, products):
        self.products = products
        print(f"Состояние подразделения 'Сканеры': {self.products}")


class Xerox(Technique):
    def Status(self, products):
        self.products = products
        print(f"Состояние подразделения 'Ксероксы': {self.products}")


def validation(param):
    try:
        i = int(param)
    except ValueError:
        print("Должно быть число")
        add_product()


def add_product():
    while True:
        i = input("Введите ID товара: ")
        validation(i)
        n = input("Введите название товара: ")
        m = input("Введите модель товара: ")
        p = input("Введите цену товара: ")
        validation(p)
        q = input("Введите количество товара: ")
        validation(q)
        g = input("Хотите продолжить? Если Да - Y, если Нет - N")
        s = Storage(n, m, p, q, i)
        my_list.append(s.Item(n, m, p, q, i))
        if g == "N":
            break
        else:
            continue
    return s.Status(my_list)


my_list = []
my_list_p = []
my_list_sc = []
my_list_x = []
while True:
    act = int(input(
        "Что вы хотите сделать:\n1 - добавить товар\n2 - переместить товар\n3 - посмотреть состояние\n4 - завершить работу\n"))
    if act == 4:
        break
    elif act == 1:
        print(add_product())
    elif act == 2:
        n = int(input("Укажите ID  товара для перемещенияя - "))
        m = int(input("Куда переместить:\n1 - в Принтеры\n2 - в Сканеры\n3 - в Ксероксы\n"))
        if m == 1:
            p = Printer()
            for item in my_list:
                j = list(item.keys())
                if j[0] == n:
                    a = my_list.pop(my_list.index(item))
                    my_list_p.append(a)
            print(p.Status(my_list_p))
        elif m == 2:
            sc = Scanner()
            for item in my_list:
                j = list(item.keys())
                if j[0] == n:
                    a = my_list.pop(my_list.index(item))
                    my_list_sc.append(a)
            print(sc.Status(my_list_sc))
        else:
            x = Xerox()
            for item in my_list:
                j = list(item.keys())
                if j[0] == n:
                    a = my_list.pop(my_list.index(item))
                    my_list_x.append(a)
            print(x.Status(my_list_x))
    else:
        s = Storage()
        s.Status(my_list)
        p = Printer()
        p.Status(my_list_p)
        sc = Scanner()
        sc.Status(my_list_sc)
        x = Xerox()
        x.Status(my_list_x)
