## 1 ++
# number = [3, -9, 15, 0, 21, 45, -11, 28, 94, -64, 0, 68, 52, 38, 18]
# minus_count = 0
# plus_count = 0
# nulcount = 0
#
# max_number = max(number)
# min_number = min(number)
#
# for el in number:
#     if el < 0:
#         minus_count += 1
#     elif el > 0:
#         plus_count += 1
#     elif el == 0:
#         nulcount += 1
# print(f"Кількість від'ємних значень:{minus_count} \nКількість додатних значень: {plus_count}\nКількість нулів: {nulcount}")
# print(f'Мінімальне/максимальне значення:{min_number}/{max_number}')

## 2 ++
# word_list = ["Літак", "дрон", "Авіація", "енергія", "Пілот", "датчик", "Контроль", "зв'язок", "Маневр", "Камера", "мотор", "Крило", "польот", "Батарея", "траєкторія", "Висота", "Швидкість", "Стабільність", "навігація", "Технологія"]
#
# for el in word_list:
#     if el.istitle() == False:
#         word_list.remove(el)
#
# print(word_list)


## 3 ++
number = [2, 3, 5, 5, 7, 3, 3, 2, 6, 6]
count = 0
result = []

for el in number:
    if el in number:
        count = number.count(el)
        if count % 2 != 0:
            result.append(el)
print(set(result))

## 4 ++
#
# types_list = ['bob', 15, 'adam', 545, True, 15.698, None, 2.56, True, None, print]
#
# list_int = []
# list_str = []
# list_bool = []
# list_float = []
#
# for el in types_list:
#     if type(el) == str:
#         list_str.append(el)
#     elif type(el) == int:
#         list_int.append(el)
#     elif type(el) == bool:
#         list_bool.append(el)
#     elif type(el) == float:
#         list_float.append(el)
#
# print(f'Рядковий {list_str}')
# print(f'Числовий {list_int}')
# print(f'Булевий {list_bool}')
# print(f'З крапкою {list_float}')


## 5 ++
# n = int(input(f'Введіть кількість чисел які потрібно внести в списки:'))
# num_list1 = list(int(input(f'Введіть число для першого списку:')) for _ in range(n))
# num_list2 = list(int(input(f'Введіть число для другого списку:')) for _ in range(n))
# sum_list = []
#
# # for el in range(n):
# #     num_list1.append(int(input(f'Введіть {el+1} число першого списку:')))
# # for el in range(n):
# #     num_list2.append(int(input(f'Введіть {el+1} число другого списку:')))
#
# for i in range(n):
#     sum_list.append(num_list1[i] + num_list2[i])
#
# print(f'Сумма елементів списків в новому списку: {sum_list}')
