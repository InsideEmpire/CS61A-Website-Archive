# Print and None

def f(x):
    return x + 1
    # return x + 2

def g(x):
    print(x + 1)
    # print(x + 2)

f(3) + 2
# g(3) + 2

def h(x):
    """
    >>> h(2)
    121
    121
    >>> f = print
    """
    y = f(x)
    print(y)
    return y


# Multiple environments

def f(x):
    return square(x + square(y + 1))
    
def square(z):
    y = z * z
    return y
    
x, y, z = 1, 2, 3
print(f(z))

# Nice numbers

def nice_end(n):
    """Round n ending in 98, 99, 01, or 02 to the nearest 100.

    >>> nice_end(2798)
    2800
    >>> nice_end(102)
    100
    >>> nice_end(998)
    1000
    """
    if n % 100 >= 98:
        return n // 100 * 100 + 100
    elif n % 100 <= 2:
        return n // 100 * 100
    else:
        return n

def nice(n):
    """Find the closest nice number to n.

    >>> nice(99)
    100
    >>> nice(2799)
    2800
    >>> nice(5016)
    5000
    >>> nice(9902)
    10000
    >>> nice(1200456)
    1200000
    >>> nice(98402001)
    100000000
    >>> nice(1100)
    1100
    >>> nice(750)
    750
    >>> nice(2859)
    2859
    >>> nice(45622895)
    45622895
    """
    rest = n
    k = 0
    while rest > 10:
        if nice_end(rest) % 100 == 0:
            n = nice_end(rest) * 10 ** k
        rest, k = rest // 10, k + 1
    return n

# Prime factorization

def prime_factors(n):
    """Print the prime factors of positive integer n
       in non-decreasing order.

    >>> prime_factors(8)
    2
    2
    2
    >>> prime_factors(9)
    3
    3
    >>> prime_factors(10)
    2
    5
    >>> prime_factors(11)
    11
    >>> prime_factors(12)
    2
    2
    3
    >>> prime_factors(858)
    2
    3
    11
    13
    """
    while n > 1:
        k = smallest_factor(n)
        print(k)
        n = n // k

def smallest_factor(n):
    """Return the smallest factor of n greater than 1."""
    k = 2
    while n % k != 0:
        k = k + 1
    return k
