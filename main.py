
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

SCREEN_SIZE = 600
BOUNDARY = 280
FOOD_COLLISION_DISTANCE = 15
TAIL_COLLISION_DISTANCE = 10
FRAME_DELAY = 0.1


def main():
    screen = Screen()
    screen.setup(width=SCREEN_SIZE, height=SCREEN_SIZE)
    screen.bgcolor("black")
    screen.title("Snake Game")
    screen.tracer(0)

    snake = Snake()
    food = Food()
    scoreboard = Scoreboard()

    screen.listen()
    screen.onkey(snake.up, "Up")
    screen.onkey(snake.down, "Down")
    screen.onkey(snake.left, "Left")
    screen.onkey(snake.right, "Right")

    game_is_on = True
    while game_is_on:
        screen.update()
        time.sleep(FRAME_DELAY)
        snake.move()

        if snake.head.distance(food) < FOOD_COLLISION_DISTANCE:
            food.refresh()
            snake.extend()
            scoreboard.increase_score()

        if (
            snake.head.xcor() > BOUNDARY
            or snake.head.xcor() < -BOUNDARY
            or snake.head.ycor() > BOUNDARY
            or snake.head.ycor() < -BOUNDARY
        ):
            scoreboard.reset()
            snake.reset()

        for segment in snake.segments[1:]:
            if snake.head.distance(segment) < TAIL_COLLISION_DISTANCE:
                scoreboard.reset()
                snake.reset()
                break

    screen.exitonclick()


if __name__ == "__main__":
    main()


