from Node import Node
from Tree import Tree

import random


my_tree = Tree()
for i in range(15):
    my_tree.add_node_by_value(random.randint(1, 100))
my_tree.add_node_by_value(27)

# my_tree.pretty_print()

my_tree.print_in_order_traversal()

new_child_node = Node(38)
old_child_node = my_tree.search(27)

my_tree.replace_child_util(old_child_node.parent, old_child_node, new_child_node)

# my_tree.pretty_print()

my_tree.print_in_order_traversal()