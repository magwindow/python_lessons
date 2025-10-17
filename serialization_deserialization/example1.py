import datetime


class User:
    def __init__(self, email, password):
        self.email = email
        self.password = password
        self.created_at = datetime.datetime.now()

    def __str__(self):
        return f'{self.__class__}: email - {self.email}, created_at - {self.created_at}'


user = User(email='test@mail.ru', password='*****')
print(user)  # <class '__main__.User'>: email - test@mail.ru, created_at - 2025-10-17 16:29:37.435367
