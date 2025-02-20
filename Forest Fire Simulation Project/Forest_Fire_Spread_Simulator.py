"""
Sophia Rosicky
COMP 1353
May 1, 2024
Percolation Project (Part One: Search Algorithms)
File Name: Rosicky_Project_3.py
"""

import random
from Stack import Stack
from Queue import Queue
import dudraw
import matplotlib.pyplot as plt


# -- FOREST CLASS --
#class that intakes a random 2d list of 0s and 1s to represent a forest of density d, with height (h) and width (w)

class Forest:
    def __init__(self, h, w, d):
        self.height = h
        self.width = w
        self.density = d
        self.forest = [[1 if random.random() < d else 0 for i in range(self.width)] for j in range(self.height)]
    
    def __str__(self):
        return str(self.forest)

    def __iter__(self):
        return ForestIterator(self.forest)

    def draw(self):

        dudraw.set_x_scale(0, self.width)
        dudraw.set_y_scale(0, self.height)
        for i in range(self.height):
            for j in range(self.width):
                if self.forest[i][j] == 1:
                    dudraw.set_pen_color_rgb(0, 255, 0)
                    dudraw.filled_square(j+.5, (self.height - 1 - i)+.5, .5)
                if self.forest[i][j] == 2:
                    dudraw.set_pen_color_rgb(255, 0, 0)
                    dudraw.filled_square(j+.5, (self.height - 1 - i)+.5, .5)
        dudraw.show(50)
	
    
    #Depth First Search: this search algorithm uses a stack data structure
    def depth_first_search(self, row):
        cells_to_explore = Stack()
    
        for i in range(self.width):
            if self.forest[row][i] == 1:
                cells_to_explore.push([row, i]) #push a coordinate onto the stack for each cell -> [row, column]
                self.forest[row][i] = 2 #light on fire


        while not cells_to_explore.is_empty():
            # self.draw()
            #pop top value off stack and assign it to current cell
            current_cell = cells_to_explore.pop()

            #edge case: the current cell is in the bottom row
            if current_cell.value[0] == self.height - 1:
                return True

            #create variables to track the position of the current cell and nearby cells
            row_num = current_cell.value[0]
            column_num = current_cell.value[1]
            
            #check above
            if row_num != 0:    #must not be the first row
                if self.forest[row_num - 1][column_num] == 1:
                    cells_to_explore.push([row_num -1, column_num])
                    self.forest[row_num - 1][column_num] = 2

            #check right
            if column_num + 1 != self.width:    #must not be the last column on the right
                if self.forest[row_num][column_num + 1] == 1:
                    cells_to_explore.push([row_num, column_num + 1])
                    self.forest[row_num][column_num + 1] = 2

            #check left
            if column_num != 0:    #must not be the first column
                if self.forest[row_num][column_num - 1] == 1:
                    cells_to_explore.push([row_num, column_num - 1])
                    self.forest[row_num][column_num - 1] = 2

            #check bottom
            if self.forest[row_num + 1][column_num] == 1:
                cells_to_explore.push([row_num + 1, column_num])
                self.forest[row_num + 1][column_num] = 2
        return False

    #Breadth First Search: this search algorithm uses a queue data structure
    def breadth_first_search(self, row):
        cells_to_explore = Queue()
    
        for i in range(self.width):
            if self.forest[row][i] == 1:
                cells_to_explore.enqueue([row, i]) 
                self.forest[row][i] = 2 #light on fire


        while not cells_to_explore.is_empty():
            # self.draw()
            
            current_cell = cells_to_explore.dequeue()

            
            if current_cell[0] == self.height - 1:
                return True

            
            row_num = current_cell[0]
            column_num = current_cell[1]
            
            #check above
            if row_num != 0:    #must not be the first row
                if self.forest[row_num - 1][column_num] == 1:
                    cells_to_explore.enqueue([row_num -1, column_num])
                    self.forest[row_num - 1][column_num] = 2

            #check right
            if column_num + 1 != self.width:    #must not be the last column on the right
                if self.forest[row_num][column_num + 1] == 1:
                    cells_to_explore.enqueue([row_num, column_num + 1])
                    self.forest[row_num][column_num + 1] = 2

            #check left
            if column_num != 0:    #must not be the first column
                if self.forest[row_num][column_num - 1] == 1:
                    cells_to_explore.enqueue([row_num, column_num - 1])
                    self.forest[row_num][column_num - 1] = 2

            #check bottom

            if self.forest[row_num + 1][column_num] == 1:
                cells_to_explore.enqueue([row_num + 1, column_num])
                self.forest[row_num + 1][column_num] = 2
        return False


