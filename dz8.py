num = 1

res = 1

for i in range(1, 21):
    res -= 10
    res += 5
    res *= i ** 3

print(res)