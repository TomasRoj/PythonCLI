from PIL import Image, ImageFont, ImageDraw
import click
from pyfiglet import Figlet

@click.command()
@click.option("-p", "--path", type=str, help="Path to target image")
@click.option("-wt", "--writeText", type=str, default="Text", help="Writes some text to image")

def write(path, writeText):

    img = Image.open(path)
    img.filter(ImageFont.load("arial.pil"))

    img.text((10, 25), writeText, font=font)
    img.show()

    click.secho("Image processed succesfully!", fg="green", bold=True)

if __name__ == "__main__":
    f = Figlet(font='slant')
    print(f.renderText('PythonCLI v1.0'))
    write()