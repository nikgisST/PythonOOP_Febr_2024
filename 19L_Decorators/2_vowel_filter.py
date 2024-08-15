def vowel_filter(function):
    def wrapper():             # def wrapper(*args, **kwargs):
        result = function()    # result = function(*args, **kwargs)
        return [el for el in result if el.lower() in 'aeyoui']
    return wrapper

@vowel_filter
def get_letters():
    return ["a", "b", "c", "d", "e"]

print(get_letters())

######################################################3

from functools import wraps

def vowel_filter(function):
    @wraps(function)
    def wrapper():
        result = function()
        return [el for el in result if el.lower() in 'aeyoui']
    return wrapper

@vowel_filter
def get_letters():
    """some docs here"""
    return ["a", "b", "c", "d", "e"]

print(get_letters.__doc__)