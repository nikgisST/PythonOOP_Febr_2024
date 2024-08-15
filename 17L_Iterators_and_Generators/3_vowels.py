class vowels:

    def __init__(self, string):
        self.string = string
        self.vowels_list = ['a', 'e', 'i', 'u', 'y', 'o']
        self.index = -1

    def __iter__(self):
        return self

    def __next__(self):
        self.index += 1
        if self.index < len(self.string):
            if self.string[self.index].lower() in self.vowels_list:
                return self.string[self.index]
        raise StopIteration

my_string = vowels('AbcedifutyOo')
for char in my_string:
    print(char)

################################################################

class vowels:

    def __init__(self, string):
        self.string = string
        self.vowels_list = ['a', 'e', 'i', 'u', 'y', 'o']
        self.index = -1
        self.vowels_values = [c for c in self.string if c.lowe() in self.vowels_list]

    def __iter__(self):
        return self
        #return iter(self.vowels_values)

    def __next__(self):
        self.index += 1
        if self.index < len(self.vowels_values):
            return self.vowels_values[self.index]
        raise StopIteration

my_string = vowels('AbcedifutyOo')
for char in my_string:
    print(char)