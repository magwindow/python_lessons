print("*" * 10, " Калькулятор ", "*" * 10)
print("Для выхода введите q в качестве знака операции")

while True:
    s = input("Знак (+ - * /): ")
    if s == 'q': 
        break
    if s in ('+', '-', '*', '/'):
        x = float(input("x = "))
        y = float(input("y = "))
        if s == '+':
            print(f"{x + y:.2f}")
        elif s == '-':
            print(f"{x - y:.2f}")
        elif s == '*':
            print(f"{x * y:.2f}")
        elif s == '/':
            if y != 0:
                print(f"{x / y:.2f}")
            else:
                print("Деление на ноль!")
    else:
        print("Неверный знак операции!")