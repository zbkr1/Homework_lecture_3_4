# """ Вычислить число c заданной точностью d. 
# # # Пример: при d = 0.001,π = 3.141   10^(-1)≤d≤10^(-10)"""

# # from math import pi

# # d =  int(input("Введите число для заданной точности числа Пи:\n"))
# # print(f'число Пи с заданной точностью {d} равно {round(pi, d)}')



# """Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N."""

# def check_number_simple(n: int):
#     i = 2
#     while n % i != 0 or i == n - 1:
#         i += 1
#     if i == n:
#         return n

# def fill_simple_list(n: int) -> list:
#     simple_list = [1]
#     for i in range(2, n+1):
#         if n % i == 0:
#             if check_number_simple(i) != None:
#                 simple_list.append(check_number_simple(i))
#             else:
#                 continue
#     return simple_list

# n = int(input('Введите натуральное число N: '))
# simple_list = fill_simple_list(n)
# print(simple_list)

# """Задайте последовательность чисел. Напишите программу, которая выведет список 
# неповторяющихся элементов исходной последовательности."""

# import random

# def fill_number_list(n=20, min=10, max=99) -> list:
#     number_list = [random.randint(min, max)]
#     for i in range (1, n):
#         number_list.append(random.randint(min, max)) 
#     return number_list

# def unique_values_list(user_list) -> list:
#     new_list = [user_list[0]]
#     for i in range(1, len(user_list)):
#         for j in range(len(new_list)):
#             if user_list[i] == new_list[j]:
#                 break
#             elif j == len(new_list)-1:
#                 new_list.append(user_list[i])
#     return new_list

# source_list = fill_number_list(20, 10, 50)
# unique_list = unique_values_list(source_list)
# print(f'{source_list} ->')
# print(unique_list)


# """Задана натуральная степень k. 
# Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k. 
# Пример:
# k=2 => 2x² + 4x + 5 = 0 или x² + 5 = 0 или 10*x² = 0"""

# import random

# def write_file(st):
#     with open('file_1.txt', 'w') as data:
#         data.write(st)

# def rnd():
#     return random.randint(0,101)

# def create_mn(k):
#     lst = [rnd() for i in range(k+1)]
#     return lst   

# def create_str(sp):
#     lst= sp[::-1]
#     wr = ''
#     if len(lst) < 1:
#         wr = 'x = 0'
#     else:
#         for i in range(len(lst)):
#             if i != len(lst) - 1 and lst[i] != 0 and i != len(lst) - 2:
#                 wr += f'{lst[i]}x^{len(lst)-i-1}'
#                 if lst[i+1] != 0:
#                     wr += ' + '
#             elif i == len(lst) - 2 and lst[i] != 0:
#                 wr += f'{lst[i]}x'
#                 if lst[i+1] != 0:
#                     wr += ' + '
#             elif i == len(lst) - 1 and lst[i] != 0:
#                 wr += f'{lst[i]} = 0'
#             elif i == len(lst) - 1 and lst[i] == 0:
#                 wr += ' = 0'
#     return wr

# k = int(input("Введите натуральную степень k = "))
# koef = create_mn(k)
# write_file(create_str(koef))


# """Даны два файла, в каждом из которых находится запись многочлена. 
# Задача - сформировать файл, содержащий сумму многочленов."""

# import random

# # запись в файл
# def write_file(name,st):
#     with open(name, 'w') as data:
#         data.write(st)

# # создание случайного числа от 0 до 100
# def rnd():
#     return random.randint(0,101)

# # создание коэффициентов многочлена
# def create_mn(k):
#     lst = [rnd() for i in range(k+1)]
#     return lst
    
# # создание многочлена в виде строки 
# def create_str(sp):
#     lst= sp[::-1]
#     wr = ''
#     if len(lst) < 1:
#         wr = 'x = 0'
#     else:
#         for i in range(len(lst)):
#             if i != len(lst) - 1 and lst[i] != 0 and i != len(lst) - 2:
#                 wr += f'{lst[i]}x^{len(lst)-i-1}'
#                 if lst[i+1] != 0 or lst[i+2] != 0:
#                     wr += ' + '
#             elif i == len(lst) - 2 and lst[i] != 0:
#                 wr += f'{lst[i]}x'
#                 if lst[i+1] != 0 or lst[i+2] != 0:
#                     wr += ' + '
#             elif i == len(lst) - 1 and lst[i] != 0:
#                 wr += f'{lst[i]} = 0'
#             elif i == len(lst) - 1 and lst[i] == 0:
#                 wr += ' = 0'
#     return wr

# # получение степени многочлена
# def sq_mn(k):
#     if 'x^' in k:
#         i = k.find('^')
#         num = int(k[i+1:])
#     elif ('x' in k) and ('^' not in k):
#         num = 1
#     else:
#         num = -1
#     return num

# # получение коэффицента члена многочлена
# def k_mn(k):
#     if 'x' in k:
#         i = k.find('x')
#         num = int(k[:i])
#     return num

# # разбор многочлена и получение его коэффициентов
# def calc_mn(st):
#     st = st[0].replace(' ', '').split('=')
#     st = st[0].split('+')
#     lst = []
#     l = len(st)
#     k = 0
#     if sq_mn(st[-1]) == -1:
#         lst.append(int(st[-1]))
#         l -= 1
#         k = 1
#     i = 1 # степень
#     ii = l-1 # индекс
#     while ii >= 0:
#         if sq_mn(st[ii]) != -1 and sq_mn(st[ii]) == i:
#             lst.append(k_mn(st[ii]))
#             ii -= 1
#             i += 1
#         else:
#             lst.append(0)
#             i += 1
        
#     return lst
    


# # создание двух файлов

# k1 = int(input("Введите натуральную степень для первого файла k = "))
# k2 = int(input("Введите натуральную степень для второго файла k = "))
# koef1 = create_mn(k1)
# koef2 = create_mn(k2)
# write_file("f_polinom_1.txt", create_str(koef1))
# write_file("f_polinom_2.txt", create_str(koef2))

# # нахождение суммы многочлена

# with open('f_polinom_1.txt', 'r') as data:
#     st1 = data.readlines()
# with open('f_polinom_2.txt', 'r') as data:
#     st2 = data.readlines()
# print(f"Первый многочлен {st1}")
# print(f"Второй многочлен {st2}")
# lst1 = calc_mn(st1)
# lst2 = calc_mn(st2)
# ll = len(lst1)
# if len(lst1) > len(lst2):
#     ll = len(lst2)
# lst_new = [lst1[i] + lst2[i] for i in range(ll)]
# if len(lst1) > len(lst2):
#     mm = len(lst1)
#     for i in range(ll,mm):
#         lst_new.append(lst1[i])
# else:
#     mm = len(lst2)
#     for i in range(ll,mm):
#         lst_new.append(lst2[i])
# write_file("file_res.txt", create_str(lst_new))
# with open('file_res.txt', 'r') as data:
#     st3 = data.readlines()
# print(f"Результирующий многочлен {st3}")