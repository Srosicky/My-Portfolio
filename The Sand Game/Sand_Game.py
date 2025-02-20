"""
 Filename: Sand_Game_Pt2.py
 Author: Sophia Rosicky
 Date: 2/25/2024
 Course: COMP 1352
 Assignment: Sand Game Part 2
 Collaborators: None
 Internet Source: None
"""

import dudraw
from random import randint
from dudraw import Color

size = 200
x_buffer = 10
y_buffer = 10

dudraw.set_x_scale(0, size)
dudraw.set_y_scale(0, size)
dudraw.set_canvas_size(600, 600)

dudraw.set_pen_color_rgb(123, 123, 123)

#create a nested list for floor
floor_list = []
for i in range(size):
    row = []
    for j in range(size):
        row.append(0)
    floor_list.append(row)

#create a nested list for water
water_list = []
for i in range(size):
    row = []
    for j in range(size):
        row.append(0)
    water_list.append(row)

#create a nested list for sand
sand_list = []
for i in range(size):
    row = []
    for j in range(size):
        row.append(0)
    sand_list.append(row)



mode = 'sand mode'
dudraw.text(20, 190, mode)
key = ''
while key != 'q':
    
    if key == 's':
        mode = 'sand mode'
    
    if key == 'f':
        mode = 'floor mode'

    if key == 'w':
        mode = 'water mode'
    
    dudraw.set_pen_color_rgb(0, 0, 0)
    dudraw.text(20, 190, mode)

    for row in range(size):
        for column in range(size):
            if sand_list[row][column] == 1:
                dudraw.filled_square(column - 0.5, size-row, 0.5)
    
    for row in range(size):
        for column in range(size):
            if floor_list[row][column] == 1:
                dudraw.filled_square(column - 0.5, size-row, 0.5)

    for row in range(size):
        for column in range(size):
            if water_list[row][column] == 1:
                dudraw.set_pen_color_rgb(0, 0, 225)
                dudraw.filled_square(column - 0.5, size-row, 0.5)
            

    if dudraw.mouse_is_pressed() and mode == 'sand mode':

        mouse_x = int(dudraw.mouse_x())
        mouse_y = int(dudraw.mouse_y())

        x_position = mouse_x + randint(-x_buffer, x_buffer)

        y_position = size-mouse_y + randint(-y_buffer, y_buffer)

        if x_position < size and x_position > 0:
            if y_position <size and y_position > 0:
                sand_list[y_position][x_position] = 1

    
    for row in range(size, 0, -1):
        for column in range(size):
            if row < size - 1:

                #is there a floor particle beneath the current sand particle?
                if floor_list[row+1][column] == 1 or water_list[row+1][column] == 1:
                    sand_list[row][column] == 1
                #is there a sand particle beneath the current one? If no, move down.
                elif sand_list[row][column] == 1 and sand_list[row+1][column] == 0:
                    sand_list[row + 1][column] = 1
                    sand_list[row][column] = 0
                #is there a sand particle to the right diagonal of the current one? If no, move to lower right diagonal.
                elif sand_list[row][column] == 1 and sand_list[row + 1][column + 1] == 0:
                    sand_list[row + 1][column + 1] = 1
                    sand_list[row][column] = 0
                #is there a sand particle to the left diagnonal of the current one? If no, move to lower left diagonal
                elif sand_list[row][column] == 1 and sand_list[row + 1][column - 1] == 0:
                    sand_list[row + 1][column - 1] = 1
                    sand_list[row][column] = 0
                
               
                
                

    if dudraw.mouse_is_pressed() and mode == 'floor mode':

        mouse_x = int(dudraw.mouse_x())
        mouse_y = int(dudraw.mouse_y())

        x_position = mouse_x

        y_position = size-mouse_y

        if x_position < size and x_position > 0:
            if y_position <size and y_position > 0:
                floor_list[y_position][x_position] = 1
                floor_list[y_position+1][x_position] = 1
    
    if dudraw.mouse_is_pressed() and mode == 'water mode':

        mouse_x = int(dudraw.mouse_x())
        mouse_y = int(dudraw.mouse_y())

        x_position = mouse_x + randint(-x_buffer, x_buffer)

        y_position = size-mouse_y + randint(-y_buffer, y_buffer)

        if x_position < size and x_position > 0:
            if y_position <size and y_position > 0:
                water_list[y_position][x_position] = 1

    
    for row in range(size, 0, -1):
        for column in range(size):
            if row < size - 1:

                #is there a floor particle beneath the current water particle?
                if floor_list[row+1][column] == 1 or sand_list[row+1][column] == 1:
                    water_list[row][column] == 1
                #is there a water particle beneath the current one? If no, move down.
                elif water_list[row][column] == 1 and water_list[row+1][column] == 0:
                    water_list[row + 1][column] = 1
                    water_list[row][column] = 0
                #is there a water particle to the right diagonal of the current one? If no, move to lower right diagonal.
                elif water_list[row][column] == 1 and water_list[row + 1][column + 1] == 0:
                    water_list[row + 1][column + 1] = 1
                    water_list[row][column] = 0
                #is there a water particle to the left diagnonal of the current one? If no, move to lower left diagonal
                elif water_list[row][column] == 1 and water_list[row + 1][column - 1] == 0:
                    water_list[row + 1][column - 1] = 1
                    water_list[row][column] = 0
                #is there a water particle to the right diagonal of the current one? If no, move to lower right diagonal.
                if water_list[row][column] == 1 and water_list[row][column + 1] == 0:
                    if column + 1 < len(water_list):
                        water_list[row][column + 1] = 1
                        water_list[row][column] = 0
                #is there a water particle to the left diagnonal of the current one? If no, move to lower left diagonal
                if water_list[row][column] == 1 and water_list[row][column - 1] == 0:
                    if column - 1 > 0:
                        water_list[row][column - 1] = 1
                        water_list[row][column] = 0



    
    key = dudraw.next_key()

    dudraw.show(1)
    dudraw.clear()


    


