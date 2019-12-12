import random
from Tree import Tree
from Node import Node

# for number_of_numbers in range(5, 100, 5):
#     for repetition in range(5):
#         red_black_tree_1 = Tree()
#         for i in range(number_of_numbers):
#             x = random.randint(1, 20000)
#             red_black_tree_1.add_red_black_node(Node(x))
#         print(f"Number of elements in balanced tree {number_of_numbers}")
#         print(f"Height of balanced tree: {red_black_tree_1.find_tree_depth()}")


number_of_numbers = 85
repetitions = 100
heights = []
for repetition in range(repetitions):
    red_black_tree_1 = Tree()
    for i in range(number_of_numbers):
        x = random.randint(1, number_of_numbers * 5)
        red_black_tree_1.add_red_black_node(Node(x))
    # print(f"Number of elements in balanced tree {number_of_numbers}")
    y =red_black_tree_1.find_tree_depth()
    # print(f"Height of balanced tree: {y}")
    heights.append(y)

print(f"Heights of {repetitions} balanced trees with {number_of_numbers} elements:")
print(heights)