words = 'one two three one four five seven ten seven one'.split()

# 1 в
# result = {}
# for el in words:
#     result[el] = words.count(el)
# print(result)
#
# # # 2 в
# # result = {}
# # for el in words:
# #     if el in result:
# #         result[el] += 1
# #     else:  # якщо ключа el не існує
# #         result[el] = 1
# #
# # print(result)
#
# # # 3 в
# # result = {}
# # for el in words:
# #     result[el] = result.get(el, 0) + 1
# #
# # print(result)
#
# # 4 в
# result = {el: words.count(el) for el in words}
# print(result)
#
#  Множини
# # Множина - невпорядкована(!!!) послідовність УНІКАЛЬНИХ елементів

# 1. Створення множини
# numbers = {1, 10, 45, 2, 1, 10, 45, 2, 1, 10, 54, 10}  # створення множини
# empty_set = set()  # створення порожньої множини

# 2. Методи множини
# # 2. 1. Розширення
# numbers.add(100)  # додає елемент в множину (неважливо, на яке місце)
# numbers.add(1)  # якщо елемент вже є, жодної реакції
#
# # 2. 2. Видалення
# numbers.remove(54)  # видаляє елемент по значенню
# # numbers.remove(20_000)  # якщо елемента не існує - помилка
#
# numbers.discard(2)  # видаляє елемент по значенню (як і remove)
# numbers.discard(20_000)  # на відміну від remove, якщо не існує - жодної реакції

# 2. 3. Стандартні методи
# # numbers.clear()  # очищає множину від всіх елементів
# numbers_copy = numbers.copy()  # як і в списках та словниках, створює автономну копію, не пов'язану з оригіналом
#
# el = numbers.pop()  # витягує умовно перший елемент та видаляє його (як і у списках)
# print(el)
#
# numbers.update([10, 20, 45, 2])  # об'єднує множину з іншою послідовністю
# new_set = numbers.union([200, 300, 20, 2])  # робить update, але результат повертає новою множиною

# 2. 4. Аналіз множин
# worker_1 = {'Python', 'Java', 'C++'}
# worker_2 = {'Java', 'JavaScript', 'C#', 'Python'}
#
# print(worker_1.intersection(worker_2))  # спільні елементи множини А та множини Б
# print(worker_2.intersection(worker_1))  # метод повністю симетричний
#
# print(worker_1.difference(worker_2))  # елементи множини А, яких немає в Б
# print(worker_2.difference(worker_1))  # елементи множини Б, яких немає в А (метод не симетричний)
#
# print(worker_1.symmetric_difference(worker_2))  # все, що не пересікається (унікальні елементи для кожної множини)

# 3. Приклад. Задача: скажіть, які символи є і у першої строки і у другої строки
# string_1 = input('Текст: ').lower()
# string_2 = input('Текст: ').lower()
#
# print("Спільні символи: " + ', '.join(set(string_1).intersection(string_2)))