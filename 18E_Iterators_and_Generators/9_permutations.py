from itertools import permutations


def possible_permutations(elements: list):
    #return permutations(elements)
    permuted = permutations(elements)      # returns tuple
    for el in permuted:
        yield list(el)


[print(n) for n in possible_permutations([1, 2, 3])]