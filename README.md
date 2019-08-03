# ImageRemakeCLI
This PythonCLI makes easier to work with images. Blur, rotate, write text, and much more! No more learning hard programs like Photoshop!

## How to set up & run

1. Clone this repo.
2. Move to this directory.
3. Type: `pip install requirements.txt`. This installs the packages needed in order for the application to run.
3. Type: `python fileName.py -p "pathToImage" + options(read more info below)`

## Files

Use file ImageRemakeCLI.py with parsing arguments to it.

## Options

* `-b` - Blurs image. Specify with number of blurriness level (int)
* `-r` - Rotates an image. Specify with the number degrees to rotate (int)
* `-w` - Writes text to image. Specify with text (string) - *** not working yet ***
* `-s` - Makes image sharper (bool).
* `-R` - Resizes an image to a specified size (int, int). Include the height and width as two integer values following the flag. Example: `-R 800 640` will resize an image to 800x640.

## Contribution

Contributions are welcome! Start by forking this repo, making changes and creating a pull request! If you have any more question or just want to talk, contact me please on email rojtomas@email.cz.

## About

Created by @TomasRoj on 27. April on rainy Saturday on living room sofa.

Tomáš Roj, rojtomas@email.cz

[Alec Trievel](https://github.com/atrievel)
This and other my projects are available under MIT license. See LICENSE file for more info.
