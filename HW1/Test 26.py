#Задача 26:  Посчитать факториал (произведение 1 до N) и треугольное число 
#(сумма чисел от 1 до N) для числа N ЧЕРЕЗ РЕКУРСИЮ и без циклов

def fact(num):
    if num == 1:
        return 1
    return fact(num - 1) * num

def fact(num):
    if num == 1:
        return 1
    return fact(num - 1) + num

num = int(input())
print(fact(num))