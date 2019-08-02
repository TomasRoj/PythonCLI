import click
from PIL import Image, ImageFilter, ImageFont, ImageDraw

def process(path, blur):
    try:
        # Load an image from the hard drive
        original = Image.open(path)

        # Blur the image
        blurred = original.filter(ImageFilter.GaussianBlur(blur)).show()

        click.secho("All images processed!", fg="green", bold=True)
    except Exception as e:
        print(e)
