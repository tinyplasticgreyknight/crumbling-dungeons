import csv
from table_source.datasource import DataSource

class File(DataSource):
    def __init__(self, filename):
        DataSource.__init__(self)
        self.filename = filename
        self.loadraw()
        self.interpret()

    def loadraw(self):
        raw = []
        with open(self.filename, "r") as h:
            for row in csv.reader(h):
                raw.append(row)
        self.raw = raw

    def interpret(self):
        self.module_name = self.raw[0][0]
        self.load_main_tables()
        self.load_creatures()

    def load_main_tables(self):
        assert(self.raw[1][0:5] == ["1d20", "Danger", "Wealth", "Features", "Connections"])
        for i in range(20):
            j = i + 2
            self.danger[i] = self.raw[j][1]
            self.wealth[i] = self.raw[j][2]
            self.features[i] = self.raw[j][3]
            self.connections[i] = self.raw[j][4]

    def load_creatures(self):
        assert(self.raw[32][0] == "Creature")
        self.creature_headers = [h for h in self.raw[32][1:] if h != ""]
        value_max = 1 + len(self.creature_headers)
        for j in range(33, len(self.raw)):
            name = self.raw[j][0]
            if name == "":
                continue
            values = self.raw[j][1:value_max]
            if name in self.creatures.keys():
                raise KeyError('"%s" already exists' % name)
            self.creatures[name] = values
