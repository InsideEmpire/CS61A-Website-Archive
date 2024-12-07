# Twenty-one

def play(strategy0, strategy1, goal=21):
    """Play twenty-one and return the index of the winner.

    >>> play(two_strat, two_strat)
    1
    """
    n = 0
    who = 0  # Player 0 goes first
    while n < goal:
        if who == 0:
            n = n + strategy0(n)
            who = 1
        elif who == 1:
            n = n + strategy1(n)
            who = 0
    return who  # The player who didn't just add to n

def two_strat(n):
    return 2

def best_strat(n):
    return min(4 - n % 4, 3)

def interactive_strat(n):
    choice = 0
    while choice < 1 or choice > 3:
        print('How much will you add to', n, '(1-3)?', end=' ')
        choice = int(input())
    return choice

def noisy(who, s):
    """A strategy that prints its choices.

    >>> play(noisy(0, two_strat), noisy(1, two_strat))
    Player 0 added 2 to 0 to reach 2
    Player 1 added 2 to 2 to reach 4
    Player 0 added 2 to 4 to reach 6
    Player 1 added 2 to 6 to reach 8
    Player 0 added 2 to 8 to reach 10
    Player 1 added 2 to 10 to reach 12
    Player 0 added 2 to 12 to reach 14
    Player 1 added 2 to 14 to reach 16
    Player 0 added 2 to 16 to reach 18
    Player 1 added 2 to 18 to reach 20
    Player 0 added 2 to 20 to reach 22
    1
    """
    def strat(n):
        choice = s(n)
        print('Player', who, 'added', choice, 'to', n, 'to reach', choice + n)
        return choice
    return strat


# Nearest Prime

def is_prime(n):
    k = 2
    while k < n:
        if n % k == 0:
            return False
        k = k + 1
    return True

def nearest_prime(n):
    """Return the nearest prime number to n. In a tie, return the larger one.

    >>> nearest_prime(8)   
    7
    >>> nearest_prime(11)   
    11
    >>> nearest_prime(21)   
    23
    """
    k = 0
    while True:
        if is_prime(n + k):
            return n + k
        if k > 0:
            k = -k 
        else:
            k = -k + 1

# Curry

"""
>>> curry = lambda f: lambda x: lambda y: f(x, y)
>>> reverse = lambda g: lambda x, y: g(y, x)
>>> square = curry(reverse(pow))(2)
"""

def curry(f):
    def g(x):
        def h(y):
            return f(x, y)
        return h
    return g

def reverse(g):
    def h(x, y):
        return g(y, x)
    return h

square = curry(reverse(pow))(2)
