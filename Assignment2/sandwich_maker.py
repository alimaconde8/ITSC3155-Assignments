class SandwichMaker:
    def __init__(self, resources):
        self.machine_resources = resources

    def check_resources(self, ingredients):
        """Returns True when order can be made, False if ingredients are insufficient."""
        for ingredient, required_amount in ingredients.items():
            if self.machine_resources[ingredient] < required_amount:
                return False
        return True

    def make_sandwich(self, sandwich_size, order_ingredients):
        if self.check_resources(order_ingredients):
            for ingredient, required_amount in order_ingredients.items():
                self.machine_resources[ingredient] -= required_amount
            print(f"{sandwich_size} sandwich made successfully!")
        else:
            print("Insufficient resources to make the sandwich.")
