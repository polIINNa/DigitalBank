from abc import ABC, abstractmethod


class SystemUser(ABC):

    @abstractmethod
    def __init__(self, f_name: str, l_name: str, age: int, login: str, password: str):
        self._f_name = f_name
        self._l_name = l_name
        self._age = age
        self._login = login
        self._password = password

    @property
    def login(self):
        return self._login

    @login.setter
    def login(self, new_login):
        self._login = new_login

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, new_password):
        self._password = new_password

    def change_password(self, old_password, new_password):
        if self.password == old_password:
            self.password = new_password
            

class DigitalWallet:
    def __init__(self):
        self._balance = 0

    @property
    def balance(self):
        return self._balance

    def deposit_money(self, val):
        """
        фунция для внесения суммы на электронный кошелек
        :param val: сумма пополнения
        :return: None
        """
        self._balance += val

    def withdraw_money(self, val):
        """
        функция для списания суммы с электронного кошелька
        :param val: сумма списания
        :return: None
        """
        if val <= self._balance:
            self._balance -= val


class User(SystemUser, DigitalWallet):
    def __init__(self, f_name: str, l_name: str, age: int, login: str, password: str):
        SystemUser.__init__(self, f_name=f_name, l_name=l_name, age=age, login=login, password=password)
        self._wallet = DigitalWallet()

    def __str__(self):
        return self._f_name + ' ' + self._l_name + ' ' + str(self._age)

    @property
    def wallet(self):
        return self._wallet


class Admin(SystemUser, DigitalWallet):
    def __init__(self, f_name: str, l_name: str, age: int, login: str, password: str):
        SystemUser.__init__(self, f_name=f_name, l_name=l_name, age=age, login=login, password=password)

    def __str__(self):
        return self._f_name + ' ' + self._l_name

    @staticmethod
    def get_user_info(usr: User):
       return str(usr), usr._login, usr._password

    @staticmethod
    def get_user_wallet(usr: User):
        """
        метод позволяет проводить все возможные операции с электронным кошелком пользователя
        :param usr: экземпляр класса User (пользователь)
        :return: электронный колшелек пользователя
        """
        return usr.wallet


        
