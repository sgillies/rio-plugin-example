import os.path
import logging

from click.testing import CliRunner

from metasay.scripts.cli import metasay


logging.basicConfig(level=logging.DEBUG)


def test_cli_random():
    """A random item is printed."""
    filename = os.path.join(os.path.dirname(__file__), 'data/float.tif')
    runner = CliRunner()
    result = runner.invoke(metasay, [filename])
    assert result.exit_code == 0
    assert "||----w |" in result.output


def test_cli_dtype():
    """The dtype item is printed."""
    filename = os.path.join(os.path.dirname(__file__), 'data/float.tif')
    runner = CliRunner()
    result = runner.invoke(metasay, [filename, '--item', 'dtype'])
    assert result.exit_code == 0
    assert "Dtype: float64" in result.output
