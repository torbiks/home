def kalculat(num1: float, num2: float, operation):
    if operation == '+':
        print(num1+num2)
    elif operation =='-':
        print(num1-num2)
    elif operation == '*':
        print(num1*num2)
    elif operation == '/':
        if num2 != 0:
            print(num1 / num2)
        else:
            print('Ділення на нуль неможливе')
    else:
        print('Unknown operation')

def is_palindrome(text: str):
    memory = ''
    for i in text[::-1]:
        memory += i
    if memory == text:
        print('Palindrom')
    else:
        print('No palindrom')
    return memory == text

def html_tag(tags: str, cod_html: str):

    tags_op, tags_cl = "<>", '</>'
    decode_html = tags_op[0] + tags + tags_op[1] + cod_html + tags_cl[0:2] + tags + tags_cl[2]
    return decode_html

def is_prime(number: int):
    if number >1 and number / number == 1:
        print('Proste')
    elif number % number != 0:
        print('Ne proste')



print(is_prime(number=int(input(': '))))

def count_vowels_consonants(text: str):
    count_g = 0
    count_p = 0
    if len(text) < 1:
        print('ERROR!!!')
    for i in text:

        if i in 'яаиоїіеєЯАИОЇІЕЄ':
            count_g += 1

        elif i in 'йцкнгшщзхфвпрлджчсмтбЙЦКНГШЩЗХФВПРЛДЖЧСМТБ':
            count_p += 1
    print(f'Голосних: {count_g}, Приголосних: {count_p}')



####################### 1 ##########################################
# print(kalculat(num1 = float(input('num1')), num2 = float(input('num2')), operation=input('Оператор:')))
#####################################################################

####################### 2 ##########################################
# print(is_palindrome(text = input('Введіть текст на перевірку паліндромності: ')))
#####################################################################

######################### 3 #########################################
#print(html_tag(tags=input("Ведіть тег HTML: "), cod_html=input('Ведіть код який треба помістити в тег:')))
#####################################################################

######################### 4 ########################################

#####################################################################

######################### 5 #########################################
# print(count_vowels_consonants('Привіт світ'))
#####################################################################

