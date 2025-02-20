from DoublyLinkedList2 import DoublyLinkedList
import random
import time
import dudraw

# -- SNAKE GAME CLASSES --

class SnakePiece:
    def __init__(self, x, y):
        self.x_coordinate = x
        self.y_coordinate = y
        self.size = 0

    def draw_snakey(self): 
        self.size += 1
        r = random.randint(0,255) #make the snake RAINBOW!
        g = random.randint(0,255)
        b = random.randint(0,255)
        dudraw.set_pen_color_rgb(r,g,b)
        dudraw.filled_square(self.x_coordinate, self.y_coordinate, 0.5)  #uses the coordinates passed to draw the snake in a spot
        
class Snake: #creates the "container" for the SnakePiece, which are the values for the nodes
    def __init__(self, food):
        self.body = DoublyLinkedList()
        self.direction = random.randint(0,3) #randomizes the direction to start
        self.first_piece = SnakePiece((random.randint(0,15)), (random.randint(0,15))) #randomizes the snake's start position - Made it in between 15/15 because otherwise it would end too fast
        self.grow_snake = False
        self.food = food
        
    def start_snake(self):
        self.body.add_first(self.first_piece) #starts the snake in a random spot

    def process_keyboard(self): #checking which direction the snake is going to move in
        if dudraw.has_next_key_typed():
            key = dudraw.next_key_typed()

            if key == 'd':
                self.direction = 0 #right

            elif key == 'a':
                self.direction = 1 #left

            elif key == 'w':
                self.direction = 2 #up

            elif key == 's':
                self.direction = 3 #down

    def move(self):
        current_first = self.body.header.next.value

        if self.direction == 0: #right
            Next_snake = SnakePiece(current_first.x_coordinate + 1, current_first.y_coordinate)
            
        elif self.direction == 1: #left
            Next_snake = SnakePiece(current_first.x_coordinate - 1, current_first.y_coordinate)

        elif self.direction == 2: #up
            Next_snake = SnakePiece(current_first.x_coordinate, current_first.y_coordinate + 1)

        elif self.direction == 3: #down
            Next_snake = SnakePiece(current_first.x_coordinate, current_first.y_coordinate - 1)
        
        self.body.add_first(Next_snake) #advancing the snake one forward
        self.body.header.next.value = Next_snake #setting it so that the coordinates can change
        
        if self.hits_food(snack) == True:
            self.grow_snake = False    #resetting grow to false, but keeping the end piece on.
        
        else: 
            self.body.remove_last() #removing the last snakey piece, if the snake didn't get any food

    def draw(self): #for every snake piece, draw it one at a time.
        size = self.body.get_size()
        temp_node = self.body.header.next
        current_snakey = temp_node.value
        for i in range(0,size):
            current_snakey.draw_snakey()
            temp_node = temp_node.next
            current_snakey = temp_node.value

    def hits_food(self, food): #if the snake hits the food, then make it grow longer and make the food disappear
        current_first = self.body.header.next
        if current_first.value.x_coordinate == food.x and current_first.value.y_coordinate == food.y:
            self.grow_snake = True
            return True
        else:
            return False
    
    def eat_food(self, food): #make the new food generate!
        self.grow_snake = True
        snack.new_food() #generate new food

    def hits_wall(self): # if the snake goes off the map, end the game
        current_first = self.body.header.next
        if current_first.value.x_coordinate >= 20 or current_first.value.y_coordinate >= 20 or current_first.value.x_coordinate <= 0 or current_first.value.y_coordinate <= 0:
            return True
        else:
            return False
    
    def collides(self): #if the snake hits itself, end game
        size = self.body.get_size()
        if size <= 1:
            return False
        first_snake = self.body.header.next
        temp_node = self.body.header.next.next
        current_snakey = temp_node
        for i in range(0,size):
            if current_snakey.value.x_coordinate == first_snake.value.x_coordinate and current_snakey.value.y_coordinate == first_snake.value.y_coordinate:
                return True
            else:
                temp_node = self.body.header.next.next
                current_snakey = temp_node
    

class FoodPiece:
    def __init__(self):
        self.x = (random.randint(0,18)) #at 18, because otherwise the food it cut off by the wall
        self.y = (random.randint(0,18))

    def draw_food(self):
        dudraw.set_pen_color(dudraw.RED)
        dudraw.filled_square(self.x, self.y, 0.5) 
    
    def new_food(self):
        self.x = (random.randint(0,18)) #creates new random place for new food
        self.y = (random.randint(0,18))

    def reset_food(self): #draw new food if the food is eaten
        self.new_food()
        dudraw.clear(dudraw.WHITE)
        self.draw_food()


# -- CANVAS AND LIST INITIALIZATIONS --

dudraw.set_canvas_size(800,800)
dudraw.set_x_scale(0,20)
dudraw.set_y_scale(0,20)
dudraw.clear(dudraw.WHITE)

limit = 100 #number of frames to allow to pass before snake moves
timer = 0  #a timer to keep track of number of frames that passed

snack = FoodPiece()
snake_buddy = Snake(snack)
snake_buddy.start_snake()

def game_over():
        dudraw. set_pen_color(dudraw.RED)
        dudraw.filled_rectangle(10, 10, 2, 1)
        dudraw.set_pen_color(dudraw.BLACK)
        dudraw.text(10, 10, "GAME OVER")
        key = 'q'


# -- MAIN DRIVER LOOP --
key = ''

while key != 'q':
    timer += 1
    dudraw.clear(dudraw.WHITE)
    snack.draw_food()
    snake_buddy.draw()
    snake_buddy.move()
    snake_buddy.process_keyboard()
    if timer >= limit:
        timer = 0
        dudraw.clear(dudraw.WHITE)
        snack.new_food()
        snake_buddy.draw()
        snake_buddy.move() 

    if snake_buddy.hits_food(snack) == True:   
        snake_buddy.eat_food(snack)
        
    if snake_buddy.hits_wall() == True:    
        game_over()
    
    if snake_buddy.collides() == True:
        game_over()


    dudraw.show(40)

    time.sleep(0.1)
dudraw.show(20000)
