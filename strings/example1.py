from collections import Counter

one = 'CoDe'
two = 'DeCo'

if Counter(one) == Counter(two):
    print('Анаграма найдена!')
else:
    print('Строки не совпадают')