import random

def shuffle_list(items):
    shuffled = items[:]
    random.shuffle(shuffled)
    return shuffled
