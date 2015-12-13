class Factory:
    def __init__(self, tables, randoms):
        self.tables = tables
        self.randoms = randoms

    def create(self):
        raise NotImplementedError()
