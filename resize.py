import click
from PIL import Image, ImageOps

def resize(path, width, height):
    try:
        org_img = Image.open(path)
        size = (width, height)
        rsz_img = ImageOps.fit(org_img, size, Image.ANTIALIAS)
        rsz_img.show()
        click.secho("All images processed!", fg="green", bold=True)
    except Exception as e:
        print(e)
