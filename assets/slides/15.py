

# --- Discussion Question  --- #
def iterator_demo():
    a = [1, 2, 3]
    b = [a, 4]
    c = iter(a)
    d = c
    print(next(c))
    print(next(d))
    print(b)

# --- map demo --- #
def map_demo():
    def double(x):
        print(f"*** now doubling {x} !! ***")
        return x*2

    s = [1, 2, 3, 4]
    doubler = map(double, s)
    print(next(doubler))
    print(next(doubler))
    n = doubler
    print(next(n))

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
    
    # Get all pixels as a list of tuples (R, G, B)
    pixels = list(img.getdata())

    # Create coordinates using list comprehension
    coordinates = [(x, y) for y in range(height) for x in range(width)]
    
    # Use zip to pair coordinates with pixel values and iterate through them
    for coord, pixel in zip(coordinates, pixels):
        print(f"Pixel at {coord}: {pixel}")
    
    # Also display the image
    img.show()


# --- text file demo --- #
def text_file_demo(file_path):
    """example usage: text_file_demo('beemovie.txt')"""
    l = open(file_path).readlines() # returns all the lines in the file as a list
    print("* fifth line: " + l[5])

    i = open(file_path) # returns an iterator that will read each line as you call next(i)
    
    #print the first 3 lines
    print(" ** first 3 lines:  **")
    print(next(i))
    print(next(i))
    print(next(i))

    #create a "yeller"...
    def yell(s): 
        return s.upper()

    yeller = map(yell, l) # ...a map object that will read each line but also make it uppercase
    print("** using our map object 'yeller' ** ")
    print(next(yeller))
    print(next(yeller))
    print(next(yeller))


