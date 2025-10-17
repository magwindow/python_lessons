import datetime
import json


class User:
    def __init__(self, email, password):
        self.email = email
        self.password = password
        self.created_at = datetime.datetime.now()

    def __str__(self):
        return f'{self.__class__}: email - {self.email}, created_at - {self.created_at}'


user = User(email='test@mail.ru', password='*****')
json_user = json.dumps({
    'email': user.email,
    'password': user.password
})
print(json_user)  # {"email": "test@mail.ru", "password": "*****"}

