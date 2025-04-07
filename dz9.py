# ## 1 ++
#
# text = input('Text:')
# result = ''
# for i in text:
#     if i.isupper():
#         result += i.replace(i, '*')
#     else:
#         result += i
# print(result)


# ## 2 ++
# rest = 'y'
# while rest == 'y':
#     text = input(':')
#     result = ''
#     max_res = ''
#     for i in text:
#         if i != '0':
#             result += i.replace(i, ' ')
#         else:
#             result += i
#     result = result.split()
#     max_res = len(max(result))
#     print(max_res)
#     rest = input('restart? y/n')
#
#     if rest == 'n':
#         break


## 3 ++
# text = input('Text:').lower()
# count_punct = 0
# result_max = 0
# memory = ''
# alphabet = 'АаБбВвГгҐґДдЕеЄєЖжЗзИиІіЇїЙйКкЛлМмНнОоПпРрСсТтУуФфХхЦцЧчШшЩщьЮюЯя'
# symbol_not = ''
# ###3a
# counter = 0
# result = ''
# max_res = 0
# if text:
#     char_text = text[0]
#     max_res = 0
#     for i in text:
#         if i in text:
#             counter = sum(1 for c in text if c == i)
#             if counter > max_res:
#                 max_res = counter
#                 char_text = i
# else:
#     print("Рядок порожній")
# print(f'Найчастіший символ: {char_text}, використовується разів: {max_res}')
#
# ###3a
# ###3b
# for i in text:
#     if i in ',.?!:;-':
#         count_punct +=1
#
# ###3b
# ###3c
# for i in alphabet:
#     if i not in text:
#         symbol_not += i
# if symbol_not:
#     print(f'Літери, яких не має в тексті: {symbol_not}')
# else:
#     print("Усі літери присутні у тексті")
# ###3c
#
# ###3d
# unic_symbol = len(set(text))
# ###3d
# print(f'Загальна кількість знаків пунктуації {count_punct} шт.')
# print(f'Загальна кількість унікальних символів: {unic_symbol}')


## 4
#
# word1 = input('word:').lower()
# word_audit1 = input('word audit: ').lower()
# result1 = ''
# # word1 = word1.find()
# for char in word_audit1:
#     if char in word1:
#         result1 += char
#
#     else:
#         break
#
# if result1 == word_audit1:
#     print('Yes')
# else:
#     print('No')


## 5

text = input('Введіть рядок який потрібно закодувати:')

coding_string = ''
i = 0
while i < len(text):
    count = 1
    while i + 1< len(text) and text[i] == text[i+1]:
        count +=1
        i +=1
    coding_string += text[i] + str(count)
    i += 1
print(f'Закодований рядок: {coding_string}')