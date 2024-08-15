from copy import deepcopy

class HashTable:
    def __init__(self):
        self.__keys = [None, None, None, None]
        self.__values = [None, None, None, None]
        self.__length = 4

    @property
    def count(self):
        return len([el for el in self.__keys if el is not None])

    def __len__(self):
        return self.__length

    def __getitem__(self, item):
        try:
            index = self.__keys.index(item)
            return self.__values[index]
        except ValueError:
            raise KeyError("Key does not exist")

    def __setitem__(self, key, value):
        try:
            existing_value_index = self.__keys.index(key)
            self.__values[existing_value_index] = value
        except ValueError:
            if self.count == self.__length:
                self.__resize()               # Resize the lists, so that we have space for the new value
            index = self.__find_index(self.hash(key))
            self.__keys[index] = key
            self.__values[index] = value

    def __find_index(self, index):
        if index == self.__length:
            index = 0
        if self.__keys[index] is None:  # Collision - find the next available spot
            return index
        return self.__find_index(index + 1)

    def hash(self, key: str) -> int:
        return sum([ord(el) for el in key]) % self.__length

    def __resize(self):
        self.__keys = self.__keys + [None] * self.__length
        self.__values = self.__values + [None] * self.__length
        self.__length *= 2

    def get(self, key, return_default_value=None):
        try:
            index = self.__keys.index(key)
            return self.__values[index]
        except ValueError:
            return return_default_value

    def sort(self):
        copy_keys = [el for el in self.__keys if el is not None]
        copy_values = [el for el in self.__values if el is not None]

        result = list(zip(copy_keys, copy_values))
        sorted_result = sorted(result, key=lambda t: t[0])
        table = HashTable()
        table._HashTable__keys = [t[0] for t in sorted_result]
        table._HashTable__values = [t[1] for t in sorted_result]
        table._HashTable__length = self.__length
        diff = self.__length - self.count
        table._HashTable__keys = table._HashTable__keys + [None] * diff
        table._HashTable__values = table._HashTable__values + [None] * diff
        return table

    def add(self, key, value):
        self.__setitem__(key, value)

    def __str__(self):
        result = [
            f"{self.__keys[index]}: {self.__values[index]}"
            for index in range(self.__length)
            if self.__keys[index] is not None]
        return "{" + ", ".join(result) + "}"


table = HashTable()
table["name"] = "Peter"
table["age"] = 25
table["id"] = 1
table["city"] = "Plovdiv"
table["street"] = "Markovo Tepe"
table["name"] = "Test"

print(table)
sorted_table = table.sort()
print(type(table))
print(type(sorted_table))
# print(table.get("name"))
# print(table.get("asd", "Me"))
# table.add("number", "8")
print(table["age"])
print(len(table))
print(table.count)
sorted_table.add("new_key", 8)
print(sorted_table)