import random

with open('numbers.txt', 'w') as file:
    s = ""
    for i in range(12):
        x = random.randint(1, 100)
        s += f"{x}, "
    file.write(s[:-2])
