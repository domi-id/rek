#!/usr/bin/env python2
#
#   Copyright (c) 2019 cryptobox.us
#

import argparse
import os
import sys

import reklib

if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument("-f", "--force", help="overwrite files silently",
                        action="store_true")
    parser.add_argument("infile", nargs="?")
    parser.add_argument("outfile", nargs="?")

    args = parser.parse_args()

    try:
        if args.infile:
            if not args.outfile:
                args.outfile = args.infile + ".rec"
            if os.path.exists(args.outfile) and not args.force:
                sys.stderr.write("Cowardly refusing to overwrite %s\n" % args.outfile)
                exit(1)

            reklib.decompress(open(args.infile), open(args.outfile, "wb"))

        elif not sys.stdin.isatty():
            reklib.decompress(sys.stdin, sys.stdout)

        else:
            parser.print_help()

    except NotImplementedError:
        sys.stderr.write("orka\n")
        exit(1)
