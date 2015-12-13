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
        room = Room(self.gensym, self.tables.get_room_size())
        room.danger += [self.tables.get_danger(self.randoms) for _ in range(self.tables.danger_rolls())]
        room.wealth += [self.tables.get_wealth(self.randoms) for _ in range(self.tables.wealth_rolls())]
        return room
