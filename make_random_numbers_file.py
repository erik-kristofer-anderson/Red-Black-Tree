import random

with open('numbers2.txt', 'w') as file:
    for i in range(25):
        x = random.randint(1, 100)
        file.write(f"{x}, ")
