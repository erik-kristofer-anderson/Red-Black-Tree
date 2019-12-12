import random

with open('numbers.txt', 'w') as file:
    s = ""
    for i in range(10000):
        x = random.randint(1, 20000)
        s += f"{x}, "
    file.write(s[:-2])
