import click
from PIL import Image, ImageFilter, ImageFont, ImageDraw

def rotate(path, rotate):
    try:
      img = Image.open(path)
      img.rotate(rotate).show()

      click.secho("Image processed succesfully!", fg="green", bold=True)
    except Exception as e:
        print(e)
