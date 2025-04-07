################ 1 ########################

#
# text = 'one two three one four five seven ten seven one'
#
# text = text.split()
# count = 0
# dict_of_text = {}
#
# for el in text:
#     if text.count(el):
#         count = text.count(el)
#     dict_of_text[el] = count
# print(dict_of_text)

########################################
############### 2 #######################

# number = list(map(int, input('input numbers in space:').split(' ')))
# print(number)
# while True:
#     if len(number) > 2:
#         number.pop(2)
#         print(number)
#     elif 0 != len(number) <= 2:
#         number.pop(0)
#         print(number)
#     else:
#         break
#######################################



############### 3 #######################
# morze = {'a': '•—', 'b': '—•••', 'c': '—•—•', 'd': '—••',
#          'e': '•', 'f': '••—•', 'g': '——•', 'h': '••••',
#          'i': '••', 'j': '•———', 'k': '—•—', 'l': '•—••',
#          'm': '——', 'n': '—•', 'o': '———', 'p': '•——•',
#          'q': '——•—', 'r': '•—•', 's': '•••', 't': '—',
#          'u': '••—', 'v': '•••—', 'w': '•——', 'x': '—••—',
#          'y': '—•——', 'z': '——••'}
# text = input('Text input:').lower()
# memory_morze = ''
# for i in text:
#     for key, val in morze.items():
#         if key == i:
#             memory_morze += val+' '
# print(f'Morze code: {memory_morze}')
#########################################