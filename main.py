from Node import Node
from Tree import Tree

import random


my_tree = Tree()
for i in range(8):
    my_tree.add_node_by_value(random.randint(1, 100))
    #my_tree.add_node_by_value(i)


# my_tree.pretty_print()

my_tree.print_in_order_traversal()
my_tree.pretty_print()


my_tree.rotate_left(my_tree.root)

# my_tree.pretty_print()

my_tree.print_in_order_traversal()
my_tree.pretty_print()