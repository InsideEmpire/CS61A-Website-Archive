from tree import *

def list_demos():
    s = [3, 3, 7, 9]
    u = s
    s[1] = 5
    s.append(11)

    t = [x+3 for x in s]
    for i in range(len(s)):
        s[i] = s[i] + 3

    [s[-(i+1)] for i in range(len(s))]
    for i in range(len(s)):
        s[i] = s[-(i+1)]

def sums(n, m):
    """Return lists that sum to n containing positive numbers up to m that
    have no adjacent repeats, for n > 0 and m > 0.

    >>> sums(5, 1)
    []
    >>> sums(5, 2)
    [[2, 1, 2]]
    >>> sums(5, 3)
    [[1, 3, 1], [2, 1, 2], [2, 3], [3, 2]]
    >>> sums(5, 5)
    [[1, 3, 1], [1, 4], [2, 1, 2], [2, 3], [3, 2], [4, 1], [5]]
    >>> sums(6, 3)
    [[1, 2, 1, 2], [1, 2, 3], [1, 3, 2], [2, 1, 2, 1], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
    """
    result = []
    for k in range(1, min(m + 1, n)):
        for rest in sums(n-k, m):
            if rest[0] != k:
                result.append([k] + rest)
    if n <= m:
        result.append([n])
    return result

def sums_demo():
    result = [[1], [2], [3]]
    for k in range(1, 4):
        for s in result:
            if s[-1] != k:
                s.append(k)
                result.append(s)
    print(result)

def identity_demos():
    a = [10]
    b = a
    a == b
    a is b
    a.extend([20, 30])
    a == b
    a is b
    
    a = [10]
    b = [10]
    a == b
    a is not b
    a.append(20)
    a != b

    s = [3, 5, 7]
    t = [9, 11]
    s.append(t)
    s.extend(t)
    t[1] = 13
    print(s)

    s = [2, 7, [1, 8]]
    t = s[2]
    t.append([2])
    e = s + t
    t[2].append(8)
    print(e)

def tuple_demos():
    (3, 4, 5, 6)
    3, 4, 5, 6
    ()
    tuple()
    tuple([1, 2, 3])
    # tuple(2)
    (2,)
    (3, 4) + (5, 6)
    (3, 4, 5) * 2
    5 in (3, 4, 5)

    # {[1]: 2}
    {1: [2]}
    {(1, 2): 3}
    # {([1], 2): 3}
    {tuple([1, 2]): 3}



