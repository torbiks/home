# def numbers_sorted (inp: str, output_file = 'files\\result.txt'):
#     numbers = []
#     with open(inp, 'r') as read_file:
#         for line in read_file:
#             line_split = line.split()
#             numbers.extend(int(el) for el in line_split)
#
#     #     file_lines = [line for line in read_file.readlines() if line.strip() !='\n']
#     # for line in file_lines:
#     #     numbers.extend(map(int, line.split()))
#     numbers.sort()
#     with open(output_file, 'w') as write_file:
#         print(*numbers, sep='\n', file=write_file)
#
# # numbers_sorted('files\\data.txt')
#
#
# def format(input_file_path: str):
#     with open(input_file_path, 'r') as read_file:
#         lines = read_file.readlines()
#
#     with open(input_file_path, 'w') as write_file:
#         for line in lines:
#             if line.strip():
#                 print(line, file=write_file, end='')
#             else:
#                 print('==============\n', file=write_file, end='')
#
# format('files\\data2.txt')

# def average_score(grades):
#     if grades:
#         return sum(grades) / len(grades)
#     return 0
#
# with open('file2.txt', 'r') as infile:
#     students = infile.readlines()
#
# good_students = []
#
# for student in students:
#     data = student.split()
#     surname = data[0]
#     grades = list(map(int, data[2:]))
#
#     avg = average_score(grades)
#
#     if avg > 6:
#         good_students.append(surname)
#
# with open('output.txt', 'w') as outfile:
#     for surname in good_students:
#         outfile.write(surname + '\n')

def get_best_students(input_file_path: str):
    with open(input_file_path, 'r') as read_file:
        with open('files\\output.txt', 'w') as write_file:
            for line in read_file:
                split = line.split()

                name = split[0]
                grades = list(map(int, split[2:]))

                if sum(grades) / len(grades) > 6:
                    print(name, file=write_file)




