import click
from PIL import Image, ImageFilter, ImageFont, ImageDraw

# List of commands
@click.command()
@click.option("-p", "--path", type=str, help="Sets path of destination image.")
@click.option("-b", "--blur", default=False, type=bool, help="Blurs an image.")
@click.option("-ra", "--radius", default=0, type=int, help="Sets blur radius for x.")
@click.option("-text", "--text", default="Text", type=str, help="Writes some text on image.")

def writeText(path, text):
    try:
        original = Image.open(path)
        withText = original.ImageDraw.Draw(original)
        font = ImageFont.truetype("sans-serif.ttff", 25)

        withText.text((0, 0), text, (255, 255, 255), font=font)
        withText.save("picture-with-text.jpg")
    except:
        print("An error ocurred somewhere :-(")

def process(path, blur, radius):
    try:
        # Load an image from the hard drive
        original = Image.open(path)

        # Blur the image
        blurred = original.filter(ImageFilter.GaussianBlur(radius))

        # save the new image
        blurred.save("blurred.png")
        print("Action completed!")

    except:
        print("Unable to load image")
