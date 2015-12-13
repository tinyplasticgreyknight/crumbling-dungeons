class DataSource:
    def __init__(self):
        self.danger = []
        self.wealth = []
        self.features = []
        self.module_name = "UNKNOWN"

    def get_danger(self, randoms):
        return self.danger[randoms.index()]

    def get_wealth(self, randoms):
        return self.wealth[randoms.index()]

    def get_feature(self, randoms):
        return self.features[randoms.index()]
