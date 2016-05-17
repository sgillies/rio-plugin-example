"""metasay: an example plugin for the Rasterio CLI"""

import logging
from random import choice

from cowpy import cow


__author__ = "Sean Gillies"
__version__ = '1.2.0'

# Get a logger object using the name of this module. Do not however
# configure this or Python's root logger: the `rio` program, of which
# this is a subcommand, makes the necessary configuration.
logger = logging.getLogger(__name__)


def moothedata(data, key=None):
    """Return an amusing picture containing an item from a dict.

    Parameters
    ----------
    data: mapping
        A mapping, such as a raster dataset's ``meta`` or ``profile``
        property.
    key:
        A key of the ``data`` mapping.
    """
    if not key:
        key = choice(list(data.keys()))
        logger.debug("Using randomly chosen key: %s", key)
    msg = cow.Moose().milk("{0}: {1}".format(key.capitalize(), data[key]))
    return msg
