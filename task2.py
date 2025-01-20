# Откройте текстовый файл task2.txt для чтения.
# Считайте его содержимое в строку.
# Найдите и замените все вхождения слова "Python" на слово "Питон" (регистр учитывать).
# Запишите обновленный текст в новый файл с другим именем.
# Выведите на экран сообщение о количестве произведённых замен.
with open('task2.txt', 'r', encoding='utf-8') as file:
    string=file.read()
    count_Python=string.count('Python')
    print(count_Python)
    string=string.replace('Python', 'Питон', count_Python)
with open('task2.txt', 'w', encoding='utf-8') as file:
    file.write(string)

