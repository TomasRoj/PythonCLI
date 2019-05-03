import click
from pyfiglet import Figlet
from PIL import Image, ImageFilter, ImageFont, ImageDraw, ImageEnhance 

@click.command()
@click.option("-p", "--path", type=str, help="Path to target image")
@click.option("-s", "--sharper", type=bool, default=False, help="Sharper an image for some level")

def sharper(path, sharper):
    try:
      img = Image.open(path)
      img.filter(ImageFilter.SHARPEN()).show()

      click.secho("Image processed sucesfully!", fg="green", bold=True)
    except Exception as e:
        print(e)

if __name__ == "__main__":
    f = Figlet(font='slant')
    click.secho(f.renderText('ImageRemake v1.0'), fg="red", bold=True)
    sharper()