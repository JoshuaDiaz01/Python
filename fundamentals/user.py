# class User:
#     def __init__(self):
#         self.first_name = "Joshua"
#         self.last_name = "Diaz"
#         self.age = 22

# print("Hello")

# user_josh = User() #this line will call function and assign all attributes to user_josh
# print(user_josh.first_name) 

# user_2 = User()
# print(user_2.first_name)




# class Shoe:
#     # now our method has 4 parameters (including self)!
#     def __init__(self, brand, shoe_type, price):
# # we assign them accordingly
#         self.brand = brand
#         self.type = shoe_type
#         self.price = price
#         self.in_stock = True

#     def on_sale_by_percent(self, percent): # must always include self in argument
#         self.price = self.price * (1 - percent) 

# skater_shoe = Shoe("Vans", "Low-top Trainers", 59.99) #This is in sequential order 
# dress_shoe = Shoe("Jack & Jill Bootery", "Ballet Flats", 29.99) #This is in sequential order 
# print(skater_shoe.price)	# output: Low-top Trainers
# # print(dress_shoe.type)	# output: Ballet Flats

# skater_shoe.on_sale_by_percent(0.2)
# dress_shoe.on_sale_by_percent(0.5)
# print(skater_shoe.price)
# print(dress_shoe.price)





class User:
    def __init__(self, first_name,last_name, email, age):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.is_rewards_member = False # this is an attribute
        self.gold_card_points = 0 # this is an attribute

#methods
    def display_info(self):
        print(f"First name: {self.first_name}")
        print(f"Last name: {self.last_name}")
        print(f"Email: {self.email}")
        print(f"Age: {self.age}")
        print(f"Member: {self.is_rewards_member}")
        print(f"Current Points: {self.gold_card_points}")
        print("=====================")

    def enroll(self):
        self.is_rewards_member = True
        self.gold_card_points = 200
        if self.is_rewards_member:
            print('User already a member.')
            return False

    def spend_points(self, amount):
        #Add logic in the spend points method to be sure they have enough points to spend that amount and handle appropriately.
        if self.gold_card_points < amount:
            print("You dont have enough points")
            return
        self.gold_card_points = (self.gold_card_points - amount)



#calling users details
my_user = User('Joshua', 'Diaz', 'joshuadiaz@gmail.com', '22')
my_user.enroll()
my_user.spend_points(50)
my_user.display_info()

second_user = User ('nat', 'diaz', 'fakeemail@gmail.com', 27)
second_user.enroll()
second_user.spend_points(80)
second_user.display_info()




#     # adding the greeting method
#     def greeting(self): #passing object into method
#     	print(f"Hello, my name is {self.first_name}")

# adrien = User("Joshua", "Diaz",22) #implementing object
# adrien.greeting() #calling on function





