from dungeon.factory import Factory

class Room:
    def __init__(self, n, size):
        self.n = n
        self.feature = None
        self.num_exits = 0
        self.width = size[0]
        self.height = size[1]
        self.danger = []
        self.wealth = []

class RoomFactory(Factory):
    def __init__(self, tables, randoms):
        Factory.__init__(self, tables, randoms)
        self.gensym = 0

    def create(self):
        self.gensym += 1
        return Room(self.gensym, self.tables.get_room_size())
