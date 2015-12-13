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
        for i in range(20):
            j = i + 2
            self.danger[i] = self.raw[j][1]
            self.wealth[i] = self.raw[j][2]
            self.features[i] = self.raw[j][3]
            self.connections[i] = self.raw[j][4]
