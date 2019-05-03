import click
from PIL import Image, ImageOps
from pyfiglet import Figlet

f = Figlet(font='slant')
click.secho(f.renderText('PythonCLI v1.0'), fg="red", bold=True)

@click.command()
@click.option("-p", "--path", type=str, help="Sets path of destination image.")
@click.option("-width", type=int, help="Resizes image to some width and height")
@click.option("-height", type=int, help="resizes Image to some height and width")

def resize(path, width, height):
    try:
        org_img = Image.open(path)
        size = (width, height)
        rsz_img = ImageOps.fit(org_img, size, Image.ANTIALIAS)
        rsz_img.show()
        click.secho("All images processed!", fg="green", bold=True)
    except Exception as e:
       print(e)

if __name__ == "__main__":
    resize()