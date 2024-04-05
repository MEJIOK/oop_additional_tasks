"""
Напишите класс User, имеющий следующие свойства и методы:

- __init__(self, name, password): конструктор, принимающий имя пользователя и пароль
- name: свойство, которое возвращает имя пользователя.
- password: свойство, которое позволяет установить или изменить пароль пользователя.
- is_admin: свойство, которое возвращает, является ли пользователь администратором или нет.
- _is_admin: свойство-помощник, которое определяет, является ли пользователь администратором или нет.
- login(self, password): метод, который проверяет, соответствует ли введенный пароль паролю пользователя.
- logout(self): метод, который выходит из аккаунта пользователя (устанавливает значение свойства _is_logged_in в False
при условии, что пользователь залогинен)

Для свойств name и password используйте декораторы @property и @password.setter.
"""


class User:

    def __init__(self, name: str, password: str):
        self.__name = name
        self.__password = password
        self._is_admin = False
        self._is_logged_in = False

    @property
    def name(self) -> str:
        return self.__name

    @property
    def password(self) -> str:
        return self.__password

    @password.setter
    def password(self, value) -> None:
        self.__password = value

    @property
    def is_admin(self) -> bool:
        return self._is_admin

    def login(self, password):
        self._is_logged_in = self.password == password
        return self._is_logged_in

    def logout(self) -> None:
        if not self._is_logged_in:
            raise Exception('User was not logged in.')
        self._is_logged_in = False


# код для проверки 
user1 = User("Alice", "qwerty")
print(user1.name)  # Alice
print(user1.password)  # qwerty
print(user1.is_admin)  # False

user1.password = "newpassword"
print(user1.password)  # newpassword

user1._is_admin = True
print(user1.is_admin)  # True

if user1.login("newpassword"):  # True
    print('User was logged in.')
    user1.logout()

users = [
    User('asd', 'qe'),
    User('eweq', '213'),
    User('qe', '123')
]

user_name_1 = 'asd'
user_name_2 = 'asd'
user_name_3 = 'asd'

user_names = [user_name_3, user_name_2, user_name_1]

for user in users:
    print('User ' + user.name)
