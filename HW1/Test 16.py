#Задача 16: Требуется вычислить, сколько раз встречается некоторое число X в массиве 
#A[N]. Пользователь в первой строке вводит натуральное число N – количество
#элементов в массиве. В последующих  строках записаны N целых чисел Ai. 
#Последняя строка содержит число X

n = int(input())
list_1 = list()
for i in range(n):
    x = int(input())
    list_1.append(x)

count = 0
a = int(input())
for i in range(len(list_1)):
    if list_1[i] == a:
        count += 1
print(count)