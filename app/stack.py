# Stacks and it's operations


class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.next = None


class Stack:
    def __init__(self, value) -> None:
        new_node = Node(value)
        self.top = new_node
        self.height = 1

    def print_stack(self):
        result = list()
        temp = self.top
        for _ in range(self.height):
            result.append(temp.value)
            temp = temp.next
        return "<-".join(str(i) for i in result)

    def push(self, value):  # just like `prepend` in linked list O(1)
        new_node = Node(value)
        if self.height != 0:
            new_node.next = self.top
        self.top = new_node
        self.height += 1

    def pop(self):  # just like `pop_first` in linked list O(1)
        if self.height == 0:
            return None
        elif self.height == 1:
            temp = self.top
            temp.next = None
            self.top = None
        else:
            temp = self.top
            self.top = temp.next
            temp.next = None
        self.height -= 1
        return temp
