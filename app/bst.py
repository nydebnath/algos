# Binary search tree and it's operations


class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self) -> None:
        self.root = None

    def insert(self, value):
        new_node = Node(value)
        if not self.root:
            self.root = new_node
        else:
            temp = self.root
            while True:
                if new_node.value < temp.value:
                    if temp.left is None:
                        temp.left = new_node
                        break
                    temp = temp.left
                elif new_node.value > temp.value:
                    if temp.right is None:
                        temp.right = new_node
                        break
                    temp = temp.right
                else: # when the value of new_node == temp node
                    return False
        return True

    def contains(self, value):
        if not self.root: # no node in tree
            return False
        else:
            temp = self.root
            while temp:
                if value == temp.value:
                    return True
                elif value < temp.value:
                    temp = temp.left
                elif value > temp.value:
                    temp = temp.right
            return False

    