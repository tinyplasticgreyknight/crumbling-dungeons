class DataSource:
    def __init__(self):
        self.danger = ["?" for i in range(20)]
        self.wealth = ["?" for i in range(20)]
        self.features = ["?" for i in range(20)]
        self.connections = ["?" for i in range(20)]
        self.creatures = {}
        self.creature_headers = []
        self.room_width = "d6"
        self.room_height = "d6"
        self.room_exits = "d6-2"
        self.danger_rolls = "d6-3"
        self.wealth_rolls = "d6-3"
        self.feature_chance = 50
        self.feature_chance_empty = 100
        self.module_name = "UNKNOWN"

    def get_danger(self, randoms):
        return self.danger[randoms.index()]

    def get_wealth(self, randoms):
        return self.wealth[randoms.index()]

    def get_feature(self, randoms):
        return self.features[randoms.index()]

    def get_connection(self, randoms):
        return self.connections[randoms.index()]
