from turtle import Turtle, pos

INITIAL_POS = [(0,0), (-20,0),(-40,0)]
MOVEMENT = 20
STARTING_TILES = 3

class Snake():
    def __init__(self) -> None:
        self.snake_body_position = (0,0)
        self.snake_body = []
        self.create_snake()
        self.head = self.snake_body[0]
        
    def create_snake(self):
        for pos in INITIAL_POS:
            self.add_segement(pos)

    def add_segement(self,position):
        seg = Turtle("circle")
        seg.penup()
        seg.color("red")
        seg.goto(position)
        self.snake_body.append(seg)

    def extend(self):
        self.add_segement(self.snake_body[-1].position())

    def move(self):
        for i in range(len(self.snake_body)-1,0,-1):
            pos = self.snake_body[i - 1].position()
            self.snake_body[i].goto(pos)
        self.head.forward(MOVEMENT)
    
    def change_direction(self,angle):
        if abs(self.head.heading() - angle) == 180:
            return

        self.head.setheading(angle)