from Node import Node
from Tree import Tree
import random
# with open('data/numbers.txt') as file:
#     numbers = [int(s) for s in file.read().strip().split(',')]

numbers = []

for i in range(5):
    x = random.randint(1, 100)
    numbers.append(x)
numbers = [2, 35, 15, 8, 22]

print("***")
print(numbers)
print("***")
my_balanced_tree = Tree()

for i in numbers:
    print("***")
    node = Node(i)
    print(f"ready to add {i}")
    my_balanced_tree.add_red_black_node(node, verbose=True)
    print("*")
    print(f"node {i} was added")

    my_balanced_tree.pretty_print()
    print("***")
    print()

print("done")

my_balanced_tree.pretty_print()

# my_balanced_tree.pretty_print()
# print(f"Number of elements in balanced tree {len(numbers)}")
# print(f"Height of balanced tree: {my_balanced_tree.find_tree_depth()}")

# for num in numbers:
#     my_balanced_tree.remove_node_by_value_rbt(num)
#


# print(my_balanced_tree.find_tree_depth())

# my_balanced_tree.pretty_print()
