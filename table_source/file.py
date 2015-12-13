import csv
import re
from table_source.datasource import DataSource

DO_ASSERT_HEADERS = False
PERCENT_TRIM = re.compile("^(\\d+)(\\.\\d*)?%?$")

def percent(s):
    return int(PERCENT_TRIM.fullmatch(s).group(1))

def assert_headers(expected, actual):
    if (not DO_ASSERT_HEADERS) or (actual == expected):
        return
    raise AssertionError("expected %s but got %s" % (expected, actual))

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
        self.load_tunable_values()
        self.load_creatures()

    def load_main_tables(self):
        TABLE_START = 1
        assert_headers(["1d20", "Danger", "Wealth", "Features", "Connections"], self.raw[TABLE_START][0:5])
        for i in range(20):
            j = i + TABLE_START + 1
            self.danger[i] = self.raw[j][1]
            self.wealth[i] = self.raw[j][2]
            self.features[i] = self.raw[j][3]
            self.connections[i] = self.raw[j][4]

    def load_tunable_values(self):
        TUNABLE_START = 23
        TUNABLE_SIZE = 8
        rows = [self.raw[j] for j in range(TUNABLE_START, TUNABLE_START+TUNABLE_SIZE)]
        heads = [row[0] for row in rows]
        assert_headers(["Room width", "Room length", "Room exits", "Number of danger rolls", "Number of wealth rolls", "Chance of feature", "Chance of feature if otherwise empty", "Chance of crosslink"], heads)
        values = [row[1] for row in rows]
        self.room_width = values[0]
        self.room_height = values[1]
        self.room_exits = values[2]
        self.danger_rolls = values[3]
        self.wealth_rolls = values[4]
        self.feature_chance = percent(values[5])
        self.feature_chance_empty = percent(values[6])
        self.crosslink_chance = percent(values[7])

    def load_creatures(self):
        CREATURE_START = 32
        assert_headers(["Creature"], self.raw[CREATURE_START][0:1])
        self.creature_headers = [h for h in self.raw[CREATURE_START][1:] if h != ""]
        value_max = 1 + len(self.creature_headers)
        for j in range(CREATURE_START+1, len(self.raw)):
            name = self.raw[j][0]
            if name == "":
                continue
            values = self.raw[j][1:value_max]
            if name in self.creatures.keys():
                raise KeyError('"%s" already exists' % name)
            self.creatures[name] = values
