class Stack:
    def __init__(self):
        self.data = []

    def push(self, el):
        self.data.append(el)

    def pop(self):
        return self.data.pop()

    def top(self):
        return self.data[-1]

    def is_empty(self):
        #return False if self.data else True
        return not self.data

    def __str__(self):
        reversed_data = reversed(self.data)
        result = ", ".join(reversed_data)
        return f"[{result}]"


s = Stack()
print(s.is_empty())
s.push("5")
s.push("6")
print(s.top())
s.push("7")
print(s.top())
print(s.is_empty())
print(s)
s.pop()
print(s)
# test zero
# import unittest
# class StackTests(unittest.TestCase):
#     def test_zero(self):
#         stack = Stack()
#         stack.push("apple")
#         stack.push("carrot")
#         self.assertEqual(str(stack), '[carrot, apple]')
#         self.assertEqual(stack.pop(), 'carrot')
#         self.assertEqual(stack.top(), 'apple')
#         stack.push("cucumber")
#         self.assertEqual(str(stack), '[cucumber, apple]')
#         self.assertEqual(stack.is_empty(), False)
#
#
# if __name__ == '__main__':
#     unittest.main()

