# Задача 10: 
# На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. 
# Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были
# повернуты вверх одной и той же стороной. Выведите минимальное количество монет, которые 
# нужно перевернуть.
# 5 -> 1 0 1 1 0
# 2

# ВАРИАНТ 1
# вводим общее количество монет
from random import randint
n = int(input('Введите количество монеток: '))
orel = 0
reshka = 0
count = 0
# собрали рандомное число из заданного количества монет
for i in range(n):
     x = randint(0, 1)
     print(x, end=' ')
     if x == 1:
         orel += 1   
     else:
         reshka += 1
if orel > reshka:
    print(f'Минимальное количество монет {reshka} , которые нужно перевернуть')
else:
    print(f'Минимальное количество монет {orel} , которые нужно перевернуть')
if reshka == orel:
 print(f'Количество орлов и решек одинаково, по {reshka} штук')





# Задача 12: 
# Петя и Катя – брат и сестра. Петя – студент, а Катя –школьница. Петя помогает Кате по 
# математике. Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. 
# Для этого Петя делает две подсказки. Он называет сумму этих чисел S и их произведение P. 
# Помогите Кате отгадать задуманные Петей числа.
# 4 4 -> 2 2
# 5 6 -> 2 3

# s, p = map(int,input('Введите сумму и произведение чисел через пробел:  ').split())
# diskrim= s**2-4*p
# # print(int(diskrim**0.5))

# x1=0
# x2=0
# while diskrim > 0:
#     x1= int((s-diskrim**0.5)//2)
#     print(x1)
#     x2= int((s+diskrim**0.5)//2)
#     print(x2)
#     break


# Задача 14: 
# Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.
# 10 -> 1 2 4 8

# n = int(input('Enter a number '))
# k = 1
# res = 0
# while k < n:
#     res = pow(2,k)
#     print(k)    
#     k *= 2
 
# n = int(input('Enter a number '))
# k = 1
# res = 0
# while k < n:
#     res = 2**k
#     print(k)    
#     k *= 2
# # Эталонное решение   
# n = int(input())
# i = 0
# while 2 ** i <= n:
#     print(2 ** i)
#     i += 1
