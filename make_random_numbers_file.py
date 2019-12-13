import random

with open('numbers.txt', 'w') as file:
    for i in range(30):
        x = random.randint(1, 100)
        file.write(f"{x}, ")
