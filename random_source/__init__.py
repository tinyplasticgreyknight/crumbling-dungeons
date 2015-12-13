import random
import re

DPATTERN_TEXT = "(\\d+)?d(\\d+)([+-]\\d+)?(x(\\d+))"
DPATTERN = re.compile(DPATTERN_TEXT)

def int_or(s, backup):
    if s is None:
        return backup
    else:
        return int(s)

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
        return dagainstmatch(matches)

    def dagainstmatch(self, matches):
        num = int_or(matches.group(1), 1)
        mod = int_or(matches.group(3), 0)
        multiplier = int_or(matches.group(5), 1)
        return self.d(int(matches.group(2)), num, mod, multiplier)

    def d(self, sides, num=1, mod=0, multiplier=1):
        rolled = 0
        mod = mod
        multiplier = multiplier
        for _ in range(num):
            rolled += self.randint(1, sides)
        return (rolled + mod) * multiplier

    def index(self, length=20):
        return self.d(length) - 1

class WrittenSeed(Seed):
    def __init__(self, nstr):
        n = int(nstr, base=16)
        Seed.__init__(self, n)
