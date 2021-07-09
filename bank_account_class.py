# from bank_user_class import User

# The BankAccount class should have a balance. When a new BankAccount instance is created, if an amount is given, the balance of the account should initially be set to that amount; otherwise, the balance should start at $0. The account should also have an interest rate, saved as a decimal (i.e. 1% would be saved as 0.01), which should be provided upon instantiation. (Hint: when using default values in parameters, the order of parameters matters!)

class BankAccount:
    # don't forget to add some default values for these parameters!
    def __init__(self, int_rate, balance): 
        # your code here! (remember, instance attributes go here)
        self.int_rate = int_rate
        self.balance = 0

        # don't worry about user info here; we'll involve the User class soon
    def deposit(self, amount):
        # deposit(self, amount) - increases the account balance by the given amount
        # your code here
        self.balance += amount

    def withdraw(self, amount):
        # withdraw(self, amount) - decreases the account balance by the given amount if there are sufficient funds; if there is not enough money, print a message "Insufficient funds: Charging a $5 fee" and deduct $5
        # your code here
        if (self.balance - amount) > 0:
    	    self.balance -= amount
        else:
    	    print("INSUFFICIENT FUNDS")
    	return self

    def display_account_info(self):
        # display_account_info(self) - print to the console: eg. "Balance: $100"
        # your code here
        return f"Balance: ${self.balance} - Interest Rate: {self.int_rate * 100}%"

    def yield_interest(self):
        # yield_interest(self) - increases the account balance by the current balance * the interest rate (as long as the balance is positive)
        # your code here
        self.balance += (self.balance * (1 + self.int_rate))

# Create 2 accounts
# account1 = BankAccount(.02, 5)
# account2 = BankAccount(.03, 10)

# To the first account, make 3 deposits and 1 withdrawal, then yield interest and display the account's info all in one line of code (i.e. chaining)
# account1.make_deposit(100)
# account1.make_deposit(500)
# account1.make_deposit(2)
# account1.make_withdrawal(50)
# account1.yield_interest()
# account1.display_account_info()

# To the second account, make 2 deposits and 4 withdrawals, then yield interest and display the account's info all in one line of code (i.e. chaining)
# account2.make_deposit(10000)
# account2.make_deposit(500)
# account2.make_withdrawal(50)
# account2.make_withdrawal(5)
# account2.make_withdrawal(5000)
# account2.make_withdrawal(150)
# account2.yield_interest()
# account2.display_account_info()