class ForestIterator:
    def __init__(self, list):
        self.list = list
        self.current = 0

    def __next__(self):
        if self.current < len(self.list):
            value = self.list[self.current]
            self.current += 1
            return value
        else:
            raise StopIteration
    
    def __iter__(self):
        return self


# -- PROBABILITY OF SPREAD FOR SINGLE DENSITY --

def prob_of_spread_depth(grid_parameter, density: float):
    fire_spread_count = 0
    for i in range(10000):
        forest = Forest(grid_parameter, grid_parameter, density)
        if forest.depth_first_search(0) == True:
            fire_spread_count += 1
    
    return f"PROBABILITY OF SPREAD: {fire_spread_count/10000}%"

def prob_of_spread_breadth(grid_parameter, density: float):
    fire_spread_count = 0
    for i in range(10000):
        forest = Forest(grid_parameter, grid_parameter, density)
        if forest.breadth_first_search(0) == True:
            fire_spread_count += 1
    
    return f"PROBABILITY OF SPREAD: {fire_spread_count/10000}%"


# -- MAXIMUM DENSITY CALCULATION CLASS --

class FireProbability:

    def __init__(self, grid_parameter):
        self.grid_parameter = grid_parameter

    def prob_of_spread_depth(self, density, trials):
        fire_spread_count = 0
        for i in range(trials):
            forest = Forest(self.grid_parameter, self.grid_parameter, density)
            if forest.depth_first_search(0) == True:
                fire_spread_count += 1
        
        return fire_spread_count/trials
    
    def prob_of_spread_breadth(self, density, trials):
        fire_spread_count = 0
        for i in range(trials):
            forest = Forest(self.grid_parameter, self.grid_parameter, density)
            if forest.breadth_first_search(0) == True:
                fire_spread_count += 1
        
        return fire_spread_count/trials
    
    def highest_density_depth(self):

        low_density = 0.0
        high_density = 1.0

        while high_density != low_density:
            density = (high_density + low_density) / 2.0
            p = self.prob_of_spread_depth(density, 100)
            if p < 0.5:
                low_density = density
            else:
                high_density = density
        return density

    def highest_density_breadth(self):

        low_density = 0.0
        high_density = 1.0

        while high_density != low_density:
            density = (high_density + low_density) / 2.0
            p = self.prob_of_spread_breadth(density, 100)
            if p < 0.5:
                low_density = density
            else:
                high_density = density
        return density
                


# -- TEST CODE --

#initialize the probablity class with the selected dimensions of the forest
spread = FireProbability(20)

#print the probability of spread using depth first search
#parameters: density, trials
print(spread.prob_of_spread_depth(0.6, 1000))

#print the highest possible density for the probability of spread to be higher than 0.5 when using depth first search
#no parameters
print(spread.highest_density_depth())

#print the probability of spread using breadth first search
#parameters: density, trials
print(spread.prob_of_spread_breadth(0.6, 1000))

#print the highest possible density for the probability of spread to be higher than 0.5 when using breadth first search
#no parameters
print(spread.highest_density_breadth())

spread = FireProbability(20)

current_density = 0.0
high_density = 1.0

x_values = []
y_values = []


while current_density <= high_density:

    x_values.append(current_density)
    y_values.append(spread.prob_of_spread_breadth(current_density, 100))
    (current_density) += 0.01

print(x_values)
print(y_values)

plt.xlabel("forest density")
plt.ylabel("probability of spread")

plt.plot(x_values, y_values)
plt.show()





