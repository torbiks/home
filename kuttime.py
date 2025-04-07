# Программа для розрахунку кута між стрілками годиника у вказаний час користувачем

def clock_angle(hours: int, minutes: int) -> float:
    # Переконуємось, що години знаходяться в діапазоні 1-12
    hours = hours % 12

    # Кут, який проходить хвилинна стрілка за одну хвилину
    minute_angle = 6 * minutes

    # Кут, який проходить годинникова стрілка за одну хвилину
    hour_angle = 30 * hours + 0.5 * minutes

    # Обчислення різниці між кутами
    angle = abs(hour_angle - minute_angle)

    # Вибір найменшого кута між двома можливими
    return min(angle, 360 - angle)


# Приклад використання
hours = int(input("Введіть години: "))
minutes = int(input("Введіть хвилини: "))
print(f"Кут між стрілками: {clock_angle(hours, minutes)} градусів")