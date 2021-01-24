from turtle import Screen
import time


from turtle import Turtle
import random


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color('green')
        self.speed('fastest')
        self.refresh()

    def refresh(self):
        rand_x = random.randint(-280, 280)
        rand_y = random.randint(-280, 280)
        self.goto(rand_x, rand_y)


STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

color_list = ['#d4955f', '#d7503e', '#2f5e8e', '#e7da5c', '#94425b', '#7aa7c3',
              '#d14659', '#c08c9f', '#27835b', '#4ba460', '#333766',
              '#e9dc0c', '#9fb136', '#23a4c4', '#a4d1bb', '#97cedc', 'white', 'blue', 'red']


class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in STARTING_POSITION:
            self.add_segment(position)

    def add_segment(self, position):
        new_segment = Turtle('circle')
        new_segment.color(random.choice(color_list))
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)
        # self.segments[0].fd(20)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)


ALIGNMENT = 'center'
FONT = ('Courier', 20, 'normal')


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.color('white')
        self.goto(0, 265)
        self.hideturtle()
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over.", align='center', font=FONT)

    def update_scoreboard(self):
        self.write(f"Score: {self.score}", align=ALIGNMENT,
                   font=(FONT))

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('Windows Snake Game')
# the tracer function will not show the animation
screen.tracer(0)

snake = Snake()                 # there is no need to write snake.create_snake()
food = Food()
scoreboard = ScoreBoard()

screen.listen()
screen.onkey(snake.up, 'Up')
screen.onkey(snake.down, 'Down')
screen.onkey(snake.right, 'Right')
screen.onkey(snake.left, 'Left')

game_is_on = True
while game_is_on:
    screen.update()             # the update function shows the animation
    time.sleep(0.1)             # making the snake's tail to head of snake
    snake.move()

    # detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    wall_collision = [
        snake.head.xcor() > 290,
        snake.head.xcor() < -290,
        snake.head.ycor() > 290,
        snake.head.ycor() < -290,
    ]
    if any(wall_collision):
        game_is_on = False
        scoreboard.game_over()

    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()


screen.exitonclick()
