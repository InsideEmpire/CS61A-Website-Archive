class Account:
    """An account has a balance and a holder.

    >>> a = Account('John')
    >>> a.holder
    'John'
    >>> a.deposit(100)
    100
    >>> a.withdraw(90)
    10
    >>> a.withdraw(90)
    'Insufficient funds'
    >>> a.balance
    10
    """
    def __init__(self, account_holder):
        self.holder = account_holder
        self.balance = 0

    def deposit(self, amount):
        """Add amount to balance."""
        self.balance = self.balance + amount
        return self.balance

    def withdraw(self, amount):
        """Subtract amount from balance if funds are available."""
        if amount > self.balance:
            return 'Insufficient funds'
        self.balance = self.balance - amount
        return self.balance

def transfer(out_of, into, amount):
    """Transfer amount between two accounts.

    >>> john = Account('John')
    >>> jack = Account('Jack')
    >>> john.deposit(100)
    100
    >>> jack.deposit(100000)
    100000
    >>> transfer(jack, john, 1000)
    'Transfer successful'
    >>> john.balance
    1100
    >>> jack.balance
    99000
    >>> transfer(john, jack, 10000)
    'Insufficient funds'
    >>> transfer(john, jack, 10)
    'Transfer successful'
    >>> john.balance
    1090
    >>> jack.balance
    99010
    """
    result = out_of.withdraw(amount)
    if type(result) == str:  # something went wrong
        return result
    else:
        into.deposit(amount)
        return 'Transfer successful'

class Scam:
    """A scam account has a balance and a holder.

    >>> a = Scam('John')
    >>> a.holder
    'John'
    >>> a.deposit(100)
    102.0
    >>> a.withdraw(90)
    'We apologize for the delay'
    >>> a.withdraw(90)
    'We apologize for the delay'
    >>> a.balance
    102.0
    """
    def __init__(self, account_holder):
        self.holder = account_holder
        self.balance = 0

    def deposit(self, amount):
        """Add amount +2% to balance."""
        self.balance = self.balance + amount * 1.02
        return self.balance

    def withdraw(self, amount):
        """Subtract amount from balance if funds are available."""
        return 'We apologize for the delay'
