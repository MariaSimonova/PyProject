# Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение
# и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл.

from googletrans import Translator

translator = Translator()

with open("text_4.txt", "r", encoding="utf-8") as f_str:
    content = f_str.readlines()

result = []
for i in content:
    i = i.split()
    s = ((translator.translate(i[0], src='en', dest='ru')).text).title() + " " + i[1] + " " + i[2] + "\n"
    result.append(s)

with open("text_5.txt", "w", encoding="utf-8") as f_str:
    f_str.writelines(result)
