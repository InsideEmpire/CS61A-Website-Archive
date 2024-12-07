import random

def sample():
    """
    >>> ws = ['the', 'of', 'when']
    >>> ps = [0.8, 0.15, 0.05]
    >>> random.choices(ws, ps)
    ['the']
    >>> random.choices(ws, ps, k=10)
    ['the', 'the', 'the', 'the', 'the', 'the', 'the', 'the', 'when', 'the']
    """

from collections import Counter
def bigram():

