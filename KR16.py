import time




### 1 #### Функція вищого порядку (higher-order function) — це функція, яка приймає інші функції як аргументи, або повертає інші функції як результат.
### 2 #### Генератор - це функція, що повертає послідовність значень
### 3 #### Рядок if __name__ == "__main__": використовується для перевірки, чи запущено скрипт безпосередньо, а не імпортовано як модуль.
### 4 #### Позиційний зобов'язує нас ввести його при виклику функції, а ключовий лише у випадку звернення до ключа.
################ 5 #########################+

def accum(text: str):
    result = []
    i = 0
    for char in text:
        print(i, char)
        result.append(char.upper() + char.lower() * i)
        i += 1
    return "-".join(result)


print(accum('aBcd'))

################ 5 ###############################+

################ 6 ###############################+

# def timer_clock(minutes: int):
#
#     seconds = minutes * 60
#     for i in range(seconds, 0, -1):
#         print(f'time of clock: {i} second')
#         time.sleep(1)
#     print('Off timer')
#
# try:
#     user_input = int(input("Введіть час у хвилинах: "))
#     timer_clock(user_input)
# except ValueError:
#     print("Будь ласка, введіть коректне число.")
#
# timer_clock()

################ 6 ###############################+

################ 7 ###############################+
# def reverse_text(text: str):
#     words = text.split()
#     print(words)
#     result = []
#     for el in words:
#         if len(el)>=5:
#             result.append(el[::-1])
#         else:
#             result.append(el)
#
#     return ' '.join(result)
#
# print(reverse_text('привіт як справи у тебе'))


################ 7 ###############################+

################ 8 ###############################

# def prosto(n: int):
#     memory = ''
#     for i in range (2, n):
#         if n % i != 0:
#             memory += str(i) + ', '
#
#     return memory
# print(prosto(50))

################ 8 ###############################

################ 9 ###############################+

def generator_n(n: int):
    num = []
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = n * 3 +1
        num.append(n)

    yield num

print(*generator_n(17), sep=', ')

################ 9 ###############################+



def accum(s: str):
    # return '-'.join(char.upper() + (char.lower() * counter) for counter, char in enumerate(s))
    # return '-'.join((char * counter).capitalize() for counter, char in enumerate(s, start=1))
    return '-'.join(char * counter for counter, char in enumerate(s, start=1)).title()


def spin_words(words: str):  # функція приймає слова через пробіл
    # 1- спосіб:
    result = ''

    for word in words.split():
        if len(word) < 5:
            result += word
        else:
            result += word[::-1]

        result += ' '

    return result.strip()

    # #  2- спосіб:
    # return ' '.join(word if len(word) < 5 else word[::-1] for word in words.split())


def prime_generator(n: int):
    for number in range(1, n + 1):
        for divider in range(2, number):
            if number % divider == 0:
                break
        else:
            yield number


def collatz_gen(n: int):
    while n != 1:
        yield n

        if n % 2 == 0:
            n //= 2
        else:
            n *= 3
            n += 1

    yield n


def memory(function):
    cache = {}  # func: sum results

    def wrapper(*args, **kwargs):
        result = function(*args, **kwargs)

        if function in cache:
            cache[function] += result
        else:
            cache[function] = result

        return cache[function]

    return wrapper


@memory
def sum_two_numbers(a, b):
    return a + b


def move_knight(position: str):  # Приклад позиції: e4, h5
    columns = {char: index for index, char in enumerate('abcdefgh')}
    board = [['.' for _ in range(8)] for _ in range(8)]

    knight_row = int(position[1]) - 1
    knight_column = columns.get(position[0])

    board[knight_row][knight_column] = 'K'

    moves = [(1, 2), (2, 1), (-1, 2), (2, -1), (-2, 1), (-2, -1), (-1, -2), (1, -2)]

    for row_change, column_change in moves:
        new_row = knight_row + row_change
        new_column = knight_column + column_change

        if new_row not in range(8) or new_column not in range(8):
            continue

        board[new_row][new_column] = '*'

    board.reverse()

    return board


print(*move_knight('c3'), sep='\n')






