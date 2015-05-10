# Moothedata command.

import sys

import click
import rasterio
from rasterio.rio.cli import cli

from metasay import moothedata


@cli.command(short_help="Cowsay some dataset metadata.")
@click.argument(
    'inputfile',
    type=click.Path(resolve_path=True),
    required=True,
    metavar="INPUT")
@click.option('--item', default=None, help="Select a metadata item.")
@click.pass_context
def metasay(ctx, inputfile, item):
    """Moo some dataset metadata to stdout."""

    verbosity = (ctx.obj and ctx.obj.get('verbosity')) or 1

    with rasterio.drivers(CPL_DEBUG=verbosity > 2):
        with rasterio.open(inputfile) as src:
            meta = src.meta

    click.echo(moothedata(meta, key=item))

    sys.exit(0)
