import turtle
 
myTurtle = turtle.Turtle()

def draw_head():
    myTurtle.penup()
    myTurtle.setposition(0,30)
    myTurtle.pendown()
    myTurtle.circle(50)

def draw_body():
    myTurtle.penup()
    myTurtle.setposition(0,-129)
    myTurtle.pendown()
    myTurtle.circle(80)

def draw_butt():
    myTurtle.penup()
    myTurtle.setposition(0,-370)
    myTurtle.pendown()
    myTurtle.circle(120)

def draw_arm_1():
    point1 = (79,-30)
    point2 = (180,-35)
    myTurtle.penup()
    myTurtle.goto(point1)
    myTurtle.pendown()
    myTurtle.goto(point2)

def draw_arm_2():
    point1 = (-79,-30)
    point2 = (-180,-35)
    myTurtle.penup()
    myTurtle.goto(point1)
    myTurtle.pendown()
    myTurtle.goto(point2)

my_functions = [
    draw_head, 
    draw_body, 
    draw_butt, 
    draw_arm_1, 
    draw_arm_2
]

#for func in my_functions:
    #func()



turtle.getscreen()._root.mainloop()


