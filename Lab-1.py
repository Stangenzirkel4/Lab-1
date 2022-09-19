#Импортируем необходимое
import csv
import random


#Объявляем переменные
count30 = 0     #Счетчик всех записей
countall = 0    #Счетчик всех записей с названием > 30 символов
choice = [] #Список для записи выборки по запросу пользователя

print("Введите искомого автора")
author = input()    #Имя искомого автора

print("Введите параметр поиска (или '-', если хотите получить случайную выборку")
wantedKey = input()
if wantedKey != "-":
    print("Введите значение параметра поиска")
    wantedValue = input()

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

        #Пополняем выборку по запросу пользователя
        if len(choice) < 20:
            if wantedKey != "-":
                if row.get(wantedKey) == wantedValue:
                    choice.append(row.get("Автор") + '. "' + row.get("Название") + '" - ' + row.get("Дата поступления")[:4])
            else:
                if int(row.get("ID")) % 100 == random.randint(0, 99):
                    choice.append(row.get("Автор") + '. "' + row.get("Название") + '" - ' + row.get("Дата поступления")[:4])


print("Всего записей:", countall)
print("Всего записей, у которых в поле 'Название' строка длиннее 30 символов:", count30)

#Сохраняем 20 книг по запросу
file = open("User's choice.txt", "w")

n = 0 #Номер строки в записываемом файле
for i in choice:
    n += 1
    file.write(str(n)+". "+str(i)+"\n")
file.close()
