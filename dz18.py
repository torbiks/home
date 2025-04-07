import json



def add_task():
    add = 'y'
    try:
        with open('files\\tasks.json', 'r') as json_file:  # відкриємо на читання, щоб зберегти попередній зміст
            data_task = json.load(json_file)
    except FileNotFoundError:  # якщо попередньо файлу немає - створюємо порожній список
        data_task = []
    while add == 'y':
        new_task = {
            'number_task': input('Введіть номер задачі:'),
            'name_task': input("Назва:"),
            'text_task': input('Короткий запис задачі:')
        }
        if add == 'y':
            add = input('Бажаєте ще додати задачу до щоденника? (y - так/n - ні:')

        data_task.append(new_task)

    with open('files\\tasks.json', 'w') as write_file:
        json.dump(data_task, write_file, indent=4)

def del_task():
    delete_task = 'y'

    try:
        with open('files\\tasks.json', 'r') as del_file:
            data_task = json.load(del_file)
    except FileNotFoundError:
        print('База порожня!')
        return

    while delete_task == 'y':

        num_del_task = int(input('Введіть номер задачі яку треба видалити:'))

        data_task.pop(num_del_task-1)
        with open('files\\tasks.json', 'w') as write_file:
            json.dump(data_task, write_file, indent=4)
        print(data_task)


        if delete_task == 'y':
            delete_task = input('Бажаєте ще видалити задачу з щоденника? (y - так/n - ні):')

def print_task():
    try:
        with open('files\\tasks.json', 'r') as print_file:
            data_task = json.load(print_file)
    except FileNotFoundError:
        print('База порожня!')
        return

    for counter, task in enumerate(data_task, start=1):
        print(f'{counter}. Задача <<{task['name_task']}>> \n\t--\t {task['text_task']}')




def main(res='y'):
    while res == 'y':
        choice = int(input('Виберіть дію: 1 - додати запис, 2 - видалити запис, 3 - друкувати всі записи'))
        if choice == 1:
            add_task()
        elif choice == 2:
            del_task()
        elif choice == 3:
            print_task()
        if res == 'y':
            res = input('Бажаєте продовжити роботу зі щоденником? (y/n)')

main()

