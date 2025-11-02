from collections import Counter

one = 'CoDe'
two = 'DeCo'

if Counter(one) == Counter(two):
    print('Анаграма найдена!')
else:
    print('Строки не совпадают')
    
    
print(len("how".encode('utf-8')))  # 3 bytes
print(len("как".encode('utf-8')))  # 6 bytes