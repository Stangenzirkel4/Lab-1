#Импортируем необходимое
import csv
import random

#Объявляем переменные
count30 = 0     #Счетчик всех записей
countall = 0    #Счетчик всех записей с названием > 30 символов
choice = [] #Список для записи выборки по запросу пользователя
tags_set = set()    #Множество тегов
publishers_set = set()  #Множество издателей (для books-en)
bestbooks = [{"Кол-во выдач":-1}]*20

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
            if int(row.get("Дата поступления")[6:10]) >= 2018:
                print(row)

        #Пополняем выборку по запросу пользователя
        if len(choice) < 20:
            if wantedKey != "-":
                if row.get(wantedKey) == wantedValue:
                    choice.append(row.get("Автор") + '. "' + row.get("Название") + '" - ' + row.get("Дата поступления")[6:10])
            else:
                if int(row.get("ID")) % 100 == random.randint(0, 99):
                    choice.append(row.get("Автор") + '. "' + row.get("Название") + '" - ' + row.get("Дата поступления")[6:10])

        #Пополняем множество тегов
        currenttags = row.get("Жанр книги").split("# ")
        for i in currenttags:
            tags_set.add(i)

        #Ищем 20 самых популярных книг
        for i in range(len(bestbooks)):
            if int(row.get("Кол-во выдач")) > int(bestbooks[i].get(("Кол-во выдач"))):
                bestbooks.insert(i,row)
                bestbooks.pop()
                break


with open('books-en.csv') as f:
    reader = csv.DictReader(f, delimiter=';')
    for row in reader:
        publishers_set.add(row.get("Publisher"))



#Выводим значения счетчиков
print("Всего записей:", countall)
print("Всего записей, у которых в поле 'Название' строка длиннее 30 символов:", count30)

#Сохраняем 20 книг по запросу
file = open("User's choice.txt", "w")

n = 0 #Номер строки в записываемом файле
for i in choice:
    n += 1
    file.write(str(n)+". "+str(i)+"\n")
file.close()

#Сохраняем множество тегов
file = open("List of tags.txt", "w")
for i in sorted(tags_set):
    file.write(i+"\n")
file.close()

#Сохраняем множество издателей
file = open("List of publishers.txt", "w")
for i in sorted(publishers_set):
    file.write(i+"\n")
file.close()

#Сохраняем 20 самых популярных книг
with open('Bestsellers.csv', 'w', newline='') as csvfile:
    fieldnames = ['ID','Название','Тип','Автор','Автор (ФИО)','Возрастное ограничение на книгу','Дата поступления','Цена поступления','Кол-во выдач','Дата списания книги','Инвентарный номер','Выдана до','Жанр книги']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for i in bestbooks:
        writer.writerow(i)


