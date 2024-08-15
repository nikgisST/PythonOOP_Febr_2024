def even_numbers(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return [el for el in result if el % 2 == 0]   # el % 2 без нищо връща нечетните
    return wrapper


@even_numbers
def get_numbers(numbers):
    return numbers
print(get_numbers([1, 2, 3, 4, 5]))



def even_numbers(func):
    def wrapper(*args, **kwargs):
        result = [el for el in args if el % 2 == 0]
        return func(result)
    return wrapper

@even_numbers
def get_numbers(numbers):
    return numbers
print(get_numbers([1, 2, 3, 4, 5]))