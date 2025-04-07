


def to_uppercase():
    return input('Ведіть текст:').upper()

# print(to_uppercase())

def find_intersection(a=[], b=[]):
    sum_list = a + b
    return sum_list
# print(find_intersection([5,6,8,9,7], [1,2,3,4,5]))

def is_anagram():
    count = 0
    text1 = input('text 1: ')
    text2 = input('text 2: ')
    if len(text1) == len(text2):
        for el in text1:
            if el in text2:
                count += 1
    if count == len(text1):
        print('Це Анаграмма!')
    elif count < len(text1):
        print(f'Співпадінь лише {count} із {len(text1)}')
    return count

print(is_anagram())