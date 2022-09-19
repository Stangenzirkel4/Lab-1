#Импортируем необходимое
import csv


#Объявляем переменные
count30 = 0     #Счетчик всех записей
countall = 0    #Счетчик всех записей с названием > 30 символов

print("Введите искомого автора")
author = input()    #Имя искомого автора

#Открываем на чтение
with open('books.csv') as f:
    reader = csv.DictReader(f, delimiter=';')

    for row in reader:
        #Считаем все
        countall += 1

        #Считаем длинное
        if len(row.get("Название")) > 30:
            count30 += 1

        #Выполняем поиск по автору
        if author == row.get("Автор"):
            if int(row.get("Дата поступления")[:4]) >= 2018:
                print(row)

print("Всего записей:", countall)
print("Всего записей, у которых в поле 'Название' строка длиннее 30 символов:", count30)
