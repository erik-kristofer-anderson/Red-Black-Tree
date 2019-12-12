class Node:
    def __init__(self, value=0, left_child=None, right_child=None, parent=None, color=None):
        self.value = value
        self.left_child = left_child
        self.right_child = right_child
        self.parent = parent
        self.color = color

    def __str__(self):
        return f"Node with value {self.value} and color {self.color}"
