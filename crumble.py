#!/usr/bin/env python3

import table_source
import random_source
import dungeon
import format
import result_sink
import sys

def main(tablefile, seedstr):
    tables = table_source.File(tablefile)
    randoms = random_source.WrittenSeed(seedstr)

    outdir = "%s-%08x" % (tables.module_name, randoms.seed)
    results = result_sink.Directory(outdir, format.GraphvizFormatter(), format.MarkdownKeyFormatter())

    room_factory = dungeon.RoomFactory(tables, randoms)
    connection_factory = dungeon.ConnectionFactory(tables, randoms)
    generator = dungeon.TreeGen(tables, randoms, room_factory)

    donjon = dungeon.Instance(connection_factory)

    results.save(generator.generate(donjon))

    print("saved: %s" % outdir)


main(sys.argv[1], sys.argv[2])
