"""
File: best_photoshop_award.py
----------------------------------
This file creates a photoshopped image
that is going to compete for the Best
Photoshop Award for SC001.
Please put all the images you will use in the image_contest folder
and make sure to choose the right folder when loading your images.
"""
from simpleimage import SimpleImage

THRESHOLD = 1.2

BLACK＿PIXEL = 120


def main():
    """
    combine the background and the figure
    """
    background = SimpleImage("image_contest/background.png")
    figure = SimpleImage("image_contest/myphoto.jpeg")
    background.make_as_big_as(figure)
    combination = combine(background, figure)
    combination.show()


def combine(background, figure):
    for x in range(background.width):
        for y in range(background.height):
            figure_pixel = figure.get_pixel(x, y)
            background_pixel = background.get_pixel(x, y)
            avg = (figure_pixel.red + figure_pixel.green + figure_pixel.blue) // 3
            total = figure_pixel.red + figure_pixel.green + figure_pixel.blue
            if figure_pixel.green > avg*THRESHOLD and total > BLACK＿PIXEL:
                figure_pixel.red = background_pixel.red
                figure_pixel.green = background_pixel.green
                figure_pixel.blue = figure_pixel.blue + 250
    return figure


if __name__ == '__main__':
    main()
