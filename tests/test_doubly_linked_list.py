# Test doubly linked list

from app.doubly_linked_list import DoublyLinkedList


class TestDoublyLinkedList:
    def test_dll_initialization(self):
        dll = DoublyLinkedList(4)
        assert dll.head.value == 4
        assert dll.tail.value == 4
        assert dll.head.next is None
        assert dll.head.prev is None
        assert dll.tail.next is None
        assert dll.tail.next is None

    def test_dll_print_list(self):
        dll = DoublyLinkedList(4)
        dll.append(5)
        dll.append(6)
        assert dll.print_list() == "4<->5<->6"

    def test_dll_append(self):
        dll = DoublyLinkedList(4)
        dll.append(5)
        assert dll.length == 2
        assert dll.print_list() == "4<->5"
        # make the length of the list to 0
        dll.length = 0
        dll.append(7)
        assert dll.length == 1
        assert dll.print_list() == "7"

    def test_dll_pop(self):
        dll = DoublyLinkedList(4)
        dll.append(5)
        dll.append(6)
        assert dll.print_list() == "4<->5<->6"
        assert dll.pop().value == 6
        assert dll.print_list() == "4<->5"
        assert dll.pop().value == 5
        assert dll.print_list() == "4"
        assert dll.pop().value == 4
        assert dll.print_list() == ""
        # popping from empty list
        dll.pop()
        assert dll.print_list() == ""

    def test_dll_prepend(self):
        dll = DoublyLinkedList(4)
        assert dll.print_list() == "4"
        dll.prepend(3)
        assert dll.print_list() == "3<->4"
        assert dll.length == 2
        # prepending into an empty list
        dll.length = 0
        dll.prepend(2)
        assert dll.print_list() == "2"
        assert dll.length == 1

    def test_dll_pop_first(self):
        dll = DoublyLinkedList(4)
        dll.append(5)
        assert dll.print_list() == "4<->5"
        assert dll.pop_first().value == 4
        assert dll.print_list() == "5"
        assert dll.pop_first().value == 5
        assert dll.print_list() == ""
        # popping from an empty list
        dll.pop_first()
        assert dll.print_list() == ""

    def test_dll_get_item(self):
        dll = DoublyLinkedList(4)
        dll.append(5)
        dll.prepend(3)
        dll.append(6)
        dll.append(7)
        assert dll.print_list() == "3<->4<->5<->6<->7"
        assert dll.length == 5
        node = dll.get(1)
        assert node.value == 4
        node = dll.get(3)
        assert node.value == 6
        node = dll.get(10)
        assert node is None

    def test_dll_set_item(self):
        dll = DoublyLinkedList(4)
        dll.append(5)
        dll.append(6)
        assert dll.print_list() == "4<->5<->6"
        dll.set_value(0, 3)
        assert dll.print_list() == "3<->5<->6"
        dll.set_value(10, 10)
        assert dll.print_list() == "3<->5<->6"

    def test_dll_insert_item(self):
        dll = DoublyLinkedList(4)
        assert dll.print_list() == "4"
        dll.insert(0, 3)
        assert dll.print_list() == "3<->4"
        dll.insert(2, 5)
        assert dll.print_list() == "3<->4<->5"
        dll.insert(1, 66)
        assert dll.print_list() == "3<->66<->4<->5"
        dll.insert(2, 77)
        assert dll.print_list() == "3<->66<->77<->4<->5"
        # insert out of index
        dll.insert(10, 10)
        assert dll.print_list() == "3<->66<->77<->4<->5"

    def test_dll_remove(self):
        dll = DoublyLinkedList(4)
        dll.append(5)
        dll.append(6)
        dll.append(7)
        dll.append(8)
        assert dll.print_list() == "4<->5<->6<->7<->8"
        dll.remove(0)
        assert dll.print_list() == "5<->6<->7<->8"
        dll.remove(2)
        assert dll.print_list() == "5<->6<->8"
        dll.remove(2)
        assert dll.print_list() == "5<->6"
        dll.remove(10)
        assert dll.print_list() == "5<->6"
