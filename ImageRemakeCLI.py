import click
from pyfiglet import Figlet

import blur as blurProcess
import resize as resizeProcess
import rotate as rotateProcess
import sharper as sharperProcess
# import writeText as writeTextProcess

click.secho(Figlet(font='slant').renderText('ImageRemake v1.0'), fg='red', bold=True)

@click.command()
@click.option("-p", "--path", required=True, type=str, help="Defines path of target image.")
@click.option("-b", "--blur", type=int, default=0, help="Blurs an image for some level.")
@click.option("-R", "--resize", type=int, nargs=2, default=(0,0), help="Resizes image to some height and width.")
@click.option("-r", "--rotate", type=int, default=0, help="Rotates image for some number of degrees.")
@click.option("-s", "--sharpen", is_flag=True, help="Sharpen an image.")
@click.option("-w", "--writeText", required=False, type=str, help="Writes some text on the image.")
def run(path, blur, resize, rotate, sharpen, writetext):
    if blur != 0:
        blurProcess.process(path, blur)
    elif not (resize[0] == 0 or resize[1] == 0):
        resizeProcess.resize(path, resize[0], resize[1])
    elif rotate != 0:
        rotateProcess.rotate(path, rotate)
    elif sharpen:
        sharperProcess.sharpen(path)
    elif not writetext is None:
        # TODO: add writeText support
        click.echo("Write text is not working yet!")
    else:
        click.echo("No options were selected for the image %s" % path)

if __name__ == '__main__':
    run()
