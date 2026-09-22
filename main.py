from turtle import Screen
import time
import snakey
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("Snake!")
screen.tracer(0)

snake = snakey.Snake()
food = Food()
scoreboard = Scoreboard()

def reset():
    global game_is_on
    game_is_on = True
    snake.reset_self()
    scoreboard.reset()
    loop()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
screen.onkey(snake.up, "w")
screen.onkey(snake.down, "s")
screen.onkey(snake.left, "a")
screen.onkey(snake.right, "d")

game_is_on = True
def loop():
    global game_is_on
    while game_is_on:
        screen.update()
        time.sleep(0.07)
        snake.move()

        if snake.head.distance(food) < 15:
            food.refresh()
            scoreboard.update_score()
            snake.extend()

        if snake.head.xcor() > 300 or snake.head.xcor() < -300 or snake.head.ycor() > 300 or snake.head.ycor() < -300:
            game_is_on = False
            scoreboard.game_over()

        for segment in snake.segments[1:]:
            if snake.head.distance(segment) < 10:
                game_is_on = False
                scoreboard.game_over()
    if game_is_on == False:
        screen.onkey(reset, "space")
loop()

screen.exitonclick()
