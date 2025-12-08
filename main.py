from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import ScoreBoard

screen = Screen()
screen.setup(600, 600)
screen.bgcolor("Black")
screen.title("My_SNAKEGAME")
screen.tracer(0)

snake = Snake()
food = Food()
score = ScoreBoard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")




game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)

    snake.move()
    #detect food collusion
    if snake.head.distance(food) < 15:
        food.refresh()
        score.increase_score()
        snake.extend()

    #dectect wall collusion
    if snake.head.xcor()> 300 or snake.head.xcor()< -300 or snake.head.ycor()>300 or snake.head.ycor()< -300 :
        game_on = False
        score.gameover()

    #dectect tail collusion
    for segment in snake.segment[1:]:
        if snake.head.distance(segment)< 10:
            game_on = False
            score.gameover()




screen.exitonclick()