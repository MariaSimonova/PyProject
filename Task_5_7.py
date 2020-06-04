# Необходимо построчно прочитать файл, вычислить прибыль каждой компании,
# а также среднюю прибыль. Если фирма получила убытки, в расчет средней прибыли ее не включать.
# Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями,
# а также словарь со средней прибылью. Если фирма получила убытки, также добавить ее в словарь
# (со значением убытков).
# Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
# Итоговый список сохранить в виде json-объекта в соответствующий файл.
# Пример json-объекта:
# [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]

key_lst = []
value_lst = []
m_profit = []

with open("text_7.txt", "r", encoding="utf-8") as f_str:
    content_1 = f_str.readlines()

len_1 = len(content_1)

with open("text_7.txt", "r", encoding="utf-8") as f_str:
    while len_1 != 0:
        content_2 = f_str.readline()
        content_2 = content_2.split()
        for i in content_2:
            if content_2.index(i) == 0:
                key_lst.append(i)
            else:
                profit = int(content_2[2]) - int(content_2[3])
        value_lst.append(profit)
        my_dict = dict(zip(key_lst, value_lst))
        if profit > 0:
            m_profit.append(profit)
        sum_profits = sum(m_profit)
        len_1 = len_1 - 1

len_m_profits = len(m_profit)
average_p = sum_profits / len_m_profits
average_profit = {"average_profit": average_p}

list = [my_dict, average_profit]
print(list)

import json

with open("text_78.json", "w", encoding="utf-8") as f_str:
    json.dump(list, f_str, sort_keys=True, indent=2, ensure_ascii=False)
