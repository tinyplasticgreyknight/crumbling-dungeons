from dungeon.generator import Generator

class TreeGen(Generator):
    def __init__(self, tables, randoms, room_factory, crosslink_chance):
        Generator.__init__(self, tables, randoms, room_factory)
        self.crosslink_chance = crosslink_chance
        self.limit = 1000

    def generate_layout(self, donjon):
        index = 0
        depth = 0
        depth_marker = 0
        crosslink_chance = self.crosslink_chance
        while True:
            if index >= donjon.num_rooms:
                break
            if index == self.limit - 1:
                crosslink_chance = 100
            self.extrude_exits(donjon, index, depth, crosslink_chance)
            if index >= depth_marker:
                depth += 1
                depth_marker = donjon.num_rooms
            index += 1

    def extrude_exits(self, donjon, index, depth, crosslink_chance):
        self.randoms.d(10)
        self.randoms.d(10)
        num_exits = self.roll_for_exits(depth)
        for _ in range(num_exits):
            if self.randoms.chance(crosslink_chance):
                if self.crosslink(donjon, index):
                    continue
            donjon.extrude_room(index)

    def roll_for_exits(self, depth):
        return max(0, self.randoms.d(6) - depth)

    def crosslink(self, donjon, index):
        ATTEMPTS = 10
        limit = donjon.num_rooms - 1
        for _ in range(ATTEMPTS):
            target = self.randoms.randint(0, limit)
            if not donjon.are_connected(index, target):
                donjon.connect_rooms(index, target)
                return True
        return False
