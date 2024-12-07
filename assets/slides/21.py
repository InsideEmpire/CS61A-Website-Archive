class Link:
    """A linked list.

    >>> s = Link(3, Link(4, Link(5)))
    >>> s
    Link(3, Link(4, Link(5)))
    >>> print(s)
    <3 4 5>
    >>> s.first
    3
    >>> s.rest
    Link(4, Link(5))
    >>> s.rest.first
    4
    >>> s.rest.first = 7
    >>> s
    Link(3, Link(7, Link(5)))
    >>> s.first = 6
    >>> s.rest.rest = Link.empty
    >>> s
    Link(6, Link(7))
    >>> print(s)
    <6 7>
    >>> print(s.rest)
    <7>
    >>> t = Link(1, Link(Link(2, Link(3)), Link(4)))
    >>> t
    Link(1, Link(Link(2, Link(3)), Link(4)))
    >>> print(t)
    <1 <2 3> 4>
    """
    empty = ()

    def __init__(self, first, rest=empty):
        assert rest is Link.empty or isinstance(rest, Link)
        self.first = first
        self.rest = rest

    def __repr__(self):
        if self.rest:
            rest_repr = ', ' + repr(self.rest)
        else:
            rest_repr = ''
        return 'Link(' + repr(self.first) + rest_repr + ')'

    def __str__(self):
        string = '<'
        while self.rest is not Link.empty:
            string += str(self.first) + ' '
            self = self.rest
        return string + str(self.first) + '>'

def map_link(f, s):
    """Return a linked list of f(x) for each x in s.

    >>> evens = Link(4, Link(2, Link(6)))
    >>> map_link(lambda x: x + 1, evens)
    Link(5, Link(3, Link(7)))
    >>> evens
    Link(4, Link(2, Link(6)))
    """
    if s is Link.empty:
        return s
    return Link(f(s.first), map_link(f, s.rest))

def cycle(k, n):
    """Build an n-element list that cycles among range(k).

    >>> cycle(3, 10)
    [0, 1, 2, 0, 1, 2, 0, 1, 2, 0]
    """
    s = []
    for i in range(n):
        s.append(i % k)
    return s

def cycle_link(k, n):
    """Build an n-element linked list that cycles among range(k).

    >>> print(cycle_link(3, 10))
    <0 1 2 0 1 2 0 1 2 0>
    """
    first = Link.empty
    for i in range(n):
        new_link = Link(i % k)
        if first is Link.empty:
            first, last = new_link, new_link
        else:
            last.rest, last = new_link, new_link
    return first

def double(s, v):
    """Insert another v after each v in s.

    >>> s = [2, 7, 1, 8, 2, 8]
    >>> double(s, 8)
    >>> s
    [2, 7, 1, 8, 8, 2, 8, 8]
    """
    i = 0
    while i < len(s):
        if s[i] == v:
            s.insert(i+1, v)
            i += 2
        else:
            i += 1

def double_link(s, v):
    """Insert another v after each v in s.

    >>> s = Link(2, Link(7, Link(1, Link(8, Link(2, Link(8))))))
    >>> double_link(s, 8)
    >>> print(s)
    <2 7 1 8 8 2 8 8>
    """
    while s is not Link.empty:
        if s.first == v:
            s.rest = Link(v, s.rest)
            s = s.rest.rest
        else:
            s = s.rest
