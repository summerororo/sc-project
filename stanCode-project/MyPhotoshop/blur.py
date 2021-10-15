"""
File: blur.py
-------------------------------
This file shows the original image(smiley-face.png)
first, and then its blurred image. The blur algorithm
uses the average RGB values of a pixel's nearest neighbors.
"""

from simpleimage import SimpleImage


def blur(img):
    """
    :param img:
    :return: new_img
    """
    old_img = SimpleImage("images/smiley-face.png")
    new_img = SimpleImage.blank(old_img.width, old_img.height)
    for x in range(old_img.width):
        for y in range(old_img.height):
            old_pixel = old_img.get_pixel(x, y)
            new_pixel = new_img.get_pixel(x, y)
            # middle
            if 0 < x < old_img.width-1 and 0 < y < old_img.height-1:
                new_pixel.red = old_pixel.



def main():
    """
    TODO:
    """
    old_img = SimpleImage("images/smiley-face.png")
    old_img.show()


    blurred_img = blur(old_img)
    for i in range(5):
        blurred_img = blur(blurred_img)
    blurred_img.show()


if __name__ == '__main__':
    main()
