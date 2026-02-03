import random
from turtle import Turtle, Screen

screen =Screen()
screen.setup(width=500,height=400)
user_input = screen.textinput(title="Make your bet", prompt="Who will win the race")
print(user_input)
colors = ['red','orange','yellow','green','blue','purple']

bet = False
all_turtles =[]
x_axis = -230
y_axis = -90
for i in range(6):
    tim =Turtle(shape="turtle")
    tim.color(colors[i])
    tim.penup()
    tim.goto(x=x_axis,y=y_axis)
    all_turtles.append(tim)
    y_axis+=40

if user_input:
    bet = True
while bet:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            winner = turtle.color()[0]
            print(f"The winner is {winner}")
            if user_input.lower() == winner:
                print("You won")
            else:
                print("You Lost")
            bet = False
        turtle.forward(random.randint(1,10))


screen.exitonclick()
