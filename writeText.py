from PIL import Image, ImageFont, ImageDraw
import click
from pyfiglet import Figlet

@click.command()
@click.option("-p", "--path", type=str, help="Path to target image")
@click.option("-wt", "--writeText", type=str, default="Text", help="Writes some text to image")

def write(path, writeText):

    #todo

if __name__ == "__main__":
    f = Figlet(font='slant')
    click.secho(f.renderText('PythonCLI v1.0'), fg="red", bold=True)
    write()