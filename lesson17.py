'''
Адреса для файлу:
1. Глобальний(абсолютний) шлях: D:\\Programs\\ItStep\\Python Core\\Projects\\PythonAI51Project\\files\\data.txt
2. Локальний шлях: files\\data.txt
'''

words = ['python', 'new', 'old', 'print', 'input', 'sep']

# запис (write)
file = open('files\\data.txt', 'w')  # 'w' або створює файл, якщо його немає, або перезаписує

file.write('PYTHON\n')  # 1-й спосіб запису: метод write()
file.write('PYTHON\n')
file.write('PYTHON\n')

print('LINE 1', file=file)  # 2-й спосіб запис: використання print
print('LINE 2', file=file)
print('LINE 3', file=file)

file.writelines(el + '\n' for el in words)  # 3-й спосіб: запис ітерованої послідовності

print(*words, sep='\n', file=file)  # 4-й спосіб: 3-й спосіб тільки через print

file.close()

# читання (read)
file = open('files\\data.txt', 'r')  # для того, щоб відкрити файл на читання, ФАЙЛ ПОВИНЕН ІСНУВАТИ (!!!)

data = file.read()  # 1-й спосіб: читання всього файлу цілком
# print(file.readlines())  # 2-й спосіб: повертає список, в якому елементом є рядок файлу
#
# for line in file:  # 3-й спосіб: ітерація файлу (в Python текстовий файл являється ітерованою послідовністю)
#     print(line, end='')

print(file.read())
# print('============')
# file.seek(0)  # переміщає курсор на початок файлу
# print(file.readline(), end='')  # 4-й спосіб: прочитати один рядок
# print(file.readline(), end='')
#
file.close()
#
# print(data)
#
# with open('files\\data.txt', 'a') as file:  # 'a' - режим для доповнення (запис без видалення)
#     print('HELLO', file=file)
#
#
# with open('files\\data.txt', 'r') as file:
#     counter = 0
#
#     for line in file:
#         counter += 1
#
#     print(counter)
#
#     # print(len(file.readlines()))