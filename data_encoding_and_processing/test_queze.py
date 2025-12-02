import pickle 

# questions = [
#     '''
#     Компания-разработчик Windows
#     1) Mikrosoft
#     2) Melkosoft
#     3) Cybersoft
#     4) Microsoft
#     ''',
#     '''
#     Самая "яблочная" операционная система
#     1) AppleOS
#     2) Linux
#     3) macOS
#     4) FreeBSD
#     ''',
#     '''
#     Символом какой операционной системы является пингвин
#     1) Linux
#     2) FreeBSD
#     3) OS/2
#     4) Windows
#     ''',
#     '''
#     Сколько бит в одном байте
#     1) 8
#     2) б
#     3) 4
#     4) 2
#     '''
#     '''
#     Сколько байт в одном килобайте
#     1) 1000
#     2) 1024
#     3) 1048
#     4) 256
#     '''
# ]

# answers = [4,3,1,2]

# datafile = open("test.dat", "wb")
# pickle.dump(questions, datafile)
# pickle.dump(answers, datafile)
# datafile.close()

mark = 0

# Загружаем списки вопросов и ответов
try:
    datafile = open("test.dat", "rb")
except:
    print('Ошибка при загрузке вопросов!')
else:
    questions = pickle.load(datafile)
    answers = pickle.load(datafile)
    datafile.close()
    n = len(answers)  # К-во вопросов и ответов
    i = 0
    for i in range(n):
        print(questions[i])
        try:
            a = int(input("Ваш ответ: "))
            if a == answers[i]:
                mark += 1
                print("Правильно 😊")
            else:
                print("Неправильно 😞")
        except:
            print("Нужно было ввести число. Ответ засчитан как неправильный!")
    print(f"Вы правильно ответили на {mark} вопросов из {n}")
    