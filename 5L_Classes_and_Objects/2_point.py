class Point:

    def __init__(self, x_coord, y_coord):   #instance methods === self
        self.x = x_coord
        self.y = y_coord

    def set_x(self, new_coord):    #instance methods === self
        self.x = new_coord

    def set_y(self, new_coord):   #instance methods === self
        self.y = new_coord

    def __str__(self):            # първо търси str method --> repr --> object location
        return f"The point has coordinates ({self.x},{self.y})"


p = Point(2, 4)
print(p)
p.set_x(3)
p.set_y(5)
print(p)
