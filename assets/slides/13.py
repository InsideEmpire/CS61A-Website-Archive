# Data abstraction

def line(slope, intercept):
    # return lambda x: slope * x + intercept
    return [slope, intercept]

def slope(f):
    # return f(1) - f(0)
    return f[0]

def y_intercept(f):
    # return f(0)
    return f[1]

def parallel(f, g):
    """Whether lines f and g are parallel.

    >>> parallel(line(3, 5), line(3, 2))
    True
    >>> parallel(line(3, 5), line(2, 3))
    False
    """
    return slope(f) == slope(g)

# Trees

def tree(label, branches=[]):
    for branch in branches:
        assert is_tree(branch), 'branches must be trees'
    return [label] + list(branches)

def label(tree):
    return tree[0]

def branches(tree):
    return tree[1:]

def is_tree(tree):
    if type(tree) != list or len(tree) < 1:
        return False
    for branch in branches(tree):
        if not is_tree(branch):
            return False
    return True

def is_leaf(tree):
    return not branches(tree)

### +++ === ABSTRACTION BARRIER === +++ ###

t = tree(1, 
         [tree(9, [
             tree(2, [
                 tree(5, [
                     tree(6), 
                     tree(7)]), 
                 tree(8), 
                 tree(3)]), 
             tree(4)])])

# the number 4
label(branches(branches(t)[0])[1])

# Examples

def fib_tree(n):
    if n <= 1:
        return tree(n)
    else:
        left, right = fib_tree(n-2), fib_tree(n-1)
        return tree(label(left) + label(right), [left, right])

def print_tree(t, indent=0):
    """Print a representation of this tree in which each label is
    indented by two spaces times its depth from the root.

    >>> print_tree(tree(1))
    1
    >>> print_tree(tree(1, [tree(2)]))
    1
      2
    >>> print_tree(fib_tree(4))
    3
      1
        0
        1
      2
        1
        1
          0
          1
    """
    print('  ' * indent + str(label(t)))
    for b in branches(t):
        print_tree(b, indent + 1)

def count_paths(t, total):
    """Return the number of paths from the root to any node in t 
    for which the labels along the path sum to total.

    >>> t = tree(3, [tree(-1), tree(1, [tree(2, [tree(1)]), tree(3)]), tree(1, [tree(-1)])])
    >>> print_tree(t) 
    3
      -1
      1
        2
          1
        3
      1
        -1
    >>> count_paths(t, 3)
    2
    >>> count_paths(t, 4)
    2
    >>> count_paths(t, 5)
    0
    >>> count_paths(t, 6)
    1
    >>> count_paths(t, 7)
    2
    """
    if label(t) == total:
        found = 1
    else:
        found = 0
    return found + sum([count_paths(b, total - label(t)) for b in branches(t)])

def largest_label(t):
    """Return the largest label in tree t.

    >>> t = tree(3, [tree(-1), tree(2, [tree(4, [tree(1)]), tree(3)]), tree(1, [tree(-1)])])
    >>> print_tree(t) 
    3
      -1
      2
        4
          1
        3
      1
        -1
    >>> largest_label(t)
    4
    """
    if is_leaf(t):
        return label(t)
    else:
        return max([label(t)] + [largest_label(b) for b in branches(t)])

def above_root(t):
    """Print all the labels of t that are larger than the root label.

    >>> t = tree(3, [tree(-1), tree(2, [tree(4, [tree(1)]), tree(3)]), tree(1, [tree(-1)])])
    >>> print_tree(t) 
    3
      -1
      2
        4
          1
        3
      1
        -1
    >>> above_root(t)
    4
    >>> above_root(branches(t)[1])
    4
    3
    """
    def process(u):
        if label(u) > label(t):
            print(label(u))
        for b in branches(u):
            process(b)
    process(t)





