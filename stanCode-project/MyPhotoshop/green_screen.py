"""
File: green_screen.py
-------------------------------
This file creates a new image that uses
MillenniumFalcon.png as background and
replace the green pixels in "ReyGreenScreen.png".
"""

from simpleimage import SimpleImage


def combine(background_img, figure_img):
    """
    :param background_img: the substitute for the green screen
    :param figure_img: the picture
    :return: the combined image
    """
    space_ship = SimpleImage("images/MillenniumFalcon.png")
    figure = SimpleImage("images/ReyGreenScreen.png")
    for x in range(figure.width):
        for y in range(figure.height):
            figure_pixel = figure.get_pixel(x, y)
            space_ship_pixel = space_ship.get_pixel(x, y)
            bigger = max(figure_pixel.red, figure_pixel.blue)
            the_green = bigger*2
            if figure_pixel.green > the_green:
                figure_pixel.red = space_ship_pixel.red
                figure_pixel.green = space_ship_pixel.green
                figure_pixel.blue = space_ship_pixel.blue
    return figure


def main():
    """
    remove the green screen
    """
    space_ship = SimpleImage("images/MillenniumFalcon.png")
    figure = SimpleImage("images/ReyGreenScreen.png")
    figure.show()

    result = combine(space_ship, figure)
    result.show()


if __name__ == '__main__':
    main()
