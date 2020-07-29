import click
from .test import test
from .rec import rec


@click.group()
def app():
    pass


# app.add_command(test)
app.add_command(rec)
