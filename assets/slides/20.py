class A:
    x, y, z = 0, 1, 2

    def f(self):
        return [self.x, self.y, self.z]

class B(A):
    """Tests

    >>> A().f()
    [0, 1, 2]
    >>> B().f()
    [6, 1, 'A']
    """
    x = 6
    def __init__(self):
        self.z = 'A'


class Bear:
    """A Bear.
    
    
    >>> oski = Bear()
    >>> oski
    Bear()
    >>> print(oski)
    a bear
    >>> print(str(oski))
    a bear
    >>> print(repr(oski))
    Bear()
    >>> print(oski.__repr__())
    oski
    >>> print(oski.__str__())
    oski the bear
    """
    def __init__(self):
        self.__repr__ = lambda: 'oski' # instance attribute
        self.__str__ = lambda: 'oski the bear' # instance attribute

    def __repr__(self): # class attribute
        return 'Bear()'

    def __str__(self): # class attribute
        return 'a bear'

def print_bear():
    oski = Bear()
    print(repr(oski))
    print(oski.__repr__())

class Letter:
    def __init__(self, contents):

        self.contents = contents

        self.sent = False

    def send(self):

        if self.sent:

            print(self, 'was already sent.')

        else:
            print(self, 'has been sent.')

            self.sent = True

            return Letter(self.contents.upper())

    def __repr__(self):
        return self.contents


class Numbered(Letter):
   
    number = 0

    def __init__(self, contents):

        super().__init__(contents)
        
        self.number = Numbered.number

        Numbered.number += 1

    def __repr__(self):

        return '#' + str(self.number)



