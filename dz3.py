def open_file():
    with open('input.txt', 'w') as file:
        print('Python\nRuby\nC++len08\nC\nJava\nGO', file=file)

def overkill():
    with open('input.txt', 'r') as file:
        memory = ""
        for line in file:
            if len(line) > len(memory):
                memory = line
    return memory

def main():
    while True:
        choice = input('Оберіть опцію 1-Зчитати файл, 2 - знайти найдовше слово, 0 - Закінчення роботи: ')

        if choice == '2':

            print(f'Результат пошуку: {overkill()}')
        elif choice == '1':
            open_file()
            print(f'Файл зчитано')
        elif choice == '0':
            print('Роботу завершено')
            break
        else:
            print('Некоректний вибір, спробуйте ще раз.')

main()

# #ДЗ №1
# var_1 = float(input('Введіть число:'))
# cile = var_1 / var_1
# if var_1 % 2 == 0:
#     print('Число парне')
# elif cile % 2 != 0:
#     print('Число не ціле, а отже не може бути парним або непарним')
# else:
#     print('Число не парне')



# #ДЗ №2
# days = {
#     1: "понеділок",
#     2: "вівторок",
#     3: "середа",
#     4: "четвер",
#     5: "п'ятниця",
#     6: "субота",
#     7: "неділя"
# }
#
# try:
#     day_number = int(input("Введіть номер дня тижня (1-7): "))
#     if 1 <= day_number <= 7:
#         print("Це", days[day_number])
#     else:
#         print("Помилка! Введіть число від 1 до 7.")
# except ValueError:
#     print("Помилка! Введіть ціле число.")


# #ДЗ №3
# zm1 = float(input('a='))
# zm2 = float(input('b='))
# zm3 = float(input('c='))
# aver = round((zm3 + zm1 + zm2) / 3, 2)
# print(f'Максимальне значення:', max(zm1, zm2, zm3))
# print(f'Мінімальне значення:', min(zm1, zm2, zm3))
# print(f'Середнє арифметичне значення: {aver}')



# #ДЗ №4
# nameuser = input('Name:')
# numberuser = int(input('Number ID user:'))
#
# if numberuser % 2 == 0:
#     print(f'Hi, {nameuser}')
# elif numberuser % 2 != 0 and numberuser % 3 == 0:
#     print(numberuser ** 2)
# else:
#     print('Bye')

#ДЗ №5

# zm1 = float(input("Number: "))
# result = zm1 / 2
# if zm1 % 2 == 0:
#     print(int(result))
# else:
#     print(result)



