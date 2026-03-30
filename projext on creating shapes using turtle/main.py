import turtle

# creating canvas
turtle.Screen().bgcolor("Orange")

sc = turtle.Screen()
sc.setup(400, 300)

turtle.title("Welcome to Turtle Window")

# turtle object creation
board = turtle.Turtle()

# creating a hexahon
for i in range(6):
	board.forward(50)
	board.left(60)
	i = i+1

# creating a equilateral triangle
for i in range(3):
    board.forward(50)
    board.left(120)
    i = i+1

#creating a rectangle
for i in range(2):
    board.forward(100)
    board.left(90)
    board.forward(50)
    board.left(90)
    i = i+1