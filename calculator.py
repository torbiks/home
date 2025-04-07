

num1 = float(input('num1 = '))
operation = input('+,-,*,/ = ')
num2 = float(input('num2='))

if operation == '+':
    print(num1+num2)
elif operation =='-':
    print(num1-num2)
elif operation == '*':
    print(num1*num2)
elif operation == '/':
    if num2 != 0:
        print(num1 / num2)
    else:
        print('ne dilymo na null')
    #pass - zaglushka

else:
    print('ERROR')
