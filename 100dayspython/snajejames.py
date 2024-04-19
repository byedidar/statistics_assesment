import time
from turtle import Turtle
import random
import turtle
from turtle import Turtle,Screen






class FOOD(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.hideturtle()
        self.penup()
        self.shapesize(0.5)
        self.color("red")
        self.speed('fastest')
        self.refresh()

    def refresh(self):
        x, y = random.randint(-280, 280), random.randint(-280, 280)
        (self.goto(x, y))
        (self.showturtle())
from turtle import Turtle,Screen
FONT = ("Courier", 20, "normal")
class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color('white')
        self.hideturtle()
        self.penup()
        self.goto(0,270)
        self.write(f'Score: {self.score}', align='center', font= FONT)

    def increment(self):
        self.clear()
        self.score += 1
        self.write(f'Score: {self.score}', align='center', font=FONT)

    def game_over(self):
        self.goto(0,0)
        self.write('GAME OVER', align='center', font=FONT)
        self.goto(-120,-30)
        self.write(f"Your score is {self.score}", align='left', font=FONT)

from turtle import Turtle,Screen
positions=[(0,0),(-20,0),(-40,0)]
UP=90
LEFT=180
DOWN=270
RIGHT=0

class Snake:
    def __init__(self):
        self.snake_body = []
        self.create_snake()
        self.head=self.snake_body[0]
    def create_snake(self):
        for pos in positions:
            self.add_segment(pos)

    def add_segment(self,position):
            x=Turtle()
            x.shape("square")
            x.color("yellow")
            x.penup()
            x.goto(position)
            self.snake_body.append(x)
    def extend(self):
        self.add_segment(self.snake_body[-1].position())
    def move(self):
        for segment in range(len(self.snake_body) - 1, 0, -1):
            new_x = self.snake_body[segment - 1].xcor()
            new_y = self.snake_body[segment - 1].ycor()
            self.snake_body[segment].goto(new_x, new_y)
        self.head.forward(20)

    #CREATING METHODS TO MOVE THE SNAKE WITH KEYBOARD BUTTONS
    def move_forward(self):
        if self.head.heading() != DOWN:
            self.snake_body[0].setheading(UP)

    def move_backward(self):
        if self.head.heading() != UP:
            self.snake_body[0].setheading(DOWN)

    def turn_left(self):
        if self.head.heading() != RIGHT:
            self.snake_body[0].setheading(LEFT)


    def turn_right(self):
        if self.head.heading() != LEFT:
            self.snake_body[0].setheading(RIGHT)



    def game_over(self):
       if self.head.xcor() >= 295 or self.head.xcor()<-280 or self.head.ycor() >= 295 or self.head.ycor()<-280:
           return False

       else:
           return True



#SETTLING THE MAIN PART OF THE GAME
snake=Snake()
food=FOOD()
score = Score()
game_is_on=True

#SCREEN SETTINGS
screen = Screen()
screen.bgcolor("black")
screen.title("Snake Game")
screen.setup(width=600,height=600)


#SETTLING THE BUTTONS TO PLAY WITH
screen.listen()
screen.onkey(snake.move_forward,'Up')
screen.onkey(snake.move_backward,"Down")
screen.onkey(snake.turn_left,'Left')
screen.onkey(snake.turn_right,"Right")

#STARTING GAME
while game_is_on:
    #updating the screen
    screen.update()
    time.sleep(0.01)
    snake.move()


    #detect collision with food
    if snake.head.distance(food)<15:
        score.increment()
        food.refresh()
        snake.extend()

    #detect collision with tail
    for segment in snake.snake_body[1:]:
        if snake.head.distance(segment)<10:
            game_is_on = False
            score.game_over()
    #check if the snake is not jumping over the barriers like mexicans
    if snake.game_over()==False:
        score.game_over()
        game_is_on=False

screen.exitonclick()






















