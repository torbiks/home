def create_hashtag(string: str):
    memory = '#'
    if len(string) == 0:
        return False
    for el in string:
        if el != ' ':
            memory += el
        if len(memory) > 140:
            return False
            break
    print(len(memory))
    return memory

def persistence(n: int):
    counter = 0
    while len(str(n)) > 1:
        memory = 1
        for el in str(n):
            memory *= int(el)
        counter += 1
        n = memory
    return counter


def get_dividers(n: int):
    while n % 2 == 0:
        mnoginy = []
        if n // 2 > 1:
            mnoginy.append(2)
        elif n // 3 > 1:
            mnoginy.append(3)
    print(mnoginy)

# get_dividers(15)
# print(persistence(9999999))
# print(create_hashtag(string= input('input text for hashtag:')))




import functools


def get_dividers(n: int):  # 1  1 -> 2, 2, 3
    while n != 1:
        for divider in range(2, n + 1):
            if n % divider == 0:
                yield divider
                n //= divider
                break


def persistence(n: int):  # 3
    counter = 0

    while n not in range(1, 10):
        # result = 1
        #
        # for str_digit in str(n):
        #     result *= int(str_digit)

        result = functools.reduce(lambda el1, el2: int(el1) * int(el2), str(n))

        counter += 1
        n = result

    return counter


def create_hashtag(string: str):  # 5
    if len(string) == '':
        return False

    result = '#' + ''.join(string.split())

    return result if len(result) <= 140 else False