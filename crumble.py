#!/usr/bin/env python3

import table_source
import random_source
import dungeon
import result_sink
import sys

def main(tablefile, seedstr):
    tables = table_source.File(tablefile)
    randoms = random_source.WrittenSeed(seedstr)

    outdir = "%s-%08x" % (tables.module_name, randoms.seed)
    results = result_sink.Directory(outdir)

    results.save(dungeon.generate(tables, randoms))

    print("saved: %s" % outdir)


main(sys.argv[1], sys.argv[2])
