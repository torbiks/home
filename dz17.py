# # #################### z Uroku #######################
# with open('input.txt', 'w') as file:
#     print('2', file=file)
#     print('2', file=file)
#
# with open('input.txt', 'r') as file:
#     memory = 0
#     for line in file:
#         memory += int(line)
#
#
# with open('output.txt', 'w') as file:
#     print(memory, file=file)
# # #################### z Uroku #######################
# ########################### 1 ######################################
# def new_file():
#     list_files = ['input.txt', 'output.txt']
#     summa = input('name is new file:')
#     memory = ''
#     for file in list_files:
#         with open(file, 'r') as file:
#             for line in file:
#                 memory += line
#     with open(summa, 'a') as file:
#         print(memory, file=file)
#
#
#     return print(f'Файли опрацьовані! Результат в файлі {summa}')
#
# new_file()
# ########################### 1 ######################################


########################### 2 ######################################
# def list_user():
#     list = []
#     end = 'y'
#
#     n = int(input('Яку кількість елементів списку будете вносити? Введіть значення:'))
#     for i in range(n):
#         num_user = int(input(f'{i+1} number for list:'))
#         list.append(num_user)
#
#     for el in list:
#         print(f'Index[{list.index(el)}] = {el}')
#
#     while end == 'y':
#         ind = int(input('Введіть номер індексу який шукаєте:'))
#         try:
#             print(list[ind])
#         except IndexError:
#             print(f'Ви вийшли поза межі списку, виберіть від 0 до {len(list)-1}')
#         if end == 'y':
#             end = input('Бажаєте ще знайти елементи списку по індексу (y - так/n - ні:')
#     print('Дякуємо за використання нашого сервісу!')
#     return list
#
# list_user()
########################### 2 ######################################


########################### 3 ######################################
find_file = input("Вкажіть назву файлу який хочете подивитися:")
add_file_user = 'y'
try:
    with open(find_file, 'r') as file:
        for line in file:
            print(line, end='')
except FileNotFoundError:
    print(f"Файл {find_file} не існує.")
    add_file_user = input('Хочете створити файл з такою назвою? y/n')
    if add_file_user == 'y':
        with open(find_file, 'w') as file:
            text_file = input('data in file:')
            print(text_file, file=file)
    res = input('Відкрити файл для перегляду? y/n')
    if res == 'y':
        with open(find_file, 'r') as file:
            for line in file:
                print(line, end='')



########################### 3 ######################################