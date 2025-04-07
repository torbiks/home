# ++1 Список - елементи поміщені в квадратних дужках розділених комою. [1, 6, 7]. Помістити в список можна будь які значення.
# ++2 Словник це впорядкована колекція у вигляді ключ: значення.
# ++3 може бути словник або множина
# ++4 дає зрозуміти що функція ітерується - перебирає елементи
############################# 5 закінчив ###################################

# pyt_cod = input("Input cod of Python").split('_')
#
#
# java_cod = ''.join(i.capitalize() for i in pyt_cod)
#
# print(java_cod)

###################################################################


############################## 6 закінчив ##################################
# num = input('Введіть числа:').split(' ')
# memory = ''
# for i in num:
#     if i in memory:
#         print('Yes')
#     else:
#         print('No')
#     memory += i

###################################################################
############################## 7 закінчив ##################################

# string1 = 'the quick brown fox jumps over the lazy dog'
# string2 = ''
# for r in string1: # вирішив прибрати всі пробіли спочатку
#     if r != ' ':
#         string2 += r
# spysok = {}
# c = 0
# for i in string2:
#     c = string2.count(i)
#     spysok.setdefault(i, c)
# print(spysok)
####################################################################


################################ 8 закінчив #################################

# xtx1 = set('Red Green Orange White'.split(' '))
# xtx2 = set('Black Green White Pink'.split(' '))
#
# print(xtx2.intersection(xtx1))

####################################################################


############################ 9 ###################################### не закінчив, не можу "звести кінці"
# friend_1 = {
#     'шкарпетки': 3,
#     "намет": 1,
#     "сокира": 2,
#     "кастрюля": 1,
#     "вода": 5,
#     "їжа": 3
# }
#
# friend_2 = {
#     'намет': 1,
#     "їжа": 2,
#     "вода": 2,
#     "ніж": 1,
#     "бінокль": 2
# }
#
# summed_friends = {}
# for key in set(friend_1) | set(friend_2):
#     summed_friends[key] = friend_1.get(key, 0) + friend_2.get(key, 0)
#
# print('Загальна кількість пердметів: ')
# for k, v in summed_friends.items():
#     print(f'\t*\t{k}: {v}')
#
#
# sum_item = set(friend_2).intersection(set(friend_1))
# print(f'Спільні речі: {sum_item}')
#
# # sum_dict = []
# # for key, val in friend_1.items() | friend_2.items():
# #     sum_dict += [key, val]
# #
# # print(f'{sum_dict}')
#
#
# print(f'Речі які є тільки в першому рюкзаку: {set(friend_1).difference(set(friend_2))}')
# print(f'Речі які є тільки в другому рюкзаку: {set(friend_2).difference(set(friend_1))}')
#####################################################################

############################## 10 закінчив ####################################
# num = '6 0 3 0 5 0 0 4'.split(' ')
#
# new_num = ''
# num_null = ''
# for i in num:
#     if i != '0':
#         new_num += i
#     else:
#         num_null += i
# print(new_num+num_null)

#####################################################################


############################### 11 закінчив #####################################
# rym = {
#     "I" : 1,
#     "IV" : 4,
#     'V' : 5,
#     'IX' : 9,
#     'X' : 10,
#     'XL' : 40,
#     'L' : 50,
#     'XC' : 50,
#     'C' : 100,
#     'CD' : 400,
#     'D' : 500,
#     'CM' : 900,
#     'M' : 1000
# }
# reversed_rym = []
# for k, v in rym.items():
#     reversed_rym = sorted(rym.items(), key=lambda item: item[1], reverse=True)
#
# number = int(input('Number: '))
# char_rym = ''
# for key, val in reversed_rym:
#     while number >= val:
#         number -= val
#
#         char_rym += key
#
# print(char_rym)

#####################################################################


############################ 12 ######################################
# room = [
#     ['*', '*', '*', '*', '*',],
#     ['*', '*', '*', '*', '*',],
#     ['*', '*', 'R', '*', '*',],
#     ['*', '*', '*', '*', '*',],
#     ['*', '*', '*', '*', '*',]
# ]
# rest = 0
# while rest == 0:
#     while True:
#         moving = {}
#         robot = 0
#         user_com1 = input('Вкажіть напрямок (UP -> U; down -> D; left -> L; right -> R; 0 -> Вихід з программи):').upper()
#
#         user_com2 = input('Вкажіть кількість клітинок яку має пройти робот (обмеження до 4):')
#         r = (user_com1, user_com2)
#         match user_com1:
#             case 'U':
#                 room[2[2]] = 'l'
#                 print(room)
#             case 'D':
#                 print('down')
#             case 'R':
#                 print('right')
#             case 'L':
#                 print('left')
#             case _:  # аналог else
#                 print('!!')
#
#         print(r)
#
#
#         if user_com1 == 0:
#             break



#####################################################################