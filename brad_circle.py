import turtle

def open_window():
    window = turtle.getscreen()
    window.bgcolor("red")

def close_window():
    window = turtle.getscreen()
    window.exitonclick()

def draw_square():
    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.color("yellow")
    brad.speed(20)

    count = 0
    while count < 46:
      box_side = 0
      while box_side < 4:
        brad.forward(100)
        brad.right(90)
        box_side = box_side+1
      brad.right(8)
      count = count+1



open_window()
draw_square()
close_window()
