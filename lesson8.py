# ## 1 ++
# memory = 0
# numbers = ''
# while numbers != 0:
#     numbers = int(input('введіть число'))
#     memory += numbers
#
# print(memory)

# ## 4 ++
#
# xtx = 'Привіт, я просто тестую. Це звичайний текст!!!'
#
# result = ''
# result_char = ''
#
# for char in xtx:
#     if 'а' <= char <= 'я' or 'А' <= char <= 'Я' or char in "єїіґЄЇІҐ" or char in ' ':
#         result += char
#     else:
#         result_char += char
#
# print(f'{result} {result_char}')



# # Завдання 1
# result = 0
#
# while True:
#     number = int(input('Введіть число: '))
#
#     if number == 0:
#         break
#
#     result += number
#
# print(result)
#
# # Завдання 2
# user_number = int(input('Введіть число: '))
#
# a = 0  # завжди передостаннє число
# b = 1  # завжди останнє число
#
# while a <= user_number:
#     print(a, end=' ')
#     a, b = b, a + b
#
# # Завдання 3
# start = int(input('Введіть початок: '))
# end = int(input('Введіть кінець: '))
#
# for number in range(start, end + 1):
#     result = 0
#     str_number = str(number)
#
#     number_len = len(str_number)
#
#     for str_digit in str_number:
#         result += int(str_digit) ** number_len
#
#     if result == number:
#         print(f'Число Армстронга знайдено: {number}')
#
# # Завдання 4
#
# text = 'Привіт, я просто тестую. Це звичайний текст!!'
#
# chars = ''
# punctuation = ''
#
# for char in text:
#     if char in '!?.,:; ()[]':
#         punctuation += char
#     else:
#         chars += char
#
# print(chars + punctuation)