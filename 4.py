t = int(input("Введите целое положительное число n = "))
m = t % 10
t = t // 10
while t > 0:
    if t % 10 > m:
        m = t % 10
    t = t // 10
print(f"Самое большое число {m}")
