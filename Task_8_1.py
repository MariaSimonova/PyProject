class Date:
    def __init__(self, text):
        self.text = text

    def __str__(self):
        return Date.validation(text)

    @classmethod
    def my_class_m(cls, param):
        my_list = param.split("-")
        for i in my_list:
            try:
                i = int(i)
                print(i)
            except ValueError:
                print("Только цифры!")

    @staticmethod
    def validation(text):
        ran_date = list(range(1, 31))
        ran_month = list(range(1, 13))
        ran_year = list(range(1, 9999))
        my_l = list(map(int, text.split("-")))
        if my_l[0] not in ran_date:
            return f"Ошибка ввода даты"
        elif my_l[1] not in ran_month:
            return f"Ошибка ввода месяца"
        elif my_l[2] not in ran_year:
            return f"Ошибка ввода года"
        else:
            return f"Валидация прошла успешно"


date = input("Введите дату в формате: «день-месяц-год».\nдень-месяц-год - должны быть указаны числами\n")
Date.my_class_m(date)
print(Date.validation(date))
