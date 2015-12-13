import random
import re

DPATTERN = re.compile("^(\\d+)?d(\\d+)([+-]\\d+)?(x(\\d+))$")

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

    def dparse(self, dstr):
        matches = DPATTERN.fullmatch(dstr)
        return self.d(int(matches.group(2)), int(matches.group(1)), int(matches.group(3)), int(matches.group(5)))

    def d(self, sides, num=1, mod=0, multiplier=1):
        rolled = 0
        for _ in range(num):
            rolled += self.randint(1, sides)
        return (rolled + mod) * multiplier

    def index(self, length=20):
        return self.d(length) - 1

class WrittenSeed(Seed):
    def __init__(self, nstr):
        n = int(nstr, base=16)
        Seed.__init__(self, n)
