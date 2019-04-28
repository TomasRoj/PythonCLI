import click
from pyfiglet import Figlet
from PIL import Image, ImageFilter, ImageFont, ImageDraw

from pyfiglet import Figlet

@click.command()
@click.option("-r", "--rotate", type=int, default=0, help="Rotates image for some number of degrees.")
@click.option("-p", "--path", type=str, help="Defines path of target image.")

def rotate(path, rotate):
    img = Image.open(path)
    img.rotate(90).show()

    click.secho("Image processed succesfully!", fg="green", bold=True)

if __name__ == "__main__":
    f = Figlet(font='slant')
    print(f.renderText('PythonCLI v1.0'))
    rotate()