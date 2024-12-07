from link import *

def count_if(f, s):
    if s is Link.empty:
        return 0
    else:
        if f(s.first):
            return 1 + count_if(f, s.rest)
        else:
            return count_if(f, s.rest)

def contained_in(s):
    def f(s, x):
        if s is Link.empty:
            return False
        else:
            return s.first == x or f(s.rest, x)
    return lambda x: f(s, x)

def overlap(s, t):
    """For s and t with no repeats, count the numbers that appear in both.

    >>> a = Link(3, Link(4, Link(6, Link(7, Link(9, Link(10))))))
    >>> b = Link(1, Link(3, Link(5, Link(7, Link(8, Link(12))))))
    >>> overlap(a, b)  # 3 and 7
    2
    """
    return count_if(contained_in(t), s)
