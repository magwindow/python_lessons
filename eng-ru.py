'''
Англо - русский словарь
'''

dict = {
    "apple": "яблоко",
    "bold": "жирный",
    "bus": "автобус",
    "cat": "кошка",
    "саr": "машина"
}

print("=" * 15, "Англо - русский словарь", "=" * 15)

# Справка. Будет выведена по команде h
help_message = '''
s - Поиск
a - Добавить новое слово
r - Удалить слово
k - Показать все слова
d - Показать весь словарь
h - Справка
q - Выход
'''

choice = ""
while choice != "q":
    choice = input("(h - help)>> ")
    if choice == "s":
        word = input("Введите слово: ")
        res = dict.get(word, "He найдено!")
        print(res)
    elif choice == "a":
        word = input("Введите слово: ")
        value = input("Введите перевод: ")
        dict[word] = value
        print("Слово добавлено!")
    elif choice == "r":
        word = input("Введите слово: ")
        if word in dict:
            del dict[word]
            print("Слово удалено!")
        else:
            print("Такого слова нет!")
    elif choice == "k":
        print([i for i in dict.keys()])
    elif choice == "d":
        for word in dict:
            print(f"{word}: {dict[word]}")
    elif choice == "h":
        print(help_message)
    elif choice == "q":
        print("До свидания!")
    else:
        print("Нераспознанная команда. Введите h для справки")
    