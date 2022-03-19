from turtle import Screen
from food import Food
from scoreboard import Scoreboard
from snake import Snake
import time

screen = Screen()

screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.update()
time.sleep(1)

screen.listen()
screen.onkey(key="Up", fun=lambda: snake.change_direction(90))
screen.onkey(key="Down", fun=lambda: snake.change_direction(270))
screen.onkey(key="Left", fun=lambda: snake.change_direction(180))
screen.onkey(key="Right", fun=lambda: snake.change_direction(0))

game_on = True

initial_interval = 0.12
max_speed = 0.05
speed_up_flag = False
threshold_score = 5

while game_on:
    screen.update()
    time.sleep(initial_interval)
    snake.move()

    # Snake eating the food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increment_score()
        if scoreboard.score % threshold_score == 0:
            speed_up_flag = True

    # Checking for snake head hitting the boundary
    if snake.head.xcor() > 280 or snake.head.ycor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() < -280:
        game_on = False
        scoreboard.game_over()

    # Detecting collisions with the tail
    for seg in snake.snake_body[1:]:
        if snake.head.distance(seg) < 10:
            game_on = False
            scoreboard.game_over()

    # Increase the snake speed after reaching each threshold
    if speed_up_flag and scoreboard.score % threshold_score == 0 and scoreboard.score > 0 and initial_interval >= max_speed:
        initial_interval -= 0.01
        speed_up_flag = False


screen.exitonclick()
