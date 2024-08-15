class Product:

    def __init__(self, name: str, quantity: int):
        self.name = name
        self.quantity = quantity

    def increase(self, quantity_given: int) ->None:
        self.quantity += quantity_given

    def decrease(self,quantity_given:int) -> None:
        if self.quantity >= quantity_given:
            self.quantity -= quantity_given

    def __repr__(self):
        return self.name