from Tree import Tree
from Node import Node
numbers = [84, 25, 72, 22, 40, 28, 49, 25, 81, 78, 7, 84, 49]
print(len(numbers))
rbt = Tree()
for num in range(1, 21):
    rbt.add_red_black_node(Node(num))

rbt.pretty_print()
print(rbt.find_tree_depth())