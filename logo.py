import turtle

screen = turtle.Screen()
screen.setup(800, 600)
screen.bgcolor("gray")

pen = turtle.Turtle()
pen.hideturtle()
pen.penup()
pen.color("blue")

pen.goto(0, 0)
pen.write(
    "Pachicom",
    align="center",
    font=("Times New Roman", 100, "bold")
)

pen.goto(0, -120)
pen.write(
    "🪿",
    align="center",
    font=("Segoe UI Emoji", 80, "normal")
)

turtle.done()