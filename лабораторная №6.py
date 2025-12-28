

#Задание 1


class UserAccount:
    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.__password = password  
    def set_password(self, new_password):
        if len(new_password) >= 8:
            self.__password = new_password
            print("Пароль успешно изменён.")
        else:
            print("Ошибка (пароль должен содержать минимум 8 символов)")

    def check_password(self, password):
        return self.__password == password


print("Создание аккаунта")
username = input("Введите имя пользователя: ")
email = input("Введите email: ")
password = input("Придумайте пароль (минимум 8 символов): ")

user = UserAccount(username, email, password)

print("Проверка пароля")
check = input("Введите пароль для проверки: ")
if user.check_password(check):
    print("Пароль верный!")
else:
    print("Неверный пароль!")

print("Смена пароля")
new_password = input("Введите новый пароль: ")
user.set_password(new_password)

print("Повторная проверка пароля")
check2 = input("Введите новый пароль для проверки: ")
if user.check_password(check2):
    print("Новый пароль подтверждён!")
else:
    print("Ошибка! Новый пароль введён неверно!")



#Задание 2

class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def get_info(self):
        return f"Марка: {self.make}, Модель: {self.model}"


class Car(Vehicle):
    def __init__(self, make, model, fuel_type):
        super().__init__(make, model)
        self.fuel_type = fuel_type

    def get_info(self):
        return f"Марка: {self.make}, Модель: {self.model}, Тип топлива: {self.fuel_type}"


print("Создание транспорта")
make = input("Введите марку автомобиля: ")
model = input("Введите модель автомобиля: ")
fuel = input("Введите тип топлива: ")

car = Car(make, model, fuel)

print("Информация об автомобиле:")
print(car.get_info())
