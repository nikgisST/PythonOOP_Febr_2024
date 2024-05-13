class PizzaDelivery:

    def __init__(self, name: str, price: float, ingredients_dict: dict):
        self.name = name
        self.price = price
        self.ingredients = ingredients_dict  # {cheese: 3, peperoni: 2, olives: 3...}
        self.ordered = False

    def get_ordered_message(self):
        return f"Pizza {self.name} already prepared, and we can't make any changes!"

    def add_extra(self, my_ingredient: str, quantity: int, price_per_piece: float) -> str or None:
        if self.ordered:
            return self.get_ordered_message()
        self.ingredients[my_ingredient] = self.ingredients.get(my_ingredient, 0) + quantity   #right
        self.price += quantity * price_per_piece

    def remove_ingredient(self, your_ingredient: str, quantity: int, price_per_slice: float) -> str or None:
        if self.ordered:
            return self.get_ordered_message()  #return int or None
        left_ingr_quantity = self.ingredients.get(your_ingredient)    #reverse

        if not left_ingr_quantity:
            return f"Wrong ingredient selected! We do not use {your_ingredient} in {self.name}!"
        if left_ingr_quantity < quantity:
            return f"Please check again the desired quantity of {your_ingredient}!"
        self.ingredients[your_ingredient] -= quantity
        self.price -= price_per_slice * quantity

    def make_order(self) -> str:
        self.ordered = True
        each_ingredient = ', '.join(f"{k}: {v}" for k, v in self.ingredients.items())
        return f"You've ordered pizza {self.name} prepared with {each_ingredient} and the price " \
               f"will be {self.price}lv."


margarita = PizzaDelivery('Margarita', 11, {'cheese': 2, 'tomatoes': 1})
margarita.add_extra('mozzarella', 1, 0.5)
margarita.add_extra('cheese', 1, 1)
margarita.remove_ingredient('cheese', 1, 1)
print(margarita.remove_ingredient('bacon', 1, 2.5))
print(margarita.remove_ingredient('tomatoes', 2, 0.5))
margarita.remove_ingredient('cheese', 2, 1)
print(margarita.make_order())
print(margarita.add_extra('cheese', 1, 1))