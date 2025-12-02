'''Работа с CSV-данными'''
import csv 

max = int(input("Сколько строк вывести из файла: "))
k = 0
with open("1.csv", "r") as f:
    f_csv = csv.reader(f)
    for row in f_csv:
        print(row)
        k += 1
        if k == max:
            break
       

