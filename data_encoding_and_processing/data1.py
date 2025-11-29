'''Консервация данных'''
# import pickle 

# first_name = ["Оля", "Вася", "Коля"]
# last_name = ["Петрова", "Пупкин", "Смирнов"]

# Запись в файл
# datafile = open("names.data", "wb")
# pickle.dump(first_name, datafile)
# pickle.dump(last_name, datafile)
# datafile.close()

# Чтение данных
# datafile = open("names.data", "rb")
# first_name = pickle.load(datafile)
# last_name = pickle.load(datafile)
# datafile.close()
# print(first_name)
# print(last_name)
'''###################################################################'''

'''Произвольный доступ к законсервированным данным'''
# import shelve 

# Запись в файл
# s = shelve.open("names2.dat")
# s["first_name"] = ["Оля", "Вася", "Коля"]
# s["last_name"] = ["Петрова", "Пупкин", "Смирнов"]
# s.sync()
# s.close()

# Чтение данных
# s = shelve.open("names2.dat")
# print(s["first_name"])
# print(s["last_name"])
# s.close()