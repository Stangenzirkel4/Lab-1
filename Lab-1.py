#Импортируем необходимое
import csv


#Объявляем переменные
count30 = 0     #Счетчик всех записей
countall = 0    #Счетчик всех записей с названием > 30 символов

#Открываем на чтение
with open('books.csv') as f:
    reader = csv.DictReader(f, delimiter=';')

    for row in reader:
        #Считаем все
        countall += 1

        #Считаем длинное
        if len(row.get("Название")) > 30:
            count30 += 1

print("Всего записей:", countall)
print("Всего записей, у которых в поле 'Название' строка длиннее 30 символов:", count30)

