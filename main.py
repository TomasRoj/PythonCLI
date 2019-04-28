import click
from PIL import Image, ImageFilter, ImageFont, ImageDraw
from pyfiglet import Figlet
import uuid
import os, sys

f = Figlet(font='slant')
print(f.renderText('PythonCLI v1.0'))

# List of commands
@click.command()
@click.option("-p", "--path", type=str, help="Sets path of destination image.")
@click.option("-b", "--blur", default=False, type=bool, help="Blurs an image.")
@click.option("-ra", "--radius", default=0, type=int, help="Sets blur radius for x.")

def process(path, blur, radius):

    dirs = os.listdir(path)

    try:
        for item in dirs:
            if os.path.isfile(path+item):
                # Load an image from the hard drive
                original = Image.open(path + item)

                # Blur the image
                blurred = original.filter(ImageFilter.GaussianBlur(radius))

                # save the new image
                blurred.save("kittens-output/random.jpg")
                print("Current image processed succesfully!")

        click.secho("All images processed!", fg="green", bold=True)

    except:
        print("Unable to load image")

process()