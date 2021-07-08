# methods must be called from an instance of a class. 
class User:		# here's what we have so far
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account_balance = 0
    # adding the deposit method
    def make_deposit(self, amount):	# takes an argument that is the amount of the deposit
    	self.account_balance += amount	# the specific user's account increases by the amount of the value received

    def make_withdrawal(self, amount):
        self.account_balance -= amount

    def display_user_balance(self):
        return f"Account Holder: {self.name}, has a balance of: ${self.account_balance}"

    def transfer_money(self, other_user, amount):
        if amount >=0 and amount < self.account_balance:
            self.account_balance = self.account_balance - amount
            other_user.make_deposit(amount)

# Create 3 instances of the User class
charles = User("Charles van Rotherdam", "charlie@pmail.com")
guido = User("Guido van Rossum", "guido@python.com")
fido = User("fido van Rossum", "fido@python.com")

# Have the first user make 3 deposits and 1 withdrawal and then display their balance
charles.make_deposit(100)
charles.make_deposit(500)
charles.make_deposit(2)
charles.make_withdrawal(50)
print(charles.display_user_balance())

# Have the second user make 2 deposits and 2 withdrawals and then display their balance
guido.make_deposit(9)
guido.make_deposit(956)
guido.make_withdrawal(50)
guido.make_withdrawal(10)
print(guido.display_user_balance())


# Have the third user make 1 deposits and 3 withdrawals and then display their balance
fido.make_deposit(10000)
fido.make_withdrawal(50)
fido.make_withdrawal(50)
fido.make_withdrawal(2)
print(fido.display_user_balance())

# BONUS: Add a transfer_money method; have the first user transfer money to the third user and then print both users' balances
charles.transfer_money(fido, 10)
print(charles.display_user_balance())
print(fido.display_user_balance())

# Because we are calling on the method from the instance, this is known as implicit passage of self. When we call on a method from an instance, that instance, along with all of its information (name, email, balance), is passed in as self.