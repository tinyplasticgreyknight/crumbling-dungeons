import random_source
import re

TEMPLATE_RANDOM = re.compile("\\[%s\\]" % random_source.DPATTERN_TEXT)

def identity(x): return x

def snip(string, start, end):
    return lambda: string[start:end]

def compile_template(template, randoms, post_transform=identity):
    last = 0
    fragments = []
    for match in TEMPLATE_RANDOM.finditer(template):
        copylast = last
        start = match.start()
        end = match.end()
        fragments.append(snip(template, copylast, start))
        fragments.append(lambda: randoms.dagainstmatch(match))
        last = end
    fragments.append(snip(template, last, None))
    return lambda: post_transform(render_template(fragments))

def render_template(fragments):
    rfragments = [str(f()) for f in fragments]
    return "".join(rfragments)

class DataSource:
    def __init__(self):
        self.danger = ["?" for i in range(20)]
        self.wealth = ["?" for i in range(20)]
        self.features = ["?" for i in range(20)]
        self.connections = ["?" for i in range(20)]
        self.creatures = {}
        self.creature_headers = []
        self.room_width = "[d6x10]"
        self.room_height = "[d6x10]"
        self.room_exits = "[d6-2]"
        self.danger_rolls = "[d6-3]"
        self.wealth_rolls = "[d6-3]"
        self.feature_chance = 50
        self.feature_chance_empty = 100
        self.module_name = "UNKNOWN"

    def compile_templates(self, randoms):
        self.room_width = compile_template(self.room_width, randoms, post_transform=int)
        self.room_height = compile_template(self.room_height, randoms, post_transform=int)
        self.room_exits = compile_template(self.room_exits, randoms, post_transform=int)
        self.danger_rolls = compile_template(self.danger_rolls, randoms, post_transform=int)
        self.wealth_rolls = compile_template(self.wealth_rolls, randoms, post_transform=int)
        self.compile_list(self.danger, randoms)
        self.compile_list(self.wealth, randoms)
        self.compile_list(self.features, randoms)
        self.compile_list(self.connections, randoms)

    def compile_list(self, items, randoms):
        for i in range(len(items)):
            items[i] = compile_template(items[i], randoms)

    def get_danger(self, randoms):
        return self.danger[randoms.index()]()

    def get_wealth(self, randoms):
        return self.wealth[randoms.index()]()

    def get_feature(self, randoms):
        return self.features[randoms.index()]()

    def get_connection(self, randoms):
        return self.connections[randoms.index()]()

    def get_room_size(self):
        return (self.room_width(), self.room_height())
