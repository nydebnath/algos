# Test linked list

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

    def test_pop_first_ll(self):
        ll = LinkedList(4)
        ll.append(5)
        assert ll.print_list() == "4->5"
        # pop first element
        ll.pop_first()
        assert ll.print_list() == "5"
        assert ll.length == 1
        # pop first with one element
        ll.pop_first()
        assert ll.print_list() == ""
        assert ll.length == 0
        # pop first with no element
        ll.pop_first()
        assert ll.print_list() == ""
        assert ll.length == 0

    def test_get_ll_with_index(self):
        ll = LinkedList(4)
        ll.append(5)
        ll.append(6)
        ll.append(7)
        assert ll.print_list() == "4->5->6->7"
        assert ll.get(2).value == 6
        assert ll.get(3).value == 7
        ll.pop_first()
        assert ll.get(2).value == 7
        ll.pop()
        assert ll.get(2) == None
        ll.pop()
        # one element
        assert ll.get(0).value == 5
        ll.pop()
        # get on ll with no element
        assert ll.get(0) == None

    def test_set_value_ll_with_index(self):
        ll = LinkedList(4)
        ll.append(5)
        ll.append(6)
        ll.append(7)
        assert ll.print_list() == "4->5->6->7"
        ll.set_value(0, 3)
        assert ll.print_list() == "3->5->6->7"
        ll.set_value(2, 8)
        assert ll.print_list() == "3->5->8->7"
        ll.set_value(10, 10)
        assert ll.print_list() == "3->5->8->7"
        for _ in range(ll.length):
            ll.pop()
        ll.set_value(0, 1)
        assert ll.print_list() == ""

    def test_insert_ll(self):
        ll = LinkedList(4)
        ll.insert(0, 3)
        assert ll.print_list() == "3->4"
        ll.insert(2, 6)
        assert ll.print_list() == "3->4->6"
        ll.insert(2, 5)
        assert ll.print_list() == "3->4->5->6"
        assert ll.insert(10, 7) == ll.insert(-2, 0) == False

    def test_remove_ll(self):
        ll = LinkedList(4)
        ll.append(5)
        ll.append(6)
        ll.append(7)
        ll.append(8)
        assert ll.print_list() == "4->5->6->7->8"
        ll.remove(2)
        assert ll.print_list() == "4->5->7->8"
        ll.remove(0)
        assert ll.print_list() == "5->7->8"
        ll.remove(1)
        assert ll.print_list() == "5->8"
        ll.remove(1)
        assert ll.print_list() == "5"
        ll.remove(0)
        assert ll.print_list() == ""
        assert ll.remove(3) == False

    def test_ll_reverse(self):
        ll = LinkedList(4)
        ll.append(5)
        ll.append(6)
        ll.append(7)
        assert ll.print_list() == "4->5->6->7"
        ll.reverse()
        assert ll.print_list() == "7->6->5->4"
