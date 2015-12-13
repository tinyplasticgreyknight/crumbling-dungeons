import os
from result_sink.sink import Sink

class Directory(Sink):
    def __init__(self, dirname, graph_formatter, key_formatter):
        self.dirname = dirname
        self.dotfile = "%s/graph.dot" % (self.dirname)
        self.keyfile = "%s/key.md" % (self.dirname)
        Sink.__init__(self, graph_formatter, key_formatter)

    def create_dir(self):
        try:
            os.mkdir(self.dirname)
        except FileExistsError:
            pass

    def save(self, donjon):
        self.create_dir()
        with open(self.dotfile, "w") as h:
            self.write_graph(donjon, h)
        with open(self.keyfile, "w") as h:
            self.write_key(donjon, h)
