# ## 1
# num1 = int(input('Скільки чисел потрібно ввести? '))
# result = ''
# for i in range(1, num1+1):
#     memory = input(f'Введіть {i} число: ')
#     result += memory + ' '
#
# print(result)


# ## 2
text_user = input("Введіть текст для підрахунку голосних літер в ньому):")
count =0
for i in text_user:
    if i in "иуеіаойяєїИУЕІАОЙЯЄЇ":
        count +=1
print(count)

## 3

# text = '"Привіт, як твої справи? У мене все ок."'
# num_char = int(input('Якої довжини слова рахувати? (введіть кількість символів) : '))
# result = ''
# counter = 0
# count_char = 0
# probel = 0
# for i in text:
#     if 'а' <= i <= 'я' or 'А' <= i <= 'Я' or i in "єїіґЄЇІҐ":
#         result += i
#     else:
#         if len(result) == num_char:
#             counter += 1
#         result = ''
#
# print(f"Кількість слів довжиною {num_char} символи: {counter} шт.")

## 4

# import random
# import time
#
# comp_number =  random.randint(1, 100)
# attempt = 0
# start_time = time.time()
# #res = 0
# while True:
#     number_user = int(input('Введіть число:'))
#     attempt += 1
#     res = abs(number_user - comp_number)
#
#     if 1 <= res <= 5:
#         print("Гаряче")
#     elif 6 <= res <= 15:
#         print('Холодно')
#     elif 16 <= res <= 100:
#         print('Крижано')
#     else:
#         end_time = time.time()
#         res_time = round(end_time - start_time, 2)
#         print('Еврика!!! Ви вгадали!!')
#         print(f'Використано спроб:{attempt}')
#         print(f'Час витрачено на рішення завдання:{res_time}')
#         break
