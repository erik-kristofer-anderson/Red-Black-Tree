from Node import Node
from Tree import Tree

with open('data/numbers.txt') as file:
    numbers = [int(s) for s in file.read().strip().split(',')]

numbers = numbers * 10

my_balanced_tree = Tree()

for i in numbers:
    node = Node(i)
    my_balanced_tree.add_red_black_node(node, verbose=False)

# my_balanced_tree.pretty_print()
print(f"Number of elements in balanced tree {len(numbers)}")
print(f"Height of balanced tree: {my_balanced_tree.find_tree_depth()}")

# for num in numbers:
#     my_balanced_tree.remove_node_by_value_rbt(num)
#
# my_balanced_tree.pretty_print()

# print(my_balanced_tree.find_tree_depth())

# my_balanced_tree.pretty_print()