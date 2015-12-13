from dungeon.factory import Factory

class Connection:
    def __init__(self, description):
        self.description = description

class ConnectionFactory(Factory):
    def __init__(self, tables, randoms):
        Factory.__init__(self, tables, randoms)

    def create(self):
        return Connection(self.tables.get_connection(self.randoms))
        raise NotImplementedError()
