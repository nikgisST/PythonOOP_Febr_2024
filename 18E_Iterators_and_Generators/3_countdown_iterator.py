class countdown_iterator:

    def __init__(self, count: int):
        self.count = count + 1
        # self.original_count = count
        # self.count = self.original_count + 1

    def __iter__(self):
        # self.count = self.original_count
        return self

    def __next__(self):
        if self.count <= 0:
            raise StopIteration

        self.count -= 1

        return self.count


#iterator = countdown_iterator(10)
#for el in iterator:
    #print(el)

for el in countdown_iterator(10):
    print(el)