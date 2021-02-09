import turtle
import random


turtles = []


def setup():
    global turtles
    startline = -620
    screen = turtle.Screen()
    screen.setup(1290, 720)
    screen.bgpic('pavement.gif')
    turtle_ycor = [-40, -20, 0, 20, 40]
    turtle_color = ['blue', 'red', 'purple', 'brown', 'green']

    for i in range(0, len(turtle_ycor)):
        new_turtle = turtle.Turtle()
        new_turtle.shape('turtle')
        new_turtle.color(turtle_color[i])
        new_turtle.penup()
        new_turtle.setpos(startline, turtle_ycor[i])
        new_turtle.pendown()
        turtles.append(new_turtle)


def race():
    global turtles
    winner = False
    finishline = 590

    while not winner:
        for curent_turtle in turtles:
            curent_turtle.speed(300)
            move = random.randint(0, 5)
            curent_turtle.forward(move)

            xcor = curent_turtle.xcor()
            if xcor >= finishline:
                winner = True
                winner_color = curent_turtle.color()
                print(f'Победитель - {winner_color[0]}')


setup()
race()
# turtle.mainloop()
