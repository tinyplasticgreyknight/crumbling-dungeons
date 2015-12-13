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
        self.features = []
        self.stats = []
        self.tags = []

class RoomFactory(Factory):
    def __init__(self, tables, randoms):
        Factory.__init__(self, tables, randoms)
        self.gensym = 0

    def _collect_list_items(self, creator, list_size, stats, tags):
        created_items = [creator(self.randoms) for _ in range(list_size)]
        for item in created_items:
            stats += item[1]
            tags += item[2]
        return [item[0] for item in created_items]

    def create(self):
        self.gensym += 1
        room = Room(self.gensym, self.tables.get_room_size())
        stats = list()
        tags = list()
        room.danger = self._collect_list_items(self.tables.get_danger, self.tables.danger_rolls(), stats, tags)
        room.wealth = self._collect_list_items(self.tables.get_wealth, self.tables.wealth_rolls(), stats, tags)
        feature_chance = self.tables.feature_chance
        if (len(room.danger) + len(room.wealth)) == 0:
            feature_chance = self.tables.feature_chance_empty
        if self.randoms.chance(feature_chance):
            room.features = self._collect_list_items(self.tables.get_feature, 1, stats, tags)
        room.stats = stats
        room.tags = tags
        return room
