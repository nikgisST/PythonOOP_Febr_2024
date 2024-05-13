class Phone:      # : this defines the SCOPE

    # State                               # __init__ - конструктор, инициализатора
    def __init__(self, color, size):      # thunder method/ magic method    # self === p1 или self === p2
        self.color = color   # attribute
        self.size = size     # attribute

    # Behivior
    def turn_on(self):                   # public method, self дава шанс да се използва методът през инстанцията
        return "The phone is turned on"


p1 = Phone("green", 2)      # instance __init__ is called only by brackets ()
p2 = Phone("red", 10)       # instance===object===вдигане на инстанция
print(p1.size)      # 2
print(p1.color)     # green
print(p2.color)     # red
print(p1.turn_on())         # The phone e is turned on
p3 = Phone("green", 2)
print(id(p1))   #2302920785872
print(id(p2))   #2302920785584
print(id(p3))   #2302920785488

phone_dict = {"size": 4, "color": "blue"}
print(phone_dict["color"])    # blue