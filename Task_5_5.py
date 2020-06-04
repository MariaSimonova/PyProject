# Создать (программно) текстовый файл, записать в него
# программно набор чисел, разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.

start_list = [i * 2 for i in range(5, 10)]
sum = sum(start_list)
m_str = []

for i in start_list:
    m_str.append((str(i) + " "))
print(f"Сумма всех чисел в файле = {sum}")

with open("text_55.txt", "w", encoding="utf-8") as f_str:
    f_str.writelines(m_str)

with open("text_55.txt", "a", encoding="utf-8") as f_str:
    f_str.write(f"\n\nСумма всех чисел = {sum}")
