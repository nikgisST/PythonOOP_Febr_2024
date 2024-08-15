def fibonacci():
    n1, n2 = 0, 1     # 0, 1, 0 + 1 = 1  1 + 1 = 2, 1 + 2 = 3

    while True:
        yield n1
        n1, n2 = n2, n1 + n2


generator = fibonacci()

for _ in range(5):
    print(next(generator))
