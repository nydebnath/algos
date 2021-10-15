# Test linked list

from random import randint

from app.linked_list import LinkedList


class TestLinkedList:
    def test_initialize_ll(self):
        ll = LinkedList(4)
        assert ll.head.value == 4
        assert ll.head.next is None
        assert ll.tail.value == 4
        assert ll.tail.next is None
        assert ll.head is ll.tail

    def test_print_ll(self):
        ll = LinkedList(4)
        ll.append(5)
        assert ll.print_list() == "4->5"

    def test_print_ll_with_no_inital_head(self):
        ll = LinkedList(None)
        ll.head = None
        ll.append(5)
        assert ll.print_list() == "5"
        assert ll.head.value == 5
        assert ll.tail.value == 5

    def test_pop_ll(self):
        ll = LinkedList(4)
        ll.append(5)
        ll.append(6)
        assert ll.length == 3
        assert ll.print_list() == "4->5->6"
        popped_node = ll.pop()
        assert popped_node.value == 6
        assert popped_node.next is None
        assert ll.length == 2
        assert ll.print_list() == "4->5"
        ll.pop()
        assert ll.length == 1
        assert ll.print_list() == "4"
        ll.pop()
        assert ll.length == 0
        assert ll.print_list() == ""

    def test_pop_ll_with_zero_length(self):
        ll = LinkedList(4)
        ll.pop()
        assert ll.length == 0
        ll.pop()
        assert ll.length == 0

    def test_prepend_ll(self):
        ll = LinkedList(4)
        ll.prepend(3)
        assert ll.length == 2
        assert ll.print_list() == "3->4"

    def test_prepend_ll_with_no_element(self):
        ll = LinkedList(4)
        ll.pop()
        ll.prepend(3)
        assert ll.length == 1
        assert ll.print_list() == "3"

    def test_