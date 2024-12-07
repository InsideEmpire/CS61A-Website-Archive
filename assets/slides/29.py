from operator import add, mul, truediv
def reduce(f, s, initial):
    """Combine elements of s pairwise using f, starting with initial.

    >>> reduce(mul, [2, 4, 8], 1)
    64
    >>> reduce(pow, [1, 2, 3, 4], 2)
    16777216
    """
    for x in s:
        initial = f(initial, x)
    return initial

def divide_all(n, ds):
    """Divide n by every d in ds.

    >>> divide_all(1024, [2, 4, 8])
    16.0
    >>> divide_all(1024, [2, 4, 0, 8])
    inf
    """
    try:
        return reduce(truediv, ds, n)
    except ZeroDivisionError:
        return float('inf')

