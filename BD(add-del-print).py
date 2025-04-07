
import json

def add_product():
    add = 'y'
    try:
        with open('files\\products.json', 'r') as json_file:
            data_prod = json.load(json_file)
    except FileNotFoundError:
        data_prod = []
    # while add == 'y':
    new_prod = {
        'name_prod': input("Назва товару:"),
        'price_prod': input('Ціна товару:')
        }
        # if add == 'y':
        #     add = input('Бажаєте ще додати товарів до БД? (y - так/n - ні):')

    data_prod.append(new_prod)

    with open('files\\products.json', 'w') as write_file:
        json.dump(data_prod, write_file, indent=4)

def del_product():

    try:
        with open('files\\products.json', 'r') as del_file:
            data_prod = json.load(del_file)
    except FileNotFoundError:
        print('База порожня!')
        return


    num_del_prod = int(input('Введіть номер запису який треба видалити:'))
    data_prod.pop(num_del_prod-1)
    with open('files\\products.json', 'w') as write_file:
        json.dump(data_prod, write_file, indent=4)


def print_product():
    try:
        with open('files\\products.json', 'r') as print_file:
            data_prod = json.load(print_file)
    except FileNotFoundError:
        print('База порожня!')
        return
    for counter, prod in enumerate(data_prod, start=1):
        print(f'{counter}. {prod['name_prod']} -  {prod['price_prod']}')

def main(res='y'):
    while res == 'y':
        add = 'y'
        delete_product = 'y'
        choice = int(input('Виберіть дію: 1 - додати запис, 2 - видалити запис, 3 - друкувати всі записи'))
        if choice == 1:
            while add == 'y':
                add_product()
                if add == 'y':
                    add = input('Бажаєте ще додати товарів до БД? (y - так/n - ні):')
        elif choice == 2:
            while delete_product == 'y':
                del_product()
                if delete_product == 'y':
                    delete_product = input('Бажаєте ще видалити дані з БД? (y - так/n - ні):')
        elif choice == 3:
            print_product()
        if res == 'y':
            res = input('Бажаєте продовжити роботу з БД? (y/n)')

main()