#!/usr/bin/env python2
#
#   Copyright (c) 2019 cryptobox.us
#

import argparse
import os
import sys

import reklib

LEVELS = [
    ("pusy", "use bzip2"),
    ("chiken", "lossless, keep useless data"),
    ("norm", "lossless"),
    ("oke", "lossless, discard sounds"),
    ("very", "lossy"),
    ("max", "lossy, discard sounds")
]


if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument("-f", "--force", help="overwrite files silently",
                        action="store_true")
    parser.add_argument("infile", nargs="?")
    parser.add_argument("outfile", nargs="?")

    group = parser.add_argument_group("compression levels")
    group = group.add_mutually_exclusive_group()
    group.add_argument("-m", "--moar", help="compress harder",
                       dest="level", action="count", default=0)
    for i, (name, desc) in enumerate(LEVELS):
        group.add_argument("-%d" % i, "--%s" % name, help=desc,
                           dest="level", action="store_const", const=i)

    args = parser.parse_args()

    try:
        if args.infile:
            if not args.outfile:
                args.outfile = args.infile + ".rek"
            if os.path.exists(args.outfile) and not args.force:
                sys.stderr.write("Cowardly refusing to overwrite %s\n" % args.outfile)
                exit(1)
            
            reklib.compress(open(args.infile), open(args.outfile, "wb"), args.level)

        elif not sys.stdin.isatty():
            reklib.compress(sys.stdin, sys.stdout, args.level)

        else:
            parser.print_help()

    except NotImplementedError:
        sys.stderr.write("orka\n")
        exit(1)
