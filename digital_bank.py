from abc import ABC, abstractmethod


class SystemUser(ABC):
    @abstractmethod
    def __init__(self, f_name: str, l_name: str, age: int, login: str, password: str):
        self.f_name = f_name
        self.l_name = l_name
        self.age = age
        self.login = login
        self.password = password


class DigitalWallet:
    def __init__(self):
        self.balance = 0

    def get_balance(self):
        return self.balance

    def deposit_money(self, val):
        self.balance += val

    def withdraw_money(self, val):
        if val <= self.balance:
            self.balance -= val


class User(SystemUser, DigitalWallet):
    def __init__(self, f_name, l_name, age, login, password):
        SystemUser.__init__(self, f_name=f_name, l_name=l_name, age=age, login=login, password=password)
        self.wallet = DigitalWallet()

    def __str__(self):
        return self.f_name + ' ' + self.l_name


user = User('Polina', 'Rebrova', 21, 'qwerty', '123')
print(str(user))
user.wallet.deposit_money(1000)
user.wallet.withdraw_money(600)
print(user.wallet.get_balance())


class Admin(SystemUser):
    def __init__(self, f_name, l_name, age, login, password):
        SystemUser.__init__(self, f_name=f_name, l_name=l_name, age=age, login=login, password=password)

    def __str__(self):
        return self.f_name + ' ' + self.l_name

    @staticmethod
    def get_user_info(usr: User):
       return str(usr), usr.login, usr.password

    @staticmethod
    def get_user_wallet(usr: User):
        return usr.wallet.get_balance()
