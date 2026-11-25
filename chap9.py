# #9.1 make a restaurant class

# class Restaurant:
#     def __init__ (self, restaurant_name, cuisine_type):
#         self.restaurant_name = restaurant_name
#         self.cuisine_type = cuisine_type

#     def describe_restuarant(self):
#         print(f"The name of the restaurant is {self.restaurant_name}")
#         print(f"The cuisine type is {self.cuisine_type}")

#     def open_restaurant(self):
#         print(f"{self.restaurant_name} is now open")



# #9.2 make 3 intances of a restaurant

# res1 = Restaurant("Dennys", "American")
# res1.describe_restuarant()

# res2 = Restaurant("Jimmy jones", "Sandwich")
# res2.describe_restuarant()

# res3 = Restaurant("McD", "fast food")
# res3.describe_restuarant()


#9.3 make a user class

# class User:

#     def __init__(self, first_name, last_name):
#         self.first_name = first_name
#         self.last_name = last_name

#     def describe_user(self):
#         print(f"Users name is {self.first_name} {self.last_name}")

#     def greet_user(self): 
#         print(f"Hiii {self.first_name}, I hope you are going to enjoy the experience")

# user1 = User("Oscar", "Isberg")
# user1.describe_user()
# user1.greet_user()


#9.4 Number served
class Restaurant:
    def __init__ (self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restuarant(self):
        print(f"The name of the restaurant is {self.restaurant_name}")
        print(f"The cuisine type is {self.cuisine_type}")


    def open_restaurant(self):
        print(f"{self.restaurant_name} is now open")

    def set_number_served(self, number):
        if number <= self.number_served:
            return self.number_served
        else: 
            self.number_served = number

    def increment_number_served(self):
        print(f"You have served this many people today: {self.number_served}")

res_new = Restaurant("Burger john", "American")
res_new.set_number_served(10)
res_new.describe_restuarant()

res_new.increment_number_served()