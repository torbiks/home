# Змінні

# # input - ВВІД інформації в консоль
# user_name = input("Enter your name: ")  # створення змінної user_name з значенням
# result = 'Hello, ' + user_name + '!'
#
# print(result)  # print - ВИВІД інформацію в консоль


# ====БАЗОВІ ОПЕРАЦІЇ====

# над числами
number_1 = 10
number_2 = 5

# print(10 + 20)
# print(number_1 + number_2)
# print(number_2 + 1)
#
# print(10 - number_2)
#
# print(10 * 5)  # * - множення
# print(number_1 / 2)  # / - ділення
#
# print(3 ** 3)  # 3 у 3 степені (** - степінь)
# print(10 // 3)  # цілочислене ділення (повертає тільки цілу частку від ділення)

# print(number_1 % number_2)  # повертає остачу від ділення
print(6 % 2)

# # над строками(текстом)
# text_1 = 'Hi'
# text_2 = '10'
#
# print(text_2 + '20')  # + для строк - "зклеювання" (concatenate)
# print(text_1 + '!!!!!')
# print('a' + 'b' + 'c')
#
# print('$' * 25)  # * для строк - "дублювання" строки n раз
# print(text_1 * 10)
#
# # Робота з змінними
# counter = 10
#
# # counter = 5
#
# # print(counter + 1)
# # print(counter + 1)
# # print(counter + 1)
#
# counter = counter + 1
# counter = counter + 1
# counter = counter + 1
#
# counter += 1  # += - додати до змінної 1, та записати в неї результат
# counter += 1
#
# # !!! в програмування "=" - присвоєння
#
# print(counter)
#
# # Типи даних
#
# string = '10'  # str(строка) - текстовий літерал, або послідовність символів
#
# integer = 10  # int - ціле число
# float_ = 10.10  # float - дробове десятичне число
#
# boolean = True  # bool - логічний тип даних: True(Істина, Так, 1); False(Брехня, Ні, 0)
#
# none = None  # None - відстуній тип даних
#
# # Перетворення
#
# # на str (фактично майже завжди просто накладає лапки на об'єкт)
# print(str(10) + '!')
# print(str(True) + '.')
#
# # на int
# print(int('10') + 1)
# # print(int('abc'))  # ValueError, бо таку строку не можна перетворити на число
# print(int('10_000_000'))
# # print(int('5354as.fbsa34'))  # ValueError
#
# print(int(9.9999))  # 9, бо це НЕ округлення
# print(int(False))
#
# # на bool - True, якщо об'єкт НЕ порожній
# print(bool(1))
# print(bool(-5))
# print(bool(0))
#
# print(bool('False'))
# print(bool(''))
#
# print(bool(None))
#
# # # Задача
# num_1 = int(input('Введіть число 1: '))  # input() завжди повертає STR
# num_2 = int(input('Введіть число 2: '))
#
# sum_of_numbers = num_1 + num_2
# print('Сума чисел: ' + str(sum_of_numbers))
# print(f'Сума чисел: {sum_of_numbers}')
#
# string = 'Hello, world!'
#
# print(len(string))
#
# print(string[0])
# print(string[5])
#
# print(string[-1])  # -1 - останній символ
#
# print(string[:5])  # зріз від початку до 4 (кінець не включається)
# print(string[7:12])  # від 7 до 11
#
# print(string[5:])  # від 5 ДО КІНЦЯ
#
# print(string[:])  # вся строка, бо ВІД ПОЧАТКУ до КІНЦЯ
#
# print(string[7:-1])
# print(string[10:1])  # порожній зріз, бо початок більший за кінець
#
# bool_true = True  # Істина, 1
# bool_false = False  # Брехня, 0
#
# # Порівняння чисел
# print(20 > 10)
# print(20 < 10)
#
# print(20 >= 20)  # більше або дорівнює
# print(10 <= 100)  # менше або дорівнює
#
# print(10 == 10.0)  # дорівнює
# print(25 != 25.0)  # не дорівнює
#
# # Порівняння строк
# print('abc' > 'ABC')  # на > < строки порівнюються за unicode
#
# print('abc' == 'acb')  # на == строки порівнюються на ідентичність
# print('25' != '25.0')
#
# # Об'єдання порівнянь
#
# # і (and) - потребує True всюди (зліва та зправа)
# print(True and True)
# print(False and True)
# print(False and False)
#
# # або (or) - потребує True хоч десь
# print(True or True)
# print(False or True)
# print(False or False)
#
# print(not True)
# print(not False)
#
# # Цикли
# # Ітерація - повторення одного порядку дій через якусь послідовність
# # _iterable - властивість об'єктів, що дозволяють їм ітеруватись
#
# # WHILE (ПОКИ)
#
# number = 1
#
# while number <= 100_000:  # ПОКИ <умова == Істина>: <код>
#     print(number)   # крок циклу - 1 виконання всього його коду (1 ітерація)
#     number += 1  # додає 1 до number
#
# while True:  # while True - нескінченний цикл
#     print(number)
#     number += 1
#
#     if number > 100_000:  # умова виходу
#         break  # break - вихід з циклу
#
#
# text = input('Text: ')
# index = 0
#
# while index < len(text):  # ітерація строки по індексу
#     print(text[index])
#     index += 1
#
# # FOR (ДЛЯ)
#
# for number in range(1, 100_001):  # ДЛЯ <частина> З <об'єкт>: <цикл>
#     print(number)
#
# text = input('Text: ')
#
# for index in range(len(text)):
#     print(text[index])
#
# for char in text:  # ітерація строки (str)
#     print(char)
#
# # Задача: користувач вводить строку. Порахуйте кількість голосних літер
#
# text = input('Text: ')
# counter = 0
#
# for char in text:
#     if char in 'OIUYEAoiuyea':
#         counter += 1
#
# print(f'Кількість голосних літер: {counter}')
#
