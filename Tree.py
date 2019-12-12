from unbalanced_example.Node import Node


class Tree:

    def __init__(self):
        self.root = None

    def __str__(self):
        return f"Tree with root: {self.root}"

    def add_node_by_value(self, value):
        return self.add_node(Node(value))

    def add_node(self, node):
        if self.root is None:
            self.root = node
            # self.root -> children and parent are already None by __init__()
            # self.root -> is also already None
        else:
            curr_node = self.root
            while curr_node:
                if node.value < curr_node.value:
                    if not curr_node.left_child:
                        curr_node.left_child = node
                        node.parent = curr_node
                        curr_node = None
                    else:
                        curr_node = curr_node.left_child
                else:  # in this case, node.value >= curr_node.value
                    if not curr_node.right_child:
                        curr_node.right_child = node
                        node.parent = curr_node
                        curr_node = None
                    else:
                        curr_node = curr_node.right_child
            # children of node are already None

                        # remember add parent references

    def search(self, value):
        """
        searches for a Node with the given value
        :param value:
        :return Node:
        """
        curr_node = self.root
        while curr_node:
            if value == curr_node.value:
                return curr_node
            elif value < curr_node.value:
                curr_node = curr_node.left_child
            else:  # in this case value >= curr_node.value
                curr_node = curr_node.right_child
        return None

    def remove_node(self, value):
        """
        removes the first-found node with the given value
        returns True is node was found and deleted
        :param value:
        :return boolean:
        """
        curr_node = self.root
        while curr_node:
            if curr_node.value == value:
                # remove curr_node
                if (not curr_node.left_child) and (not curr_node.right_child):  # curr_node is leaf
                    if not curr_node.parent:
                        self.root = None
                    elif curr_node.parent.left_child == curr_node:
                        curr_node.parent.left_child = None
                    else:  # in this case curr_node.parent.right_child == curr_node
                        curr_node.parent.right_child = None
                elif curr_node.left_child and (not curr_node.right_child):  # curr_node has left_child only
                    if not curr_node.parent:  # curr_node is root
                        self.root = curr_node.left_child
                    elif curr_node.parent.left_child == curr_node:
                        curr_node.parent.left_child = curr_node.left_child
                    else:  # curr_node.parent.left_child == curr_node
                        curr_node.parent.right_child = curr_node.left_child
                elif (not curr_node.left_child) and curr_node.right_child:  # curr_node has right_child only
                    if not curr_node.parent:
                        self.root = curr_node.right_child
                    elif curr_node.parent.left_child == curr_node:
                        curr_node.parent.left_child = curr_node.right_child
                    else:  # curr_node = curr_node.parent.right_child
                        curr_node.parent.right_child = curr_node.right_child
                else:  # curr_node has left and right children
                    successor = curr_node.right_child
                    while successor.left_child:
                        successor_data = successor.value
                        self.remove_node(successor.value)
                        curr_node.value = successor_data
                return True  # node with value has been removed
            elif curr_node.value < value:
                curr_node = curr_node.right_child
            else:
                curr_node = curr_node.left_child
        return False

    def pretty_print(self):
        """
        function to print a 2D representation of the tree
        source: https://www.geeksforgeeks.org/print-binary-tree-2-dimensions/
        :return None:
        """

        def print_2d_util(curr_node, space):
            my_count = [6]
            if not curr_node:
                return

            space += my_count[0]

            print_2d_util(curr_node.right_child, space)

            print()
            for i in range(my_count[0], space):
                print(end = "  ")
            print(curr_node.value)

            print_2d_util(curr_node.left_child, space)

        count = [10]
        print_2d_util(self.root, 0)

    def in_order_traversal_util(self, curr_node):
        if not curr_node:
            return
        self.in_order_traversal_util(curr_node.left_child)
        print(str(curr_node.value) + ", ", end="")
        self.in_order_traversal_util(curr_node.right_child)

    def print_in_order_traversal(self):
        print("{{ ", end="")
        self.in_order_traversal_util(self.root)
        print("}}")

    @staticmethod
    def set_child_util(parent, which_child, child_node):
        if (which_child != "left") and (which_child != "right"):
            return False
        if which_child == "left":
            parent.left_child = child_node
        else:
            parent.right_child = child_node
        if child_node:
            child_node.parent = parent
        return True

    def replace_child_util(self, parent, current_child, new_child):
        if parent.left_child == current_child:
            return self.set_child_util(parent, "left", new_child)
        elif parent.right_child == current_child:
            return self.set_child_util(parent, "right", new_child)

    def rotate_left(self, node):
        right_left_child = node.right_child.left_child
        if node.parent:
            self.replace_child(node.parent, node, node.right_child)
        else:
            self.root = node.right_child
            self.root.parent = None
        self.set_child_util(node.right_child, "left", node)
        self.set_child_util(node, "right", right_left_child)

    def rotate_right(self, node):
        left_right_child = node.left_child.right_child
        if node.parent:
            self.replace_child_util(node.parent, node, node.left)
        else:
            self.root = node.left_child
            self.root.parent = None
        self.set_child_util(node.left_child, "right", node)
        self.set_child_util(node, "left", left_right_child)




