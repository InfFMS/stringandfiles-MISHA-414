# Откройте текстовый файл для чтения task1.txt.
# Подсчитайте:
# Общее количество строк в файле.
# Общее количество слов во всем тексте файла.
# Общее количество символов (включая пробелы).
# Выведите полученную статистику на экран.
with open("task1.txt", 'r', encoding='utf-8') as f:
    f1=f.readlines()
    print(sum(1 for line in f1))
    print(sum(line.count(' ')-line.count('—') for line in f1))
    print(sum(len(line) for line in f1))
