class Instance:
    def __init__(self, connection_factory):
        self.num_rooms = 1
        self.rooms = []
        self.connections = dict()
        self.connection_factory = connection_factory

    def extrude_room(self, from_index):
        new_index = self.num_rooms
        self.num_rooms += 1
        self.rooms.append(None)
        self.connect_rooms(from_index, new_index)

    def connect_rooms(self, index_a, index_b):
        connection = self.connection_factory.create()
        key1 = (index_a, index_b)
        key2 = (index_b, index_a)
        if self.are_connected(index_a, index_b):
            raise KeyError("already connected")
        self.connections[key1] = connection

    def are_connected(self, index_a, index_b):
        if index_a == index_b: return True
        key1 = (index_a, index_b)
        key2 = (index_b, index_a)
        return (key1 in self.connections.keys()) or (key2 in self.connections.keys())

    def assign_room(self, index, room):
        if index < 0 or index >= self.num_rooms:
            raise IndexError("bad room index")
        if self.rooms[index] is not None:
            raise IndexError("already assigned")
        self.rooms[index] = room

    def verify(self):
        assert(len(self.rooms) == self.num_rooms)
        for room in self.rooms:
            assert(room is not None)
