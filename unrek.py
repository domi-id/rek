#!/usr/bin/env python3
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
                print(f"Cowardly refusing to overwrite {args.outfile}", file=sys.stderr)
                exit(1)

            reklib.decompress(open(args.infile, "rb"), open(args.outfile, "wb"))

        elif not sys.stdin.isatty():
            reklib.decompress(sys.stdin.buffer, sys.stdout.buffer)

        else:
            parser.print_help()

    except NotImplementedError:
        print("orka", file=sys.stderr)
        exit(1)
