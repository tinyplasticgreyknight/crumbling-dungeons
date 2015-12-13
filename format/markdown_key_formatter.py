from format.formatter import Formatter

class MarkdownKeyFormatter(Formatter):
    def format(self, donjon, writer):
        for room in donjon.rooms:
            self.write_room(room, writer)

    def write_room(self, room, writer):
        writer.write("## Room %s\n" % room.n)
