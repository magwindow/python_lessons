names = input('Введите фамилии участников через запятую:\n')

list_names = names.split(',')
list_names.sort()

n = len(list_names)

print('\nОбщий список участников:')
for i in range(len(list_names)):
    print(i+1, list_names[i])
    
k = int(input('\nВведите количество участников в подгруппе: '))
while k < 1:
    print('Некорректный ввод')
    k = int(input('\nВведите количество участников в подгруппе: '))
    
list_groups = []
    
if n//k == n/k:
    for i in range(n//k):
        list_groups.append([])
        for j in range(k):
            list_groups[i].append(list_names[0])
            del list_names[0]
        
    for i in range(len(list_groups)):
        print('\nПодгруппа ', i+1)
        for j in range(k):
            print(list_groups[i][j])
else:
    for i in range(n//k):
        list_groups.append([])
        for j in range(k):
            list_groups[i].append(list_names[0])
            del list_names[0]
    list_groups.append([])
    list_groups[-1] = list_names
        
    for i in range(len(list_groups)-1):
        print('\nПодгруппа ', i+1)
        for j in range(k):
            print(list_groups[i][j])   
                
    print('\nРезерв:')
    for i in range(len(list_groups[-1])):
        print(list_groups[-1][i])     