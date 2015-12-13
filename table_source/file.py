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
