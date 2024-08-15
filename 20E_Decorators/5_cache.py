def cache(func):
    def wrapper(num):
        if not wrapper.log.get(num):  # 0(1)
            wrapper.log[num] = func(num)
        return wrapper.log[num]
    wrapper.log = {}
    return wrapper

@cache
def fibonacci(n):
    if n < 2:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


fibonacci(3)
print(fibonacci.log)


#############################################################

class Fibonacci:
    def __init__(self):
        self.cache = {}
    def __call__(self, n):
        if n not in self.cache:
            if n == 0:
                self.cache[0] = 0
            elif n == 1:
                self.cache[1] = 1
            else:
                self.cache[n] = self.cache[n-1] + self.cache[n-2]   # = self(n-1) + self(n-2)
        return self.cache[n]

fib = Fibonacci()
for i in range(5):
    print(fib(i))
print((fib.cache))