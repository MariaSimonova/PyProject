# Создать текстовый файл (не программно), сохранить в нем несколько строк,
# выполнить подсчет количества строк, количества слов в каждой строке.

with open("text_1.txt", "r", encoding="utf-8") as f_str:
    content = f_str.readlines()
    print(f"Содержимое файла: {content}")
    print(f"Количество строк в файле: {len(content)}")

with open("text_1.txt", "r", encoding="utf-8") as f_str:
    for ind, i in enumerate(f_str, 1):
        i = len(i.split())
        print(f"В строке № {ind} - количество слов: {i}")
