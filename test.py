room = [['*'] * 5 for _ in range(5)]
room[2][2] = 'R'

for row in room:
    print(" ".join(row))
print()

while True:
    command = input("Введіть команду (<Напрям> <Кількість клітинок>) або 0 для виходу: ")
    if command == "0":
        break

    parts = command.split()
    if len(parts) != 2 or not parts[1].isdigit():
        print("Невірний формат команди. Спробуйте ще раз.")
        continue

    direction, steps = parts[0].upper(), int(parts[1])
    if direction not in ["UP", "DOWN", "LEFT", "RIGHT"]:
        print("Невірний напрям. Використовуйте UP, DOWN, LEFT або RIGHT.")
        continue

    for i in range(len(room)):
        for j in range(len(room[i])):
            if room[i][j] == 'R':
                r_x, r_y = i, j
                break

    room[r_x][r_y] = '*'

    if direction == "UP":
        r_x = max(0, r_x - steps)
    elif direction == "DOWN":
        r_x = min(4, r_x + steps)
    elif direction == "LEFT":
        r_y = max(0, r_y - steps)
    elif direction == "RIGHT":
        r_y = min(4, r_y + steps)

    room[r_x][r_y] = 'R'

    for row in room:
        print(" ".join(row))
    print()

print("Остаточне положення робота:")
for row in room:
    print(" ".join(row))
