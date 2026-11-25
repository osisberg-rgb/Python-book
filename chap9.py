#9.1

class Restaurant:
    def __init__ (self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restuarant(self):
        print(f"The name of the restaurant is {self.restaurant_name}")
        print(f"The cuisine type is {self.cuisine_type}")

    def open_restaurant(self):
        print(f"{self.restaurant_name} is now open")


res1 = Restaurant("Burger hytten", "American")
res1.describe_restuarant()
res1.open_restaurant()