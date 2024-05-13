class Shop:
    def __init__(self, name, items):
        # pass
        self.name = name
        self.items = items
        # billa["name"] = ["item1", "item2"]

    def get_items_count(self):
        return len(self.items)


billa = Shop("Billa", ["apple", "bread"])
print(billa.__dict__)  # {}
print(billa.get_items_count())  # 2

