import click
from .logo import showLogo


@click.command('test', help="Test Video Camera")
def test(total_cam):
    showLogo()
    print(total_cam)
