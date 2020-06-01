# Сформировать словарь, содержащий название предмета и общее количество занятий по нему.
# Вывести словарь на экран.
# Примеры строк файла: Информатика:   100(л)   50(пр)   20(лаб).
#                                         Физика:   30(л)   —   10(лаб)
#                                         Физкультура:   —   30(пр)   —
# Пример словаря: {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}


key_lst = []
value_lst_sum = []

with open("text_6.txt", "r", encoding="utf-8") as f_str:
    content = f_str.readlines()

for i in content:
    q = i.split()
    value_lst = []
    for k in q:
        if q.index(k) == 0:
            key_lst.append(k[:-1])
        elif k != '-':
            try:
                value_lst.append(int(k[:2]))
            except ValueError:
                value_lst.append(int(k[:1]))
    value_lst_sum.append(sum(value_lst))

my_dict = dict(zip(key_lst, value_lst_sum))
print(my_dict)
