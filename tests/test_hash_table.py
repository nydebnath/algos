# Test hash table




from app.hash_table import HashTable


class TestHashTable:

    def test_hash_table_initialization(self):
        hash = HashTable()
        assert hash.data_map == [None] * 7

    def test_set_item(self):
        hash = HashTable()
        hash.set_item("tesla", 369)
        index = hash._HashTable__hash("tesla")
        assert hash.data_map[index][0] == ("tesla", 369)

    def test_get_item(self):
        hash = HashTable()
        hash.set_item("nissan", 567)
        hash.set_item("merc", 900)
        assert hash.get_item("nissan") == 567
        assert hash.get_item("merc") == 900
        # get item not set
        assert hash.get_item("honda") is None

    def test_keys(self):
        hash = HashTable()
        hash.set_item("nissan", 567)
        hash.set_item("merc", 900)
        hash.set_item("tesla", 369)
        assert sorted(hash.keys()) == sorted(["nissan", "merc", "tesla"])
