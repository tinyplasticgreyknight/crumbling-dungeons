import random_source
import re

TEMPLATE_RANDOM = re.compile("\\[%s\\]" % random_source.DPATTERN_TEXT)
TEMPLATE_NAME = re.compile("\\[(.+)\\]")

def identity(x): return x

def snip(string, start, end=None):
    return string[start:end]

def extract_fragments(template, pattern, transform_text, transform_item):
    last = 0
    fragments = []
    for match in pattern.finditer(template):
        copylast = last
        start = match.start()
        end = match.end()
        fragments.append(transform_text(snip(template, copylast, start)))
        fragments.append(transform_item(match))
        last = end
    fragments.append(transform_text(snip(template, last)))
    return fragments

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
        self.room_width = self.compile_int_template(self.room_width, randoms)
        self.room_height = self.compile_int_template(self.room_height, randoms)
        self.room_exits = self.compile_int_template(self.room_exits, randoms)
        self.danger_rolls = self.compile_int_template(self.danger_rolls, randoms)
        self.wealth_rolls = self.compile_int_template(self.wealth_rolls, randoms)
        self.compile_list(self.danger, randoms)
        self.compile_list(self.wealth, randoms)
        self.compile_list(self.features, randoms)
        self.compile_list(self.connections, randoms, include_extra=False)

    def compile_list(self, items, randoms, include_extra=True):
        for i in range(len(items)):
            items[i] = self.compile_template(items[i], randoms, include_extra)

    def compile_names(self, fragment, acc_names, acc_tags):
        transform_text = lambda text: lambda: text
        def transform_item(match):
            name = match.group(1)
            if name == "":
                return lambda: ""
            elif name.startswith("#"):
                acc_tags.append(name[1:])
                return lambda: ""
            else:
                acc_names.append(name)
                return lambda: name
        subfragments = extract_fragments(fragment, TEMPLATE_NAME, transform_text, transform_item)
        return lambda: render_template(subfragments)

    def compile_int_template(self, template, randoms):
        transform_text = lambda text: lambda: text
        transform_item = lambda match: lambda: randoms.dagainstmatch(match)
        fragments = extract_fragments(template, TEMPLATE_RANDOM, transform_text, transform_item)
        return lambda: int(render_template(fragments))

    def compile_template(self, template, randoms, include_extra=True):
        acc_names = list()
        acc_tags = list()
        transform_text = lambda text: self.compile_names(text, acc_names, acc_tags)
        transform_item = lambda match: lambda: randoms.dagainstmatch(match)
        fragments = extract_fragments(template, TEMPLATE_RANDOM, transform_text, transform_item)
        stats = self.critter_stat_blocks(sorted(set(acc_names)))
        if include_extra:
            return lambda: (render_template(fragments), stats, acc_tags)
        else:
            return lambda: render_template(fragments)

    def critter_stat_blocks(self, critter_names):
        return [self.critter_stat_block(name) for name in critter_names]

    def critter_stat_block(self, name):
        self.creature_headers
        statline = ", ".join(map(lambda pair: "%s: %s" % pair, zip(self.creature_headers, self.creatures[name])))
        return "%s: %s" % (name, statline)

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
