# class User:

#     def __init__(self, name):
#         self.name = name
#         self.amount = 0
        

#     def make_deposit(self, amount):
#         self.amount += amount
#         return self

#     def make_withdrawl(self,amount):
#         self.amount -= amount
#         return self

#     def display_user_balance(self):
#         print(f"User: {self.name}, Balance: {self.amount}")
#         return self

#     def transfer_money(self,amount,user):
#         self.amount -= amount
#         user.amount += amount
#         self.display_user_balance()
#         user.display_user_balance()
#         return self


# adrien = User("Adrien")
# nibbles = User("Mr. Nibbles")
# benny_bob = User("Benny Bob")

# adrien.make_deposit(100).make_deposit(200).make_deposit(50).make_withdrawl(45).display_user_balance()

# nibbles.make_deposit(1000).make_deposit(1000).make_withdrawl(500).make_withdrawl(300).display_user_balance()

# benny_bob.make_deposit(1500).make_withdrawl(1000).make_withdrawl(5000).make_withdrawl(3000).display_user_balance()

# nibbles.transfer_money(400, adrien)

class BankAccount:
    # don't forget to add some default values for these parameters!
    def __init__(self, int_rate, balance): 
        # your code here! (remember, instance attributes go here)
        # don't worry about user info here; we'll involve the User class soon
        self.int_rate = int_rate
        self.balance = balance 
    def deposit(self, amount):
        # your code here
        self.balance += amount
        return self
    def withdraw(self, amount):
        # your code here
        if self.balance >= amount:
            self.balance -= amount
        else:
            print("Insufficient funds: Chanrging a $5 fee")
            self.balance -= 5
        return self
    def display_account_info(self):
        # your code here
        print("Balance: $", self.balance, self.int_rate)
        return self
    def yield_interest(self):
        # your code here
        if self.balance>0:
            self.balance += (self.balance * self.int_rate)
            return self
        else:
            return self


account1 = BankAccount (.01,100)
account2 = BankAccount (.02, 200)


account1.deposit(20).deposit(20).deposit(20).deposit(20).withdraw(20).yield_interest().display_account_info()
account2.deposit(30).deposit(30).deposit(30).deposit(30).withdraw(50).yield_interest().display_account_info()


class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = BankAccount(int_rate=0.02, balance=0)
    
    # other methods
    
    def make_deposit(self, amount):
        self.account.deposit(amount)
    
    def make_withdraw(self, amount):
        self.account.withdraw(amount)
    
    def yield_interest(self):
        # your code here
        self.account.yield_interest()

    def display_user_balance(self):
        self.account.display_account_info()
        # print(self.account.balance)
    


user1 = User("Joshua", ("Joshuadiaz@ucsb.edu"))
user1.make_deposit(100)
user1.make_withdraw(50)
user1.yield_interest()
User.display_user_balance(user1)

user2 = User("Nat", ("heyo@ucsb.edu"))
user2.make_deposit(200)
user2.make_withdraw(50)
user2.yield_interest()
User.display_user_balance(user2)


    # your code here
#hello
