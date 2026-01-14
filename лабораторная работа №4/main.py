import math
from datetime import datetime
import my_module
from mypackage import multiply, shout

print("Квадратный корень из 25 =", math.sqrt(25))
print("Текущая дата и время:", datetime.now())
print("Результат сложения:", my_module.add(10, 20))
print("Тест умножения:", multiply(3, 4))
print("Тест строки:", shout("hello"))
