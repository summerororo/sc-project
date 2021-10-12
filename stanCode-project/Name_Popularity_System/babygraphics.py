"""
SC101 Baby Names Project
Adapted from Nick Parlante's Baby Names assignment by
Jerry Liao.

YOUR DESCRIPTION HERE
"""

import tkinter
import babynames
import babygraphicsgui as gui

FILENAMES = [
    'data/full/baby-1900.txt', 'data/full/baby-1910.txt',
    'data/full/baby-1920.txt', 'data/full/baby-1930.txt',
    'data/full/baby-1940.txt', 'data/full/baby-1950.txt',
    'data/full/baby-1960.txt', 'data/full/baby-1970.txt',
    'data/full/baby-1980.txt', 'data/full/baby-1990.txt',
    'data/full/baby-2000.txt', 'data/full/baby-2010.txt'
]
CANVAS_WIDTH = 1000
CANVAS_HEIGHT = 600
YEARS = [1900, 1910, 1920, 1930, 1940, 1950, 1960, 1970, 1980, 1990, 2000, 2010]
GRAPH_MARGIN_SIZE = 20
COLORS = ['red', 'purple', 'green', 'blue']
TEXT_DX = 2
LINE_WIDTH = 2
MAX_RANK = 1000


def get_x_coordinate(width, year_index):
    """
    Given the width of the canvas and the index of the current year
    in the YEARS list, returns the x coordinate of the vertical
    line associated with that year.

    Input:
        width (int): The width of the canvas
        year_index (int): The index of the current year in the YEARS list
    Returns:
        x_coordinate (int): The x coordinate of the vertical line associated
                              with the specified year.
    """
    gap_distance = (width-2*GRAPH_MARGIN_SIZE)//len(YEARS)
    x_coordinate = year_index*gap_distance + GRAPH_MARGIN_SIZE
    return x_coordinate


def draw_fixed_lines(canvas):
    """
    Erases all existing information on the given canvas and then
    draws the fixed background lines on it.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.

    Returns:
        This function does not return any value.
    """
    canvas.delete('all')            # delete all existing lines from the canvas

    # Write your code below this line
    #################################
    # the upper line
    canvas.create_line(GRAPH_MARGIN_SIZE, GRAPH_MARGIN_SIZE,
                       CANVAS_WIDTH-GRAPH_MARGIN_SIZE, GRAPH_MARGIN_SIZE,
                       width=LINE_WIDTH)
    # the lower line
    canvas.create_line(GRAPH_MARGIN_SIZE, CANVAS_HEIGHT-GRAPH_MARGIN_SIZE,
                       CANVAS_WIDTH-GRAPH_MARGIN_SIZE, CANVAS_HEIGHT-GRAPH_MARGIN_SIZE,
                       width=LINE_WIDTH)

    # add coordinate lines and text
    for i in range(len(YEARS)):
        the_x_coordinate = get_x_coordinate(CANVAS_WIDTH, i)
        canvas.create_line(the_x_coordinate, 0, the_x_coordinate, CANVAS_HEIGHT, width=LINE_WIDTH)
        canvas.create_text(the_x_coordinate+TEXT_DX, CANVAS_HEIGHT-GRAPH_MARGIN_SIZE,
                           text=YEARS[i], anchor=tkinter.NW)


def draw_names(canvas, name_data, lookup_names):
    """
    Given a dict of baby name data and a list of name, plots
    the historical trend of those names onto the canvas.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.
        name_data (dict): Dictionary holding baby name data
        lookup_names (List[str]): A list of names whose data you want to plot

    Returns:
        This function does not return any value.
    """
    draw_fixed_lines(canvas)        # draw the fixed background grid

    # Write your code below this line
    #################################

    color_index = -1
    for name in lookup_names:
        color_index += 1
        for j in range(len(YEARS)-1):
            color = COLORS[color_index % len(COLORS)]
            # x 座標
            x_1 = get_x_coordinate(CANVAS_WIDTH, j)
            x_2 = get_x_coordinate(CANVAS_WIDTH, j+1)
            # y 座標
            if name in name_data:
                # start of the line
                if str(YEARS[j]) in name_data[name]:
                    rank_1 = name_data[name][str(YEARS[j])]
                    y_1 = (((CANVAS_HEIGHT - 2 * GRAPH_MARGIN_SIZE) * rank_1) / 1000) + GRAPH_MARGIN_SIZE
                    text_1 = name + str(' ') + str(rank_1)
                else:
                    y_1 = CANVAS_HEIGHT - GRAPH_MARGIN_SIZE
                    text_1 = name + str(' *')
                # end of the line
                if str(YEARS[j+1]) in name_data[name]:
                    rank_2 = name_data[name][str(YEARS[j+1])]
                    y_2 = (((CANVAS_HEIGHT - 2 * GRAPH_MARGIN_SIZE) * rank_2) / 1000) + GRAPH_MARGIN_SIZE
                    text_2 = name + str(' ') + str(rank_2)
                else:
                    y_2 = CANVAS_HEIGHT - GRAPH_MARGIN_SIZE
                    text_2 = name + str(' *')
            else:
                break
            # create line
            canvas.create_line(x_1, y_1, x_2, y_2, width=LINE_WIDTH, fill=color)
            # create text
            canvas.create_text(x_1 + TEXT_DX, y_1, text=text_1, anchor=tkinter.SW, fill=color)
            if j == (len(YEARS)-2):
                canvas.create_text(x_2 + TEXT_DX, y_2, text=text_2, anchor=tkinter.SW, fill=color)


# main() code is provided, feel free to read through it but DO NOT MODIFY
def main():
    # Load data
    name_data = babynames.read_files(FILENAMES)

    # Create the window and the canvas
    top = tkinter.Tk()
    top.wm_title('Baby Names')
    canvas = gui.make_gui(top, CANVAS_WIDTH, CANVAS_HEIGHT, name_data, draw_names, babynames.search_names)

    # Call draw_fixed_lines() once at startup so we have the lines
    # even before the user types anything.
    draw_fixed_lines(canvas)

    # This line starts the graphical loop that is responsible for
    # processing user interactions and plotting data
    top.mainloop()


if __name__ == '__main__':
    main()
