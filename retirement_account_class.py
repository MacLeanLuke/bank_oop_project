from bank_account_class import BankAccount

# with just the inclusion of the parent class in parentheses, both the CheckingAccount and RetirementAccount classes both have all the attributes and functionality of the parent class
class RetirementAccount(BankAccount):
    def __init__(self, int_rate, is_roth, balance=0):
        
        # To indicate we are trying to use the parent's methods, we call on it with the keyword super.
        super().__init__(int_rate, balance)	

        # The only line we need to add is to set the is_roth attribute, since this is unique to the RetirementAccount class.
        self.is_roth = is_roth	

    def withdraw(self, amount, is_early):
        if is_early:
            amount = amount * 1.10
        return super().withdraw(amount)
