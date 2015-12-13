import random

class Seed:
    def __init__(self, n):
        self.seed = n
        self.stream = random.Random(n)

    def randint(self, a, b):
        return self.stream.randint(a, b)

    def randrange(self, start, stop=None, step=1):
        return self.stream.randrange(start, stop, step)

    def chance(self, percent_chance):
        return self.randint(0, 99) < percent_chance

    def d(self, n):
        return self.randint(1, n)

    def index(self, length=20):
        return self.d(length) - 1

class WrittenSeed(Seed):
    def __init__(self, nstr):
        n = int(nstr, base=16)
        Seed.__init__(self, n)
