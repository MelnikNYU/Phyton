#Требуется найти в массиве A[N] самый близкий по величине элемент к заданному
#числу X. Пользователь в первой строке вводит натуральное число N – 
#количество элементов в массиве. В последующих  строках записаны N целых 
#чисел Ai. Последняя строка содержит число X

n = int(input())
list_1 = list()
for i in range(n):
    x = int(input())
    list_1.append(x)

a = int(input())
b = abs(a - list_1[0])
num = list_1[0]
for i in range(1, len(list_1)):
    if b > abs(list_1[i] - a):
        b = abs(list_1[i] - a)
        num = list_1[i]
print(num) 