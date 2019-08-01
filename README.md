# ImageRemakeCLI
This PythonCLI makes easier to work with images. Blur, rotate, write text, and much more! No more learning hard programs like Photoshop!

## How to set up & run

1. Clone this repo.
2. Move to this directory.
3. Type: `pip install requirements.txt`. This installs the packages needed in order for the application to run.
3. Type: `python fileName.py -p "pathToImage" + options(read more info below)`

## Files

This project is contained in multiple .py files which use
different Image methods. Here is the list of currently available and tested files:

1. `rotate.py` - Rotates an image.
2. `blur.py` - Blurs an image.
3. `sharper.py` - Makes image little bit sharper.
4. `resize.py` - Resizes image to some height and width.

There are more files, (ex. writeText.py) but these are not working yet (that can be good contribution! 🎉)

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
This and other my projects are available under MIT license. See LICENSE file for more info.

### Contributors

* [Alec Trievel](https://github.com/atrievel)
