import click

@click.command()
@click.option("-w", "--write", type=str, default="Hello from PythonCLI!", help="Writes some text on command line")
@click.option("-openFile", "--openFile", type=str, help="opens file from path")

def writeText(write):
    print(write)

def OpenFile(openFile, path):
    file = open(path)
    file.write("opened")
