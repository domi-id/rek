#
#   Copyright (c) 2019 cryptobox.us
#

import lzma


def compress(infile, outfile, level=0):
    if level != 0:
        raise NotImplementedError()

    lzma_filters = ({"id": lzma.FILTER_LZMA2, "preset": lzma.PRESET_EXTREME | 9}, )
    outfile.write(lzma.compress(infile.read(),
                                format=lzma.FORMAT_RAW, check=lzma.CHECK_NONE,
                                filters=lzma_filters))


def decompress(infile, outfile):
    raise NotImplementedError()
