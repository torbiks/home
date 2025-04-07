import pickle


def load_contact():
    try:
        with open('files\\contact.pkl', 'rb') as file:
            return pickle.load(file)
    except (FileNotFoundError, EOFError):
        return {}


def save_contact(contacts):
    with open('files\\contact.pkl', 'wb') as file:
        pickle.dump(contacts, file)


def add_contact(contacts):
    number = input('Введіть номер телефону: ')
    if number in contacts:
        print('Контакт з таким номером вже існує!')
        return
    name = input('Введіть ім’я: ')
    description = input('Введіть опис: ')
    contacts[number] = {'name': name, 'description': description}
    save_contact(contacts)
    print('Контакт успішно додано!')


def del_contact(contacts):
    number = input('Введіть номер телефону контакту, який потрібно видалити: ')
    if number in contacts:
        del contacts[number]
        save_contact(contacts)
        print('Контакт видалено!')
    else:
        print('Контакт не знайдено.')

def view_contact(contacts):
    if not contacts:
        print('Список контактів порожній.')
    else:
        print('\nСписок контактів:')
        for number, info in contacts.items():
            print(f'Номер: {number}, Ім’я: {info['name']}, Опис: {info['description']}')


def main():
    contacts = load_contact()

    while True:
        print('\nМенеджер контактів:')
        print('1. Додати контакт')
        print('2. Видалити контакт')
        print('3. Показати всі контакти')
        print('4. Вийти')

        choice = input('Оберіть опцію: ')

        if choice == '1':
            add_contact(contacts)
        elif choice == '2':
            del_contact(contacts)
        elif choice == '3':
            view_contact(contacts)
        elif choice == '4':
            print('До побачення!')
            break
        else:
            print('Некоректний вибір, спробуйте ще раз.')

if __name__ == '__main__':
    main()
