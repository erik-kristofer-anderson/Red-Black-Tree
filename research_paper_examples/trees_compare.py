from Tree import Tree
from Node import Node
numbers = [84, 25, 72, 22, 40, 28, 49, 25, 81, 78, 7, 84, 49]
print(len(numbers))
rbt = Tree()
bst = Tree()
for num in numbers:
    rbt.add_red_black_node(Node(num))
    bst.add_node_by_value(num)

rbt.pretty_print()
bst.pretty_print(red_black=False)