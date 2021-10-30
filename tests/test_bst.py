# Test binary search tree

from app.bst import BinarySearchTree


class TestBinarySearchTree:
    def test_bst_initialization(self):
        bst = BinarySearchTree()
        assert bst.root is None

    def test_bst_insert(self):
        bst = BinarySearchTree()
        bst.insert(4)
        assert bst.root.value == 4
        assert bst.root.left is None
        assert bst.root.right is None
        bst.insert(2)
        assert bst.root.value == 4
        assert bst.root.left.value == 2
        assert bst.root.right is None
        bst.insert(7)
        assert bst.root.value == 4
        assert bst.root.left.value == 2
        assert bst.root.right.value == 7
        bst.insert(3)
        assert bst.root.left.right.value == 3
        bst.insert(1)
        assert bst.root.left.left.value == 1
        bst.insert(10)
        assert bst.root.right.right.value == 10
        bst.insert(6)
        assert bst.root.right.left.value == 6
        value = bst.insert(6) # inserting value that already exists
        assert value is False

    def test_bst_contains(self):
        bst = BinarySearchTree()
        bst.insert(4)
        bst.insert(2)
        bst.insert(7)
        bst.insert(3)
        bst.insert(1)
        bst.insert(10)
        bst.insert(6)
        assert bst.contains(3) is True
        assert bst.contains(10) is True
        assert bst.contains(7) is True
        assert bst.contains(4) is True
        assert bst.contains(6) is True
        # value not available
        assert bst.contains(100) is False

    def test_bst_no_node_contains(self):
        bst = BinarySearchTree()
        assert bst.contains(6) is False