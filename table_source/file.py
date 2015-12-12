from table_source.datasource import DataSource

class File(DataSource):
    def __init__(self, filename):
        DataSource.__init__(self)
        self.filename = filename
        self.load()

    def load(self):
        pass
