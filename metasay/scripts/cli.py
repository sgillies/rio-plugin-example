# Moothedata command.

import sys

import click
import rasterio

from metasay import moothedata
from metasay import __version__ as metasay_version


@click.command(short_help="Cowsay some dataset metadata.")
@click.argument('inputfile', type=click.Path(resolve_path=True), required=True,
                metavar="INPUT")
@click.option('--item', default=None, help="Select a metadata item.")
@click.version_option(version=metasay_version, message='%(version)s')
@click.pass_context
def metasay(ctx, inputfile, item):
    """Moo some dataset metadata to stdout.

    Python module: rio-metasay
    (https://github.com/sgillies/rio-plugin-example).
    """
    with rasterio.open(inputfile) as src:
        meta = src.profile
    click.echo(moothedata(meta, key=item))
