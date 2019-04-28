import click
from PIL import Image, ImageFilter, ImageFont, ImageDraw
from pyfiglet import Figlet

f = Figlet(font='slant')
print(f.renderText('PythonCLI v1.0'))

# List of commands
@click.command()
@click.option("-p", "--path", type=str, help="Sets path of destination image.")
@click.option("-b", "--blur", default=0, type=int, help="Blurs an image for some level.")

def process(path, blur):
    try:
        # Load an image from the hard drive
        original = Image.open(path)

        # Blur the image
        blurred = original.filter(ImageFilter.GaussianBlur(blur)).show()

        click.secho("All images processed!", fg="green", bold=True)
    except:
        print("Unable to load image")

if __name__ == "__main__":
    process()