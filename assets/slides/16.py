def add_to_each(p, edit):
    """
    Given a list, p, of 3-element tuples: [(x1, y1, z1), (x2, y2, z2), ...]
    And an "editor" tuple (also 3 elements) edit = (a, b, c)
    return a map object where
    a is added to each x-value, 
    b to each y-value, 
    and c to each z-value in the list of tuples.

    >>> list(add_to_each([(0, 0, 0), (1, 1, 1)], (10, 10, 10)))
    [(10, 10, 10), (11, 11, 11)]

    >>> list(add_to_each([(1, 2, 3), (1, 1, 1)], (10, 20, 30)))
    [(11, 22, 33), (11, 21, 31)]
    """
    return map(lambda x: (x[0] + edit[0], x[1] + edit[1], x[2] + edit[2]), p)


# --- image data demo --- #
def display_image_data(image_path):
    """
    displays an image and prints out the pixel data
    example usage: display_image_data("sonic.gif")
    """

    from PIL import Image # library for helping work with images, just for the fun little image demo
    # you'll have to install this by running 'pip install pillow' in your terminal first.

    # Load image and make sure it is in RGB format
    img = Image.open(image_path).convert("RGB")
    
    # Get the image dimensions
    width, height = img.size
    
    # Get all pixels as a list of tuples with 3 numbers (R, G, B)
    pixels = list(img.getdata())

    # Create coordinates using list comprehension
    coordinates = [(x, y) for y in range(height) for x in range(width)]

    # display the image
    img.show()

    # Make the red values "redder" by adding 100 to the 0th element of each R,G,B tuple
    redder_pixels = list(add_to_each(pixels, (100,0,0)))  # Increase red by 100
    
    # Update the image with the new redder pixel data
    img.putdata(redder_pixels)
    
    # Display the modified image
    img.show()


# --- intro to generators --- #

def generator_demo():
    def cycle(s):
        while True:
            for x in s:
                print("before yielding!")
                yield x
                print("after yielding!")


    l = [1,2,3]
    g = cycle(l)
    next(g)
    next(g)
    next(g)
    next(g)

    #all_of_them = list(g) # will run forever, trying to build an infinite list: [1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4...]


# -- revisiting the parking problem --- #
def park(n):
    """Return a list of the ways to park cars and motorcycles in n adjacent spots.

    >>> park(1)
    ['%', '.']
    >>> park(2)
    ['%%', '%.', '.%', '..', '<>']
    >>> park(3)
    ['%%%', '%%.', '%.%', '%..', '%<>', '.%%', '.%.', '..%', '...', '.<>', '<>%', '<>.']
    >>> len(park(4))
    29
    """
    if n < 0:
        return []
    elif n == 0:
        return ['']
    else:
        return (['%'  + s for s in park(n-1)] +
                ['.'  + s for s in park(n-1)] +
                ['<>' + s for s in park(n-2)])



def park(n):
    """Return a generator that yields all the ways to park cars and motorcycles in n adjacent spots.

    >>> sorted(park(1))
    ['%', '.']
    >>> sorted(park(2))
    ['%%', '%.', '.%', '..', '<>']
    >>> sorted(park(3))
    ['%%%', '%%.', '%.%', '%..', '%<>', '.%%', '.%.', '..%', '...', '.<>', '<>%', '<>.']
    >>> len(list(park(4)))
    29
    """
    if n == 0:
        yield ''
    elif n > 0:
        for s in park(n-1):
            yield '%'  + s
            yield '.'  + s
        for s in park(n-2):
            yield '<>' + s


# -- fibonacci sequence generator -- #
def fib_generator():
    """
    A generator that yields the Fibonacci sequence indefinitely.
    (The Fibonacci sequence starts with 0 and 1, and each subsequent number
    is the sum of the previous two.)

    >>> fib = fib_generator()
    >>> next(fib)
    0
    >>> next(fib)
    1
    >>> next(fib)
    1
    >>> next(fib)
    2
    >>> list(next(fib) for i in range(0,10)) # list the next 10 fibonacci numbers
    [3, 5, 8, 13, 21, 34, 55, 89, 144, 233]
    """
    a, b = 0, 1  # Starting values for the Fibonacci sequence
    while True:
        yield a  # Yield the current Fibonacci number
        a, b = b, a + b  # Update to the next Fibonacci numbers


