from dungeon.factory import Factory

class Room:
    def __init__(self, n):
        self.n = n

class RoomFactory(Factory):
    def __init__(self, tables, randoms):
        Factory.__init__(self, tables, randoms)
        self.gensym = 0

    def create(self):
        self.gensym += 1
        return Room(self.gensym)
