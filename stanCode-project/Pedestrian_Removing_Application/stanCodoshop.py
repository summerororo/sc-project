"""
File: stanCodoshop.py
Name: 黃兆嘉Summer
----------------------------------------------
SC101_Assignment3
Adapted from Nick Parlante's
Ghost assignment by Jerry Liao.

-----------------------------------------------

TODO:
"""

import os
import sys
from simpleimage import SimpleImage


def get_pixel_dist(pixel, red, green, blue):
    """
    Returns the color distance between pixel and mean RGB value

    Input:
        pixel (Pixel): pixel with RGB values to be compared
        red (int): average red value across all images
        green (int): average green value across all images
        blue (int): average blue value across all images

    Returns:
        dist (float): color distance between red, green, and blue pixel values

    """
    color_dist = ((red - pixel.red)**2 + (green - pixel.green)**2 + (blue - pixel.blue)**2)**0.5
    return color_dist


def get_average(pixels):
    """
    Given a list of pixels, finds the average red, blue, and green values

    Input:
        pixels (List[Pixel]): list of pixels to be averaged
    Returns:
        rgb (List[int]): list of average red, green, blue values across pixels respectively

    Assumes you are returning in the order: [red, green, blue]

    """
    red = 0
    green = 0
    blue = 0
    for pixel in pixels:
        red += pixel.red
        green += pixel.green
        blue += pixel.blue
    avg_red = red // len(pixels)
    avg_green = green // len(pixels)
    avg_blue = blue // len(pixels)
    rgb = [avg_red, avg_green, avg_blue]
    return rgb


def get_best_pixel(pixels):
    """
    Given a list of pixels, returns the pixel with the smallest
    distance from the average red, green, and blue values across all pixels.

    Input:
        pixels (List[Pixel]): list of pixels to be averaged and compared
    Returns:
        best (Pixel): pixel closest to RGB averages

    """
    smallest = 0
    for pixel in pixels:
        rgb = get_average(pixels)
        color_distance = get_pixel_dist(pixel, rgb[0], rgb[1], rgb[2])
        if smallest == 0:
            smallest = color_distance
            the_best_one = pixel
        elif color_distance <= smallest:
            smallest = color_distance
            the_best_one = pixel
    return the_best_one


def solve(images):
    """
    Given a list of image objects, compute and display a Ghost solution image
    based on these images. There will be at least 3 images and they will all
    be the same size.

    Input:
        images (List[SimpleImage]): list of images to be processed
    """
    width = images[0].width
    height = images[0].height
    result = SimpleImage.blank(width, height)
    ######## YOUR CODE STARTS HERE #########
    # Write code to populate image and create the 'ghost' effect
    # the_images = SimpleImage(images) # 不用再對the_images用SimpleImage
    for x in range(result.width):
        for y in range(result.height):
            # It has RGB
            img_pixel_lst = list(img.get_pixel(x, y) for img in images)
            best_pixel = get_best_pixel(img_pixel_lst)
            # It doesn't have RGB
            result_pixel = result.get_pixel(x, y)
            result_pixel.red = best_pixel.red
            result_pixel.green = best_pixel.green
            result_pixel.blue = best_pixel.blue
    ######## YOUR CODE ENDS HERE ###########
    print("Displaying image!")
    result.show()      # 人還在OAO


def jpgs_in_dir(dir):
    """
    (provided, DO NOT MODIFY)
    Given the name of a directory, returns a list of the .jpg filenames
    within it.

    Input:
        dir (string): name of directory
    Returns:
        filenames(List[string]): names of jpg files in directory
    """
    filenames = []
    for filename in os.listdir(dir):
        if filename.endswith('.jpg'):
            filenames.append(os.path.join(dir, filename))
    return filenames


def load_images(dir):
    """
    (provided, DO NOT MODIFY)
    Given a directory name, reads all the .jpg files within it into memory and
    returns them in a list. Prints the filenames out as it goes.

    Input:
        dir (string): name of directory
    Returns:
        images (List[SimpleImages]): list of images in directory
    """
    images = []
    jpgs = jpgs_in_dir(dir)
    for filename in jpgs:
        print("Loading", filename)
        image = SimpleImage(filename)
        images.append(image)
    return images


def main():
    # (provided, DO NOT MODIFY)
    args = sys.argv[1:]
    # We just take 1 argument, the folder containing all the images.
    # The load_images() capability is provided above.
    images = load_images(args[0])
    solve(images)


if __name__ == '__main__':
    main()
