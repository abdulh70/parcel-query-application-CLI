import click
from utils.helpers import add_landowner, add_property, add_plot, list_landowners
from database.db import init_db

@click.group()
def cli():
    """Land Query CLI Application."""
    pass

@cli.command()
def init():
    """Initialize the database."""
    init_db()

@cli.command()
@click.argument('name')
def add_landowner_cmd(name):
    """Add a new landowner."""
    add_landowner(name)

@cli.command()
@click.argument('name')
@click.argument('landowner_id', type=int)
def add_property_cmd(name, landowner_id):
    """Add a new property to a landowner."""
    add_property(name, landowner_id)

@cli.command()
@click.argument('name')
@click.argument('property_id', type=int)
def add_plot_cmd(name, property_id):
    """Add a new plot to a property."""
    add_plot(name, property_id)

@cli.command()
def list_landowners_cmd():
    """List all landowners."""
    landowners = list_landowners()
    for landowner in landowners:
        print(landowner)

if __name__ == '__main__':
    cli()
