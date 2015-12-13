from dungeon.factory import Factory

class ConnectionFactory(Factory):
    def __init__(self, tables, randoms):
        Factory.__init__(self, tables, randoms)

    def create(self):
        raise NotImplementedError()
