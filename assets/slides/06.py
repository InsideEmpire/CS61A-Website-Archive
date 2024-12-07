# Zero-args

y = lambda: 2*x
x = 3
y()
x = 4
y()

# Dice

from random import randint

def six_sided():
    return randint(1, 6)

def eight_sided():
    return randint(1, 8)

def repeats(n, dice):
    "Return how many times a dice roll is the same as the previous one in n rolls."
    count = 0
    previous = None
    while n:
        outcome = dice()
        print(outcome)
        if previous == outcome:
            count += 1
        previous = outcome
        n -= 1
    return count

# Loops

def reprint(n):
    def a(word):
        k = n
        while k:
            print(word)
            k -= 1
    return a


# Lambdas

(lambda f: lambda x: f(f(x)))(lambda y: y * y)(3)

def twice(f):
    # g = lambda x: f(f(x))
    def g(x):
        return f(f(x))
    return g

square = lambda y: y * y

def square(y):
    return y * y



snap = lambda chat: lambda: snap(chat)
snap, chat = print, snap(2020)
chat()


chat()


