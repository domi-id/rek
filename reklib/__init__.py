#
#   Copyright (c) 2019 cryptobox.us
#

import bz2


def compress(infile, outfile, level=0):
    if level != 0:
        raise NotImplementedError()
    outfile.write(bz2.compress(infile.read()))


def decompress(infile, outfile):
    raise NotImplementedError()
