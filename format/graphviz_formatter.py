from format.formatter import Formatter

class GraphvizFormatter(Formatter):
    def format(self, donjon, writer):
        writer.write("graph G {\n")
        for room in donjon.rooms:
            self.write_room(room, writer)
        writer.write("\n")
        for key in donjon.connections:
            conn = donjon.connections[key]
            self.write_connection(key, conn, writer)
        writer.write("}\n")

    def write_room(self, room, writer):
        writer.write('\troom%d [label="%d", shape=rect];\n' % (room.n, room.n))

    def write_connection(self, key, conn, writer):
        writer.write('\troom%d -- room%d [len=2];\n' % (key[0]+1, key[1]+1))
