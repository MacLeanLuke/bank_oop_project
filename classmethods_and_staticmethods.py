# Class methods are defined with a decorator @classmethod. They belong to the class itself instead of the instance. Instead of implicitly passing self into the method, we pass cls. This is reference to the class.

class BankAccount:


         # class attribute
        bank_name = "First National Dojo"
        all_accounts = []
         def __init__(self, int_rate, balance):
                self.int_rate = int_rate
                self.balance = balance
                BankAccount.all_accounts.append(self)
    
        # class method to change the name of the bank
        @classmethod
         def change_bank_name(cls, name):
                cls.bank_name = name
        # class method to get balance of all accounts
        @classmethod
        def all_balances(cls):
                sum = 0
                # we use cls to refer to the class
                for account in cls.all_accounts:
                        sum += account.balance
                return sum


# Static methods are functions defined within the class with a decorator @staticmethod.  They have no access on instance or class attributes so we do need to pass any arguments into them.

# If we wanted our BankAccount class to have a utility function to add or subtract we could implement @staticmethod on the class.

class BankAccount:
    # ... __init__ goes here
    def with_draw(self, amount):
        # we can use the static method here to evaluate
        # if we can with draw the funds without going negative
        if BankAccount.can_withdraw(self.balance, amount):
            self.balance -= amount
        else:
            print("Insufficient Funds")
            return self


    # static methods have no access to any attribute
    # only to wha   t is passed into it@st aticmethoddef can_withdraw(balance,amount):
    if (balance - amount) < 0:
        return False
    else:
        return True
