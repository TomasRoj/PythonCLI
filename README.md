# ImageRemakeCLI
This PythonCLI makes easir work with images. Blur, rotate, put text and many more! No more learning hard programs like Photoshop!

## How to set up & run

1. Clone this repo.
2. Move to this directory.
3. Type: python fileName.py -p "pathToImage" + options(read more info below)
3. Type: `pip install requirements.txt`. This installs the packages needed in order for the application to run.
3. Type: `python fileName.py -p "pathToImage" + options(read more info below)`

## Files

This project is in multiple .py files which contains
different Image methods. Here is the list of currently availibe and tested files:

1. rotate.py - Rotates an image.
2. blur.py - Blurs an image.
3. sharper.py - Makes image little bit sharper.
4. resize.py - Resizes image to some height and width.
1. `rotate.py` - Rotates an image.
2. `blur.py` - Blurs an image.
3. `sharper.py` - Makes image little bit sharper.
4. `resize.py` - Resizes image to some height and width.

There is more files (ex. writeText.py) but theese are not working yet (that can be good contribution! 🎉)

## Options

Every otion is availibe only in equal file (ex. -b ➡ blur.py)

`-b` - Blurs image. Specify with number of blury level (int)
`-r` - Rotates an image. Specify with degree (int)
`-wT` - Writes text to image. Specify with text (string) - ! not working yet !

`-s` Makes image sharper (bool).

`-height`, `-width` - include theese two flags if you want to resize an image (int).
* `-b` - Blurs image. Specify with number of blurriness level (int)
* `-r` - Rotates an image. Specify with the number degrees to rotate (int)
* `-w` - Writes text to image. Specify with text (string) - *** not working yet ***
* `-s` - Makes image sharper (bool).
* `-R` - Resizes an image to a specified size (int, int). Include the height and width as two integer values following the flag. Example: `-R 800 640` will resize an image to 800x640.

## Contribution

Contributions are welcome! Start by forking this repo, making changes and creating a pull request! If you have any more question or just want to talk, contact me please on email rojtomas@email.cz.

## About

Created by @TomasRoj on 27. April on rainy saturday on living room sofa.

Tomáš Roj, rojtomas@email.cz
This and other my projects are avalibe under MIT license. See LICENSE file for more info.

### Contributors

* [Alec Trievel](https://github.com/atrievel)
