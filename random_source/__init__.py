import random

class Seed:
    def __init__(self, n):
        self.seed = n
        self.stream = random.Random(n)

    def randint(self, a, b):
        return self.stream.randint(a, b)

    def randrange(self, start, stop=None, step=1):
        return self.stream.randrange(start, stop, step)

class WrittenSeed(Seed):
    def __init__(self, nstr):
        n = int(nstr, base=16)
        Seed.__init__(self, n)
