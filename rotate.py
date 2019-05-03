import click
from pyfiglet import Figlet
from PIL import Image, ImageFilter, ImageFont, ImageDraw

from pyfiglet import Figlet
f = Figlet(font='slant')
click.secho(f.renderText('PythonCLI v1.0'), fg="red", bold=True)

@click.command()
@click.option("-r", "--rotate", type=int, default=0, help="Rotates image for some number of degrees.")
@click.option("-p", "--path", type=str, help="Defines path of target image.")

def rotate(path, rotate):
    try:
      img = Image.open(path)
      img.rotate(rotate).show()

      click.secho("Image processed succesfully!", fg="green", bold=True)
    except Exception as e:
        print(e)

if __name__ == "__main__":
    rotate()