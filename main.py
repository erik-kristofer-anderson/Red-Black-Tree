from Node import Node
from Tree import Tree

with open('data/numbers.txt') as file:
    numbers = [int(s) for s in file.read().strip().split(',')]

my_balanced_tree = Tree()

for i in numbers:
    node = Node(i)
    my_balanced_tree.add_red_black_node(node, verbose=False)

my_balanced_tree.pretty_print()