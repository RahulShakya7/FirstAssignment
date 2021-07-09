def fizz_buzz(a):
    if  a % 3 == 0 and a % 5 == 0:
        print('Fizzbuzz')
    elif a % 5 == 0:
        print('buzz')
    elif a % 3 == 0:
        print('Fizz')


a = int(input('Enter a number : '))
fizz_buzz(a)

# 1
# a = (input('Enter a word : '))
# b = ''
# for i in a:
#     b = i + b
# print(f"The reverse is {b}")
# 2
# a = [1, 2, 3, 3, 3, 4, 4, 5, 6]
# b = []
# for i in a:
#     if i not in b:
#         b.append(i)
#         print(i)
# 3
# a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# for i in a:
#     if i % 2 == 0:
#         print(i)
# 4
# import math
# a = int(input('Enter a number : '))
# b = math.factorial(a)
# print(f'The factorial of {a} is {b}')
# 5
# a = input("Enter a string\n")
# b = a[::2]
# print(b)
# 6
# a = input("Enter a string\n")
# b = a[1::2]
# print(b)
# 7
# myList = "Parameter"
# print(len(myList))
# 8
# x = 5
# x += 3
# print(x)
# 9
# def ok(a):
#     b = 1
#     for i in a:
#         b = b * i
#     print(b)
#
#
# a = [8, 2, 3, -1, 7]
# ok(a)
# 10
# num = int(input('Enter a number : '))
# if num > 1:
#     for i in range(2, num):
#         if (num % i) == 0:
#             print(num, "is not a prime number")
#             break
#     else:
#         print(num, "is a prime number")
#
# else:
#     print(num, "is not a prime number")
# 11
# a = 0
# while a < 10:
#     a = a + 1
#     print('Hello World')
# 12
# a = 1
# b = 0
# while a <= 10:
#     b = b + a
#     a = a + 1
# print(b)
# 13
# s = []
# for i in range(5):
#     a = int(input(f'Age of person is {i} : '))
#     s.append(a)
# print(s)


