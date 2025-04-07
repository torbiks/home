# month = int(input('Number months:'))
#
# match month:
#     case 1 | 2 | 12:         # | - or
#         print('Winter')
#     case 3:
#         print('Vesna')
#     case 4:
#         print('Vesna')
#     case 5:
#         print('Vesna')
#     case 6:
#         print('Summer')
#     case 7:
#         print('Summer')
#     case 8:
#         print('Summer')
#     case 9:
#         print('Osin')
#     case 10:
#         print('Osin')
#     case 11:
#         print('Osin')
#     case _:
#         print("Ведіть будь ласка від 1 до 12")

# day = int(input("Number day in year:"))
# result = day % 7
#
# if result == 0:
#     print('')
# elif result == 1:
#     print('')
# elif result == 1:
#     print('')
# elif result == 1:
#     print('')
#
#  match day % 7:     # порівнюємо результат
#      case 0:
#          print('nedila')



char = input("1 bukva")

# len довжина строки
# in орівняння ліву і праву чатину



'''
Користувач вводить номер дня(1-365). Відомо, що рік починається з понеділка.
Виведіть відповідний день тижня.
'''

# day = int(input('Введіть номер дня(1-365): '))
# result = day % 7
#
# print(result)
#
# # if result == 0:
# #     print('Неділя')
# # elif result == 1:
# #     print('Понеділок')
# # elif result == 2:
# #     print('Вівторок')
# # elif result == 3:
# #     print('Середа')
# # elif result == 4:
# #     print('Четвер')
# # elif result == 5:
# #     print("П'ятниця")
# # elif result == 6:
# #     print("Субота")
#
# match day % 7:  # порівнюємо в match остачу від ділення на 7
#     case 0:
#         print('Неділя')
#     case 1:
#         print('Понеділок')
#     case 2:
#         print('Вівторок')
#     case 3:
#         print('Середа')
#     case 4:
#         print('Четвер')
#     case 5:
#         print('П`ятниця')
#     case 6:
#         print('Субота')

'''
Користувач вводить символ(літеру алфавіту). Скажіть, чи являється цей символ голосним або
приголосним. Якщо вводиться не 1 символ, то видайте помилку
'''

# char = input('Введіть 1 літеру: ')
#
# if len(char) != 1:
#     print('ERROR. Ви ввели не одну літеру!!!')
# elif char in 'яаиоїіеєЯАИОЇІЕЄ':
#     print('Літера голосна!')
# elif char in 'йцкнгшщзхфвпрлджчсмтбЙЦКНГШЩЗХФВПРЛДЖЧСМТБ':
#     print('Літера приголосна!')
# else:
#     print('Ви ввели не літеру, або літеру іншої мови!')

'''
Користувач вводить ШЕСТИЗНАЧНЕ число. Скажіть, чи являється це число щасливим.
Примітка: щасливим числом вважаться число, де сума перших трьох цифр дорівнює сумі останніх трьох
Наприклад: 306117 - щасливе число
'''

number = input('Введіть шестизначне число: ')

if len(number) == 6:
    first_part = int(number[0]) + int(number[1]) + int(number[2])
    second_part = int(number[3]) + int(number[4]) + int(number[5])

    # # в 1
    # if first_part == second_part:
    #     print('Число щасливе!')
    # else:
    #     print('Число звичайне')

    # в 2
    print('Число щасливе' if first_part == second_part else "Число звичайне")
else:
    print('Ви ввели не шестизначне число')