# Задача 26:  Напишите программу, которая на вход принимает два числа A и B, 
# и возводит число А в целую степень B с помощью рекурсии.
# *Пример:*
# A = 3; B = 5 -> 243 (3⁵)
#     A = 2; B = 3 -> 8 

# result = 1
# a = int(input('print number a: '))
# b = int(input('print number b: '))

# for i in range(b):
#     if b > 0:
#         result = result * a
#         b -=1

# print(result)

def result (b):
    if b == 0:
        return 1
    elif b==1:
        return a
    return a * result(b-1)

a = int(input('print number a: '))
b = int(input('print number b: '))
print(result(b))