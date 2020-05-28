# Создать текстовый файл (не программно),
# построчно записать фамилии сотрудников и величину их окладов
# (не менее 10 строк). Определить, кто из сотрудников имеет оклад менее 20 тыс.,
# вывести фамилии этих сотрудников. Выполнить подсчет средней величины дохода сотрудников.
# Пример файла:
# Иванов 23543.12
# Петров 13749.32

with open("text_3.txt", "r", encoding="utf-8") as f_str:
    content = f_str.readlines()

content_len = len(content)
surnames = []
salaris = []
for i in content:
    i = i.split()
    s = float(i[1])
    salaris.append(s)
    if s < 20000.0:
        surnames.append(i[0])

print(f"Сотрудники с окладом менее 20 тыс.: {surnames}")
print(f"Средняя величина дохода сотрудников: {sum(salaris) / content_len}")
