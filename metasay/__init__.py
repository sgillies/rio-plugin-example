# rio_say

from random import choice

from cowpy import cow


def moothedata(metadata, key=None):
    keys = list(metadata.keys())
    # Blacklist metadata items that cows can't pronounce.
    blacklist = ['transform', 'affine']
    for k in blacklist:
        if k in keys:
            keys.remove(k)
    key = key or choice(keys)
    msg = cow.Moose().milk("%s: %s" % (key.capitalize(), metadata[key]))
    return msg
