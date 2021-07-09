# tried to add chaining but I'm not sure it what isn't working
# received error: AttributeError: 'NoneType' object has no attribute 'make_deposit'

# Take a look into modularization if you feel the need to have the 2 classes in separate files.
from bank_account_class import BankAccount


# methods must be called from an instance of a class. 
class User:		# here's what we have so far
    def __init__(self, name, email):
        self.name = name
        self.email = email
        # Update the User class __init__ method
        self.account = BankAccount(int_rate=0.02, balance=0)

    # adding the deposit method
    # Update the User class make_deposit method
    def user_deposit_method(self, amount):	# takes an argument that is the amount of the deposit
    	self.account.deposit(amount)	# the specific user's account increases by the amount of the value received

    # Update the User class make_withdrawal method
    def user_withdraw_method(self, amount):
        self.account.withdraw(amount)

    # Update the User class display_user_balance method
    def user_display_balance_method(self):
        return f"Account Holder: {self.name}, has a balance of: ${self.account.display_account_info()}"

    def transfer_money(self, other_user, amount):
        if amount >=0 and amount < self.account.balance:
            self.account.balance = self.account.balance - amount
            other_user.account.deposit(amount)

# Create 3 instances of the User class
charles = User("Charles van Rotherdam", "cwaharlie@pmail.com")
guido = User("Guido van Rossum", "guido@python.com")
fido = User("fido van Rossum", "fido@python.com")

# Have the first user make 3 deposits and 1 withdrawal and then display their balance
charles.user_deposit_method(100)
charles.user_deposit_method(500)
charles.user_deposit_method(2)
charles.user_withdraw_method(50)
print(charles.user_display_balance_method())

# Have the second user make 2 deposits and 2 withdrawals and then display their balance
guido.user_deposit_method(9)
guido.user_deposit_method(956)
guido.user_withdraw_method(50)
guido.user_withdraw_method(10)
print(guido.user_display_balance_method())


# Have the third user make 1 deposits and 3 withdrawals and then display their balance
fido.user_deposit_method(10000)
fido.user_withdraw_method(50)
fido.user_withdraw_method(50)
fido.user_withdraw_method(2)
print(fido.user_display_balance_method())

# BONUS: Add a transfer_money method; have the first user transfer money to the third user and then print both users' balances
# charles.transfer_money(fido, 10)
# print(charles.display_user_balance())
# print(fido.display_user_balance())

# Because we are calling on the method from the instance, this is known as implicit passage of self. When we call on a method from an instance, that instance, along with all of its information (name, email, balance), is passed in as self.