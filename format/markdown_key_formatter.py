from format.formatter import Formatter

class MarkdownKeyFormatter(Formatter):
    def format(self, donjon, writer):
        for i in range(len(donjon.rooms)):
            room = donjon.rooms[i]
            conns = self.render_connections(donjon, i)
            if i == 0:
                conns.insert(0, "To outside.")
            self.write_room(room, conns, writer)
            writer.write("\n")

    def write_room(self, room, conns, writer):
        writer.write("## Room %s (%dx%dft)\n" % (room.n, room.width, room.height))
        self.write_list("Dangers", room.danger, writer)
        self.write_list("Loot", room.wealth, writer)
        self.write_list("Features", room.features, writer)
        self.write_list("Exits", conns, writer)
        self.write_list("Stat Blocks", room.stats, writer)

    def write_list(self, header, items, writer):
        if len(items) == 0:
            return
        writer.write("### %s\n" % header)
        for item in items:
            writer.write("* %s\n" % item)

    def render_connection(self, donjon, room_index, key):
        dest = 0
        if key[0] == room_index:
            dest = key[1] + 1
        elif key[1] == room_index:
            dest = key[0] + 1
        else:
            return None
        conn = donjon.connections[key]
        return "To room %d.  %s" % (dest, conn.description)

    def render_connections(self, donjon, room_index):
        pre_result = [self.render_connection(donjon, room_index, k) for k in donjon.connections.keys()]
        return [text for text in pre_result if text is not None]
