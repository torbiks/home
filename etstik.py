def copypaste(text: str, n: int):
    print(text * n)
    return

copypaste('I love coding', 3)


def powers(n: int):
    dictionare = {}
    for i in range(1, n+1):
        if i <= n:
            dictionare.setdefault(i, i * i)
    print(f'{dictionare}')
    return

powers(10)

def add_string(str1: str, str2: str):
    d = len(str1)
    print(d)


    return
add_string('{{}}', hellomit)