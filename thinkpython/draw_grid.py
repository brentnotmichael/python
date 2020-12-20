#!/usr/bin/python

# def defines a function
# function header ends with a colon:
# ''' is a docstring and describes what the  function does '''
# docstrings are the first line in a function and must be comments

def draw_grid(intRows,intCols,intCellWidth,intCellHeight):
    '''draws a grid
    intRows - number of rows
    intCols - number of columns
    intCellWidth - width of a cell, the number is multiplied by 2 to account for the height of a cell, visually more pleasing
    intCellHeight - height of a cell in lines'''

    # inner functions are encapsulated in their outer function (here, draw_grid)
    # inner functions are not accessible outside their outer function
    # inner functions obey program flow and MUST be defined before they are called
    # placing the for loop at the top of the function would not work, since draw_grid_line
    # and draw_grid_hspace would not have yet been defined
    def draw_grid_hline(intCols, intCellWidth):
        '''draws the horizontal lines of the grid'''
        for i in range(0, intCols):
            print("+" + "-" * intCellWidth*2, end="")
        print("+")

    def draw_grid_hspace(intCols, intCellWidth, intCellHeight):
        '''draws the horizontal spaces of the grid, including all vertical lines'''
        # TODO: it would make more sense to build this part to draw a box rather than a row
        for height in range(0, intCellHeight):
            for width in range(0,intCols):
                print("|" + " " * intCellWidth*2, end="")
            print("|")

    # for loop that calls the other functions
    for row in range(0,intRows):
        draw_grid_hline(intCols, intCellWidth)
        draw_grid_hspace(intCols, intCellWidth, intCellHeight)
    draw_grid_hline(intCols, intCellWidth)

# rows, cols, colwidth, colheight
draw_grid(2,5,3,2)


