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

    def remove_node_by_node_reference_bst(self, node):
        curr_node = node
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
                self.remove_node_bst(successor.value)
                curr_node.value = successor_data
        return True  # node with value has been removed




    def remove_node_bst(self, value):
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
                        self.remove_node_bst(successor.value)
                        curr_node.value = successor_data
                return True  # node with value has been removed
            elif curr_node.value < value:
                curr_node = curr_node.right_child
            else:
                curr_node = curr_node.left_child
        return False

    def find_tree_depth(self):

        def find_tree_depth_util(node):
            left_height = right_height = 0
            if node.left_child:
                left_height = find_tree_depth_util(node.left_child) + 1
            if node.right_child:
                right_height = find_tree_depth_util(node.right_child) + 1
            return max(left_height, right_height)

        return find_tree_depth_util(self.root)

    def pretty_print(self, red_black=True):
        """
        function to print a 2D representation of the tree
        source: https://www.geeksforgeeks.org/print-binary-tree-2-dimensions/
        :return None:
        """
        tree_height = self.find_tree_depth()

        def print_2d_util(curr_node, space):
            my_count = [6]
            if not curr_node:
                return

            space += my_count[0]

            print_2d_util(curr_node.right_child, space)

            bar = "-" * int(tree_height * my_count[0] * 2.5)
            print(bar)
            # print("---------------------------------------------------------------------------------------"
            #       "----------------------------------")
            for i in range(my_count[0], space):
                print(end="  ")

            if curr_node.color == "red":
                s = ": R"
            else:
                s = ": B"
            if red_black is False:
                s = ""
            print(f"{curr_node.value}{s}")


            print_2d_util(curr_node.left_child, space)


        count = [10]
        print_2d_util(self.root, 0)
        print("---------------------------------------------------------------------------------------"
              "----------------------------------")
        print("===================================================")

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
    def util_set_child(parent, which_child, child_node):
        if (which_child != "left") and (which_child != "right"):
            return False
        if which_child == "left":
            parent.left_child = child_node
        else:
            parent.right_child = child_node
        if child_node:
            child_node.parent = parent
        return True

    def util_replace_child(self, parent, current_child, new_child):
        if parent.left_child == current_child:
            return self.util_set_child(parent, "left", new_child)
        elif parent.right_child == current_child:
            return self.util_set_child(parent, "right", new_child)

    def rotate_left(self, node):
        right_left_child = node.right_child.left_child
        if node.parent:
            self.util_replace_child(node.parent, node, node.right_child)
        else:
            self.root = node.right_child
            self.root.parent = None
        self.util_set_child(node.right_child, "left", node)
        self.util_set_child(node, "right", right_left_child)

    def rotate_right(self, node):
        left_right_child = node.left_child.right_child
        if node.parent:
            self.util_replace_child(node.parent, node, node.left_child)
        else:
            self.root = node.left_child
            self.root.parent = None
        self.util_set_child(node.left_child, "right", node)
        self.util_set_child(node, "left", left_right_child)

    def add_red_black_node(self, node, verbose=False):
        self.add_node(node)
        node.color = "red"
        self.balance_tree(node, verbose)

    @staticmethod
    def util_get_grandparent(node):
        if node.parent is None:
            return None
        return node.parent.parent

    @staticmethod
    def util_get_uncle(node):
        grandparent = None
        if node.parent:
            grandparent = node.parent.parent
        if not grandparent:
            return None
        if grandparent.left_child == node.parent:
            return grandparent.right_child
        else:
            return grandparent.left_child

    def balance_tree(self, node, verbose=False):
        if verbose:
            print('balance_tree line 2')
            self.pretty_print()
        if node.parent is None:
            node.color = "black"
            return
        if node.parent.color == "black":
            return
        parent = node.parent
        grandparent = self.util_get_grandparent(node)
        uncle = self.util_get_uncle(node)
        if uncle and uncle.color == "red":
            parent.color = uncle.color = "black"
            grandparent.color = "red"
            self.balance_tree(grandparent)
            return
        if node == parent.right_child and parent == grandparent.left_child:
            self.rotate_left(parent)
            node = parent
            parent = node.parent
        elif node == parent.left_child and parent == grandparent.right_child:
            self.rotate_right(parent)
            node = parent
            parent = node.parent
        parent.color = "black"
        grandparent.color = "red"
        if node == parent.left_child:
            self.rotate_right(grandparent)
        else:
            self.rotate_left(grandparent)

    def remove_node_rbt(self, node):
        if node.left_child and node.right_child:
            pred_node = self.get_pred_node_rbt(node)
            pred_node_value = pred_node.value
            self.remove_node_rbt(pred_node)
            node.value = pred_node_value
            return
        if node.color == "black":
            self.prepare_for_removal_rbt(node)
        self.remove_node_by_node_reference_bst(node)

    def remove_node_by_value_rbt(self, value):
        node = self.search(value)
        if node:
            self.remove_node_rbt(node)

    @staticmethod
    def get_pred_node_rbt(node):
        node = node.left_child
        while node.right_child:
            node = node.right_child
        return node

    @staticmethod
    def get_sibling_rbt(node):
        if node.parent:
            if node == node.parent.left_child:
                return node.parent.right_child
            return node.parent.left_child
        return None

    @staticmethod
    def is_non_null_and_red_rbt(node):
        if not node:
            return False
        return node.color == "red"

    @staticmethod
    def is_null_or_black_rbt(node):
        if not node:
            return True
        return node.color == "black"

    @staticmethod
    def are_both_children_black_rbt(node):
        if node.left_child and node.left_child.color == "red":
            return False
        if node.right_child and node.right_child.color == "red":
            return False
        return True

    def prepare_for_removal_rbt(self, node):
        if self.try_case_1_rbt(node):
            return

        sibling = self.get_sibling_rbt(node)
        if self.try_case_2_rbt(node, sibling):
            sibling = self.get_sibling_rbt(node)
        if self.try_case_3_rbt(node, sibling):
            return
        if self.try_case_4_rbt(node, sibling):
            return
        if self.try_case_5_rbt(node, sibling):
            sibling = self.get_sibling_rbt(node)
        if self.try_case_6_rbt(node, sibling):
            sibling = self.get_sibling_rbt(node)

        sibling.color = node.parent.color
        node.parent.color = "black"
        if node == node.parent.left_child:
            sibling.right_child.color = "black"
            self.rotate_left(node.parent)
        else:
            sibling.left_child.color = "black"
            self.rotate_right(node.parent)

    @staticmethod
    def try_case_1_rbt(node):
        if node.color == "red" or node.parent == "null":
            return True
        else:
            return False

    def try_case_2_rbt(self, node, sibling):
        if sibling.color == "red":
            node.parent.color = "red"
            sibling.color = "black"
            if node == node.parent.left_child:
                self.rotate_left(node.parent)
            else:
                self.rotate_right(node.parent)
            return True
        return False

    def try_case_3_rbt(self, node, sibling):
        if node.parent.color == "black" and self.are_both_children_black_rbt(sibling):
            sibling.color = "red"
            self.prepare_for_removal_rbt(node.parent)
            return True
        return False

    def try_case_4_rbt(self, node, sibling):
        if node.parent.color == "red" and self.are_both_children_black_rbt(sibling):
            node.parent.color = "black"
            sibling.color = "red"
            return True
        return False

    def try_case_5_rbt(self, node, sibling):
        if self.is_non_null_and_red_rbt(sibling.left_child) and self.is_null_or_black_rbt(sibling.right_child) \
                and node == node.parent.left_child:
            sibling.color = "red"
            sibling.left_child.color = "black"
            self.rotate_right(sibling)
            return True
        return False

    def try_case_6_rbt(self, node, sibling):
        if self.is_null_or_black_rbt(sibling.left_child) and self.is_non_null_and_red_rbt(sibling.right_child) \
                and node == node.parent.right_child:
            sibling.color = "red"
            sibling.right_child.color = "black"
            self.rotate_left(sibling)
            return True
        return False



