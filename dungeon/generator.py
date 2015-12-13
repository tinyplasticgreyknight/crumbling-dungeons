class Generator:
    def __init__(self, tables, randoms, room_factory):
        self.tables = tables
        self.randoms = randoms
        self.room_factory = room_factory

    def generate(self, donjon):
        self.generate_layout(donjon)
        donjon.rooms = [self.room_factory.create() for i in range(donjon.num_rooms)]
        return donjon

    def generate_layout(self, donjon):
        raise NotImplementedError
