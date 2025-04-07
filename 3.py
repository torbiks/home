# # 1
# import random
#
# numbers = [random.randint(-100, 100) for _ in range(20)]
# result = []
# minus = 0
# for num in numbers:
#     if num % 2 == 0:
#         result.append(num)
#     if num < 0:
#         minus += 1
#
# print(result, end=', ')
# print(minus)
#
# # print(numbers)


# words = 'Happy New Year Happy New Year May we all have a vision now and then Of a world where every neighbor is a friend'
#
# result = words.split()
# counter = 0
# memory = []
# # result1 = set(result)
# # print(len(result1))
# for el in result:
#     if el not in memory:
#         counter +=1
#         memory.append(el)
# print(counter)


x = 11
y = 4

x = x % y
x = x % y
y = y % x

print(y)

