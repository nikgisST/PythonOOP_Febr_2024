def solution():

    def integers():
        num: int = 1
        while True:
            yield num
            num += 1

    def halves():
        for i in integers():  # for цикъла връща next на integers() генератора и каквото ми върне го пази в i
            yield i / 2

    def take(n, seq_of_halves):
        return [next(seq_of_halves) for _ in range(n)]  # seq е или integers(), или halves()

    return take, halves, integers


#print(solution())
take = solution()[0]
halves = solution()[1]
print(take(5, halves()))

# generator = halves()
# print(next(generator))
# print(next(generator))
# print(next(generator))
# print(next(generator))
# print(next(generator))