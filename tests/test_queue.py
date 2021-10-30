# Test queue

from app.queue import Queue


class TestQueue:
    def test_queue_initialization(self):
        q = Queue(4)
        assert q.first.value == 4
        assert q.last.value == 4
        assert q.length == 1

    def test_queue_print(self):
        q = Queue(4)
        assert q.print_queue() == "4"

    def test_queue_add_item(self):
        q = Queue(4)
        q.enqueue(5)
        assert q.print_queue() == "4->5"
        q.length = 0  # no element
        q.enqueue(6)
        q.enqueue(7)
        assert q.print_queue() == "6->7"

    def test_queue_remove_item(self):
        q = Queue(4)
        q.enqueue(5)
        q.enqueue(6)
        assert q.print_queue() == "4->5->6"
        q.dequeue()
        assert q.print_queue() == "5->6"
        q.dequeue()
        assert q.print_queue() == "6"
        q.dequeue()
        assert q.print_queue() == ""
        # no element
        q.dequeue()
        assert q.print_queue() == ""
