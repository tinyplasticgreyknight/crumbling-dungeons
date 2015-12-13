import random_source
import re

TEMPLATE_RANDOM = re.compile("\\[%s\\]" % random_source.DPATTERN_TEXT)

def compile_template(template, randoms, post_transform=id):
    last = 0
    fragments = []
    for match in TEMPLATE_RANDOM.finditer(template):
        start = match.start()
        end = match.end()
        fragments.append(lambda: template[last:start])
        fragments.append(lambda: randoms.dagainstmatch(match))
        last = end
    fragments.append(lambda: template[last:])
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

    def get_danger(self, randoms):
        return self.danger[randoms.index()]

    def get_wealth(self, randoms):
        return self.wealth[randoms.index()]

    def get_feature(self, randoms):
        return self.features[randoms.index()]

    def get_connection(self, randoms):
        return self.connections[randoms.index()]

    def get_room_size(self):
        return (self.room_width(), self.room_height())
