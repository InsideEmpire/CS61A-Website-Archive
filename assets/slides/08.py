# Self-Reference

def print_all(k):
    print(k)
    return print_all
    
print_all(1)(3)(5)

def print_sums(n):
    print(n)
    def next_sum(k):
        return print_sums(n+k)
    return next_sum

print_sums(1)(3)(5)

# Functions that call functions that reference each other

def add_next(n):
    print(n)
    return lambda f: subtract_next(n + f)

def subtract_next(n):
    print(n)
    return lambda f: add_next(n - f)

add_next(2500)(500)(1000)(24)

# Recursion

from ucb import trace

def fact(n):
    """Compute n factorial.

    >>> fact(5)
    120
    >>> fact(0)
    1
    """
    result = 1
    while n > 0:
        result = result * n
        n -= 1
    return result

fact(5)

def fact(n):
    """Compute n factorial.

    >>> fact(5)
    120
    >>> fact(0)
    1
    """
    if n == 0 or n == 1:
        return 1
    else:
        return fact(n-1) * n

fact(5)

# Boxes and Pyramids
# https://pythontutor.com/cp/composingprograms.html#code=def%20boxes_r%28k%29%3A%0A%20%20%20%20%22%22%22%20prints%20k%20boxes%20in%20a%20line.%0A%20%20%20%3E%3E%3E%20boxes%284%29%20%20%0A%20%20%20%5B%5D%5B%5D%5B%5D%5B%5D%0A%20%20%20%20%22%22%22%0A%20%20%20%20if%20k%20%3D%3D%200%3A%20%0A%20%20%20%20%20%20%20return%0A%20%20%20%20else%3A%0A%20%20%20%20%20%20%20%20print%28%22%5B%5D%22,%20end%3D%22%22%29%0A%20%20%20%20%20%20%20%20boxes_r%28k-1%29%0A%20%20%20%20return%20%0A%0Adef%20pyramid_r%28k%29%3A%0A%20%20%20%20%22%22%22%20recursively%20prints%20out%20a%20pyramid%20of%20k%20height.%0A%20%20%20%3E%3E%3E%20pyramid%284%29%20%0A%20%20%20%20%5B%5D%0A%20%20%20%20%5B%5D%5B%5D%0A%20%20%20%20%5B%5D%5B%5D%5B%5D%0A%20%20%20%20%5B%5D%5B%5D%5B%5D%5B%5D%0A%20%20%20%20%22%22%22%0A%20%20%20%20if%20k%3D%3D0%3A%0A%20%20%20%20%20%20%20%20return%0A%20%20%20%20else%3A%0A%20%20%20%20%20%20%20%20pyramid_r%28k-1%29%0A%20%20%20%20%20%20%20%20print%28%22%22%29%0A%20%20%20%20%20%20%20%20boxes_r%28k%29%0A%20%20%20%20return%0A%0Apyramid_r%284%29&cumulative=true&curInstr=0&mode=display&origin=composingprograms.js&py=3&rawInputLstJSON=%5B%5D

def boxes_iter(k):
    """ iteratively prints out k boxes.
   >>> boxes_iter(4)
    [][][][]
    """
    while k > 0:
        print("[]", end="")
        k -= 1 
    return

def boxes_r(k):
    """ recursively prints out k boxes.
   >>> boxes_r(4)  
   [][][][]
    """
    if k == 0: 
       return
    else:
        print("[]", end="")
        boxes_r(k-1)
    return 

def pyramid_iter(k):
    """ iteratively prints out a pyramid of k height.
    >>> pyramid(4) 
    []
    [][]
    [][][]
    [][][][]
    """
    i = 1;          # start with 1 box
    while k > i:    # until we get to k boxes
        print(" ") 
        boxes_r(i)  
        i += 1      # increment i 
    return

def pyramid_r(k):
    """ recursively prints a pyramid of k height.
    >>> pyramid(4) 
    []
    [][]
    [][][]
    [][][][]
    """
    if k == 0: 
       return
    else:
       pyramid_r(k-1) # make a smaller pyramid
       print("")
       boxes_r(k)   # then print out k boxes
    return 

pyramid_r(4)
print("")

# Upside Down Pyramids
# https://pythontutor.com/cp/composingprograms.html#code=def%20boxes_r%28k%29%3A%0A%20%20%20%20%22%22%22%20prints%20k%20boxes%20in%20a%20line.%0A%20%20%20%3E%3E%3E%20boxes%284%29%20%20%0A%20%20%20%5B%5D%5B%5D%5B%5D%5B%5D%0A%20%20%20%20%22%22%22%0A%20%20%20%20if%20k%20%3D%3D%200%3A%20%0A%20%20%20%20%20%20%20return%0A%20%20%20%20else%3A%0A%20%20%20%20%20%20%20%20print%28%22%5B%5D%22,%20end%3D%22%22%29%0A%20%20%20%20%20%20%20%20boxes_r%28k-1%29%0A%20%20%20%20return%20%0A%0Adef%20pyramid_r%28k%29%3A%0A%20%20%20%20%22%22%22%20prints%20out%20an%20upside%20down%20pyramid%20of%20k%20height.%0A%20%20%20%3E%3E%3E%20pyramid%284%29%20%0A%20%20%20%20%5B%5D%5B%5D%5B%5D%5B%5D%0A%20%20%20%20%5B%5D%5B%5D%5B%5D%0A%20%20%20%20%5B%5D%5B%5D%0A%20%20%20%20%5B%5D%0A%20%20%20%20%22%22%22%0A%20%20%20%20if%20k%3D%3D0%3A%0A%20%20%20%20%20%20%20%20return%0A%20%20%20%20else%3A%0A%20%20%20%20%20%20%20%20boxes_r%28k%29%0A%20%20%20%20%20%20%20%20print%28%22%20%22%29%20%23%20new%20line%0A%20%20%20%20%20%20%20%20pyramid_r%28k-1%29%0A%20%20%20%20return%0Apyramid_r%284%29&cumulative=true&curInstr=0&mode=display&origin=composingprograms.js&py=3&rawInputLstJSON=%5B%5D

def pyramid_iter(k):
    """ iteratively prints out an upside down pyramid of k height.
    >>> pyramid(4) 
    [][][][]
    [][][]
    [][]
    []
    """
    while k < 0:    # start with k boxes
        print(" ")  
        boxes_r(k)
        k -= 1      #decrement k
    return

def pyramid_r(k):
    """ recursively prints an upside down pyramid of k height.
   >>> pyramid(4) 
    [][][][]
    [][][]
    [][]
    []
    """
    if k == 0: 
       return
    else:
        boxes_r(k)      # print out k boxes
        print(" ")
        pyramid_r(k-1)    # print out a smaller pyramid
    return 
pyramid_r(5)


