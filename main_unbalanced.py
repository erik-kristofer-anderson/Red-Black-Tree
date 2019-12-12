
from Tree import Tree
# import random
with open('data/numbers.txt') as file:
    numbers = [int(s) for s in file.read().strip().split(',')]

my_tree = Tree()

for i in numbers:
    my_tree.add_node_by_value(i)

my_tree.pretty_print(red_black=False)

