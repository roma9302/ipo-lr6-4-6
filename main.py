"""
Написать программу, которая:
- Создаёт случайный список из 20 значений по 4 случайных целых чисел от -10 до 10.
- Находит все уникальные комбинации пар из этих значений и выводит их в виде списка кортежей.
- Пользователь вводит целое число.
- Вычисляет количество пар, чья сумма меньше заданного пользователем значения.
"""
import random 

#списки хранения данных
unique=[]
list2=[]

#счетчик 
counter=0

#ввод с клавиатуры
number=int(input("Введите число"))

#генератор комбинаций
for i in range(0,20):
 list1=[random.randint(-10,10) for x  in range(4)]
 list2.append(list1)
 for i in list2:
   if i not in unique:
    unique.append(i)
#проверка суммы
    if sum(i)<number:
     counter+=1
#вывод результатов
print(f"уникальные значения {tuple(unique)}")
print(f"счетчик комбинаций,чья сумма меньше,чем число пользователя {counter}")
