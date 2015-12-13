class Sink:
    def __init__(self, graph_formatter, key_formatter):
        self.graph_formatter = graph_formatter
        self.key_formatter = key_formatter

    def save(self, donjon):
        raise NotImplementedError
        
    def write_graph(self, donjon, writer):
        self.graph_formatter.format(donjon, writer)

    def write_key(self, donjon, writer):
        self.key_formatter.format(donjon, writer)
