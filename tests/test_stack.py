# Test stacks

from app.stack import Stack


class TestStacks:
    def test_stack_initialzation(self):
        s = Stack(4)
        assert s.top.value == 4
        assert s.height == 1

    def test_stack_print(self):
        s = Stack(4)
        assert s.print_stack() == "4"

    def test_stack_push(self):
        s = Stack(4)
        s.push(5)
        s.push(6)
        assert s.print_stack() == "6<-5<-4"
        assert s.height == 3
        s.height = 0
        s.push(7)
        assert s.print_stack() == "7"

    def test_stack_pop(self):
        s = Stack(4)
        s.push(5)
        s.push(6)
        assert s.print_stack() == "6<-5<-4"
        s.pop()
        assert s.print_stack() == "5<-4"
        s.pop()
        assert s.print_stack() == "4"
        s.pop()
        assert s.print_stack() == ""
        s.pop()
        assert s.print_stack() == ""
