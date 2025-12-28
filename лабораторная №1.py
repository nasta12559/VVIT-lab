#1 задание
while True:
     try:
          f = int(input("Введите число:",))
          break
     except ValueError:
          print('не правильно,пиши цифрами')
for m in range(1, f+1):
    print(m)

#2 задание

number1 = float(input("введите первое число:"))
number2 = float(input("введите второе число:"))
if number1 > number2:
    print(number1)
elif number2 > number1:
    print(number2)
else:
    print("числа равны:", number1)
