import random

def CreateRandomData(size):
    A = []
    for i in range(size):
        A.append(random.randrange(0, size))

    return A
