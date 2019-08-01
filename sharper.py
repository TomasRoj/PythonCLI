import click
from pyfiglet import Figlet
from PIL import Image, ImageFilter, ImageFont, ImageDraw, ImageEnhance 

def sharpen(path):
    try:
      img = Image.open(path)
      img.filter(ImageFilter.SHARPEN()).show()

      click.secho("Image processed sucesfully!", fg="green", bold=True)
    except Exception as e:
        print(e)
