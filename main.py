import click

@click.command()
@click.argument('name')
def print_name(name):
    if not name.startswith('p'):
        click.echo(name)

if __name__ == '__main__':
    print_name()
# to run go on terminal and type python name_printer.py neil
