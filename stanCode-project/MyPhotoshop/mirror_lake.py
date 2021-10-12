"""
File: mirror_lake.py
----------------------------------
This file reads in mt-rainier.jpg and
makes a new image that creates a mirror
lake vibe by placing an inverse image of
mt-rainier.jpg below the original one.
"""
from simpleimage import SimpleImage


def reflect(filename):
    """
    :param filename: The filename
    :return: blank_img
    """
    original_mt = SimpleImage(filename)

    blank_img = SimpleImage.blank(original_mt.width, original_mt.height*2)
    blank_img.show()

    for x in range(original_mt.width):
        for y in range(original_mt.height):
            # get color
            original_pixel = original_mt.get_pixel(x, y)

            # blank 1
            blank1_pixel = blank_img.get_pixel(x, y)
            blank1_pixel.red = original_pixel.red
            blank1_pixel.green = original_pixel.green
            blank1_pixel.blue = original_pixel.blue

            # blank2
            blank2_pixel = blank_img.get_pixel(x, blank_img.height - 1 - y)
            blank2_pixel.red = original_pixel.red
            blank2_pixel.green = original_pixel.green
            blank2_pixel.blue = original_pixel.blue
    return blank_img


def main():
    """
    flip the image vertically
    """
    original_mt = SimpleImage('images/mt-rainier.jpg')
    original_mt.show()

    reflected = reflect('images/mt-rainier.jpg')
    reflected.show()


if __name__ == '__main__':
    main()
