# Tree Recursion 

# ----------------------- #
# Tracing factorial

from ucb import trace

@trace
def fact(n):
    """ computes the factorial of n (n!)
    >>> fact(5) # 5! = 5 * 4 * 3 * 2 * 1
    120
    """
    if n == 0 or n == 1:
        return 1
    else:
        return n * fact(n-1)

# ----------------------- #
# Mutual Recursion
# (Counting Unique Prime Factors Recursively)
# https://pythontutor.com/render.html#code=def%20smallest_factor%28n%29%3A%0A%20%20%20%20if%20%28n%252%20%3D%3D%200%29%3A%0A%20%20%20%20%20%20%20%20return%202%0A%20%20%20%20k%20%3D%203%0A%20%20%20%20while%20%28k%20%3C%20n%29%3A%0A%20%20%20%20%20%20%20%20if%20%28n%25k%20%3D%3D%200%29%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20return%20k%0A%20%20%20%20%20%20%20%20k%20%2B%3D%201%0A%20%20%20%20return%20n%0A%0A%0Adef%20unique_prime_factors%28n%29%3A%0A%20%20%20%20%22%22%22Return%20the%20number%20of%20unique%20prime%20factors%20of%20n.%0A%0A%20%20%20%20%3E%3E%3E%20unique_prime_factors%2851%29%20%20%23%203%20*%2017%0A%20%20%20%202%0A%20%20%20%20%3E%3E%3E%20unique_prime_factors%2827%29%20%20%20%23%203%20*%203%20*%203%0A%20%20%20%201%0A%20%20%20%20%3E%3E%3E%20unique_prime_factors%28120%29%20%23%202%20*%202%20*%202%20*%203%20*%205%0A%20%20%20%203%0A%20%20%20%20%22%22%22%0A%20%20%20%20k%20%3D%20smallest_factor%28n%29%0A%20%20%20%20def%20no_k%28n%29%3A%0A%20%20%20%20%20%20%20%20%22Return%20the%20number%20of%20unique%20prime%20factors%20of%20n%20other%20than%20k.%22%0A%20%20%20%20%20%20%20%20if%20n%20%3D%3D%201%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20return%200%0A%20%20%20%20%20%20%20%20elif%20n%20%25%20k%20!%3D%200%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20return%20unique_prime_factors%28n%29%0A%20%20%20%20%20%20%20%20else%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20return%20no_k%28n//k%29%0A%20%20%20%20return%201%2Bno_k%28n%29%0A%0Aunique_prime_factors%2860%29&cumulative=false&curInstr=0&heapPrimitives=nevernest&mode=display&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false
def smallest_factor(n):
    if (n%2 == 0):
        return 2
    k = 3
    while (k < n):
        if (n%k == 0):
            return k
        k += 1
    return n


def unique_prime_factors(n):
    """Return the number of unique prime factors of n.

    >>> unique_prime_factors(51)  # 3 * 17
    2
    >>> unique_prime_factors(27)   # 3 * 3 * 3
    1
    >>> unique_prime_factors(120) # 2 * 2 * 2 * 3 * 5
    3
    """
    k = smallest_factor(n)
    def no_k(n):
        "Return the number of unique prime factors of n other than k."
        if n == 1:
            return 0
        elif n % k != 0:
            return unique_prime_factors(n)
        else:
            return no_k(n//k)
    return 1+no_k(n)

unique_prime_factors(120)

# ----------------------- #
# Count Partitions
# https://pythontutor.com/cp/composingprograms.html#code=def%20count_partitions%28n,%20m%29%3A%0A%20%20%20%20if%20n%20%3D%3D%200%3A%0A%20%20%20%20%20%20%20%20return%201%0A%20%20%20%20elif%20n%20%3C%200%3A%0A%20%20%20%20%20%20%20%20return%200%0A%20%20%20%20elif%20m%20%3D%3D%200%3A%0A%20%20%20%20%20%20%20%20return%200%0A%20%20%20%20else%3A%0A%20%20%20%20%20%20%20%20with_m%20%3D%20count_partitions%28n-m,%20m%29%20%0A%20%20%20%20%20%20%20%20without_m%20%3D%20count_partitions%28n,%20m-1%29%0A%20%20%20%20%20%20%20%20return%20with_m%20%2B%20without_m%0A%20%20%20%20%20%20%20%20%0Aresult%20%3D%20count_partitions%285,%203%29%0A%0A%23%201%20%2B%201%20%2B%201%20%2B%201%20%2B%201%20%3D%205%0A%23%201%20%2B%201%20%2B%201%20%2B%202%20%2B%20%20%20%3D%205%0A%23%201%20%2B%202%20%2B%202%20%2B%20%20%20%20%20%20%20%3D%205%0A%23%201%20%2B%201%20%2B%203%20%2B%20%20%20%20%20%20%20%3D%205%0A%23%202%20%2B%203%20%2B%20%20%20%20%20%20%20%20%20%20%20%3D%205&cumulative=false&curInstr=0&mode=display&origin=composingprograms.js&py=3&rawInputLstJSON=%5B%5D

def count_partitions(n, m):
    if n == 0:
        return 1
    elif n < 0:
        return 0
    elif m == 0:
        return 0
    else:
        with_m = count_partitions(n-m, m) 
        without_m = count_partitions(n, m-1)
        return with_m + without_m
        
result = count_partitions(5, 3)

# 1 + 1 + 1 + 1 + 1 = 5
# 1 + 1 + 1 + 2 +   = 5
# 1 + 2 + 2 +       = 5
# 1 + 1 + 3 +       = 5
# 2 + 3 +           = 5

# ----------------------- #

def count_park(n):
    """Count the ways to park cars and motorcycles in n adjacent spots.
    >>> count_park(1)  # '.' or '%'
    2
    >>> count_park(2)  # '..', '.%', '%.', '%%', or '<>'
    5
    >>> count_park(4)  # some examples: '<><>', '.%%.', '%<>%', '%.<>'
    29
    """
    if n < 0:
        return 0
    elif n == 0:
        return 1
    else:
        return count_park(n-2) + count_park(n-1) + count_park(n-1)

