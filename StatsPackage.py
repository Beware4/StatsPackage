import turtle

turtle.title("What do you Usually use the Beltline for Stats")
turtle.Screen().bgcolor("grey")
t = turtle.Turtle()
t.width(10)
t.speed(100)
t.hideturtle()

currnumbers = []


def createstat(name, number, color):
  t.penup()

  t.goto(t.position()[0], 0)

  t.color(str(color))

  t.pendown()

  t.write(str(name), move=False, align="Center", font=("Arial", 8, "normal"))

  t.penup()

  t.left(90)
  t.forward(20)

  t.pendown()

  t.forward(int(number) * 10)

  t.penup()

  posx = t.position()[0]

  if not number in currnumbers:
    currnumbers.append(number)
    t.goto(-50, t.position()[1])
    t.color("black")
    t.write(str(number))
    t.goto(posx, t.position()[1])

  t.right(180)
  t.forward(int(number) * 10)

  t.left(90)
  t.forward(90)
