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
        self.stats = []

class RoomFactory(Factory):
    def __init__(self, tables, randoms):
        Factory.__init__(self, tables, randoms)
        self.gensym = 0

    def _collect_list_items(self, creator, list_size, stats):
        pairs = [creator(self.randoms) for _ in range(list_size)]
        for pair in pairs:
            stats += pair[1]
        return [pair[0] for pair in pairs]

    def create(self):
        self.gensym += 1
        room = Room(self.gensym, self.tables.get_room_size())
        stats = list()
        room.danger = self._collect_list_items(self.tables.get_danger, self.tables.danger_rolls(), stats)
        room.wealth = self._collect_list_items(self.tables.get_wealth, self.tables.wealth_rolls(), stats)
        room.stats = stats
        return room
