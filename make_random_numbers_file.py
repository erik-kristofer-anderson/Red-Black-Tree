import random

with open('numbers.txt', 'w') as file:
    for i in range(10000):
        x = random.randint(1, 20000)
        file.write(f"{x}, ")
