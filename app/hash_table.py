# Hash table and it's operations


class HashTable:
    def __init__(self, size=7) -> None:
        self.data_map = [None] * size

    def __hash(self, key):
        my_hash = 0
        for letter in key:
            my_hash = (my_hash + ord(letter) * 23) % len(self.data_map)
        return my_hash

    def set_item(self, key, value):
        index = self.__hash(key)
        if not self.data_map[index]:
            self.data_map[index] = []
        self.data_map[index].append((key, value))

    def get_item(self, key):
        index = self.__hash(key)
        if self.data_map[index]:
            for item in self.data_map[index]:
                if item[0] == key:
                    return item[1]
        return None

    def keys(self):
        result = []
        for rec in self.data_map:
            if rec:
                for item in rec:
                    result.append(item[0])
        return result