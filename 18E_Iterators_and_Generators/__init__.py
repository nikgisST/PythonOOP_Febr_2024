# iterator

class MyList:
    def __init__(self, my_list: list):
        self.my_list = my_list
        self.index = -1

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == len(self.my_list) - 1:
            raise StopIteration
        self.index += 1
        return self.my_list[self.index]


iterator = MyList([1, 2, 3]).__iter__()

while True:
    try:
        print(next(iterator))
    except StopIteration:
        break


# generator

def numbers_multiplied_by_two(numbers: list):
    for number in numbers:
        yield number * 2

a = numbers_multiplied_by_two([1, 2, 3])
print(next(a))    # 2
print(next(a))    # 4

a = (number * 2 for number in [1, 2, 3])

a = ', '.join(str(x) for x in [1, 2, 3])