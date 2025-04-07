## 1 через FOR
# num1 = int(input('Введіть число 1:'))
# num2 = int(input('Введіть число 2:'))
#
#
# for i in range(num1, num2+1):
#     if i % 3 == 0 and i % 5 != 0:
#         print(i)


## 1 через WHILE
# num1 = int(input('Введіть число 1:'))
# num2 = int(input('Введіть число 2:'))
# result = num1
#
# while result < num2:
#     if result % 3 == 0 and result % 5 != 0:
#         print(result, end=" ")
#     result = result+1

# # 2
# num = int(input('Number:'))
# res = 1 # множення на 0 неможливе
# for fact in range(1, num+1):
#     res = fact * res
#     print(f'{fact}! = {res}')

## 3
# name = input('Name:')
#
# while len(name) <= 10:
#     name = input('Name:')

## 3
# name = input("Введіть ім'я: ")
# res_name = name
# counter = 0
# while len(res_name) <= 100:
#     counter = len(res_name)
#     print(f'{res_name}. Кількість символів: {counter}')
#     res_name += name

## 4 погуглив метод визначення числа в тексті вийшло, але якщо вводжу від'ємні значення, мінус прибирається((
## також якщо більше одного пробіла, рахує неправильно
#
# text = input('Text: ')
# counterp = 0
# countern = 0
# res = ""
# for char in text + ' ':
#     if char.isdigit():
#         res += char
#     elif res:
#         if int(res) % 2 == 0:
#             counterp += 1
#         else:
#             countern += 1
# print(res)
# print(f'Парних чисел {counterp}, непарних чисел {countern}')


