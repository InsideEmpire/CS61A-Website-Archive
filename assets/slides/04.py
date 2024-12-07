# DRY

def same_length(a, b):
    """Return whether positive integers a and b have the same number of digits.

    >>> same_length(50, 70)
    True
    >>> same_length(50, 100)
    False
    >>> same_length(1000, 100000)
    False
    """
    return digits(a) == digits(b)
    # a_digits = 0
    # while a > 0:
    #     a = a // 10
    #     a_digits = a_digits + 1
    # b_digits = 0
    # while b > 0:
    #     b = b // 10
    #     b_digits = b_digits + 1
    # return a_digits == b_digits

def digits(a):
    a_digits = 0
    while a > 0:
        a = a // 10
        a_digits = a_digits + 1
    return a_digits

# Higher-order function

def double(x):
    return 2 * x

def twice(f, x):
    """Apply f twice to x.

    >>> twice(double, 3)
    12
    """
    return f(f(x))

# Nim

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

# Local function definitions; returning functions

def make_adder(n):
    """Return a function that takes one argument K and returns K + N.

    >>> add_three = make_adder(3)
    >>> add_three(4)
    7
    """
    def adder(k):
        return k + n
    return adder

make_adder(2000)(24)

def noisy_strat(who, s):
    """A strategy that prints its choices.

    >>> play(noisy_strat(0, two_strat), noisy_strat(1, two_strat))
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

def interactive_strat(n):
    choice = 0
    while choice < 1 or choice > 3:
        print('How much will you add to', n, '(1-3)?', end=' ')
        choice = int(input())
    return choice
