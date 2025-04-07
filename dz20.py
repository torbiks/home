import json

def pair_currency():
    add = 'y'
    try:
        with open('files\\currency.json', 'r') as json_file:
            data_currency = json.load(json_file)
    except FileNotFoundError:
        data_currency = []
    while add == 'y':
        new_pair_currency = {
            'number': input('Номер пари:'),
            'name': input("Назва пари:").upper(),
            'currency_quotes': float(input('Котирування пари:'))
        }
        if add == 'y':
            add = input('Бажаєте ще додати пару? (y - так/n - ні):')

        data_currency.append(new_pair_currency)

    with open('files\\currency.json', 'w') as write_file:
        json.dump(data_currency, write_file, indent=4)

def choice_currency():
    with open('files\\currency.json', 'r') as json_file:
        data_currency = json.load(json_file)
    for counter, key in enumerate(data_currency, start=1):
        print(f'{counter}. {key['name']}-->{key['currency_quotes']}')
    try:
        pass
    except ValueError:
        pass

def converter():

    with open('files\\currency.json', 'r') as json_file:
        data_currency = json.load(json_file)
    print("Наразі маємо такі валютні пари:")
    for el in data_currency:
        print(f'{el['number']}. {el['name']}=={el['currency_quotes']}')
    num = int(input('Введіть номер пари для конвертації:'))
    rate = data_currency[num - 1]['currency_quotes']
    babki = int(input("Введіть сумму яку хочете конвертувати:"))
    print(float(rate * babki))


def main(res='y'):
    while res == 'y':
        choice = int(input('Виберіть дію: 1 - додати валютну пару, 2 - конвертувати, 3 - друкувати всі пари'))
        if choice == 1:
            pair_currency()
        elif choice == 2:
            converter()
        elif choice == 3:
            choice_currency()
        if res == 'y':
            res = input('Бажаєте продовжити роботу зі конвертером? (y/n)')

main()
