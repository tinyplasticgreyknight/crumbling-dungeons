from dungeon.generator import Generator

class TreeGen(Generator):
    def __init__(self, tables, randoms, room_factory):
        Generator.__init__(self, tables, randoms, room_factory)

    def generate_layout(self, donjon):
        pass #todo
