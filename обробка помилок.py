
class MyException(Exception):  # створення власного винятку
    def __str__(self):
        return 'Хеллоу, це моя власна помилка!)'


def raiser(n: int):
    match n:
        case 1:
            raise ValueError  # генерація помилки
        case 2:
            raise FloatingPointError
        case 3:
            raise IndexError('Це мій власний IndexError!🤯')
        case 4:
            raise KeyboardInterrupt
        case 5:
            raise MyException


try:
    raiser(5)

    number_1 = int(input('Введіть число 1: '))  # ValueError
    number_2 = int(input('Введіть число 2: '))  # ValueError

    result = number_1 / number_2  # ZeroDivisionError
    print(result)
except ValueError:  # обробка винятку ValueError
    print('Ви ввели не число!')
except ZeroDivisionError:
    print('Не можна ділити на нуль!')
except ArithmeticError:
    print('Математична помилка!')
except Exception as exc:
    print(f'Сталася помилка: {exc}')
except KeyboardInterrupt:
    print('Ви закрили програму вручну!')
else:  # спрацьовує, якщо не було помилок
    print('ELSE')
finally:  # спрацьовує в будь-якому разі в кінці, навіть якщо помилка не була оброблена except
    print('FINALLY')

# Конструкція для уснування повинна мати: 1 try і або finally, або 1 except