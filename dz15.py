task = []

def add_task(n, nt, dt, done_t):

    task.append({'id_task': n, 'name_task': nt, 'description_task': dt, 'done_task': done_t})
    print()

# def update_task(n, nt, dt, done_t):
#     for el in task:
#         if el['n'] == '1':

def del_task(n: int):
    n = n-1
    delete_item = task.pop(n)

def main():
    while True:
        choice = input('Введіть одну із команд(add - добавити завдання, del - видалити завдання, all-вивести всі завдання, q - вихід з програми: ')
        if choice == 'del':
            del_task(n=int(input('Вкажіть номер завдання для видалення:')))
        if choice == 'add':
            add_task(n=input('Number task:'), nt=input('Name task:'), dt=input('Description:'), done_t=input('Done task:'))
        # if choice == 'upd':
        #     update_task()
        if choice == 'all':
            print(f'Завдання які є в Вашому списку:')
            if task == []:
                print("Список пустий")
            # print(' ID  NAME  DESCRIPTION        ')
            # print('_______________________________')
            for item in task:
                print(f'{item['id_task']}. {item['name_task']} \n\t > Опис завдання: {item['description_task']}\n \t > Стадія виконання: {item['done_task']}\n ')
        if choice == 'q':
            print('Всього найкращого!!')
            break



main()

