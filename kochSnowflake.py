import turtle


window = turtle.Screen()
t = turtle.Turtle()
t.speed = 0
t.hideturtle()

t.pu()
t.goto(0,200)
t.pd()
t.color('green')

def koch (t, size):
	if size <= 10:
		t.forward(size)
	else:
		for angle in [60,-120,60,0]:
			koch(t, size / 3)
			t.left(angle)

def snowflake(t,size):
	for i in range(3):
		koch(t, size)
		t.right(120)

def triforce(t,size):
	t.setheading(-60)
	# t.right(60)
	if size <= 25:
		for i in range(3):
			t.forward(size)
			t.right(120)
		t.forward(size)
	else:
		newsize = size / 2
		triforce(t, newsize)
		topRight = t.position()
		triforce(t, newsize)
		t.setheading(180)
		t.forward(newsize)
		bottom = t.position()
		t.setheading(120)
		t.forward(newsize)
		topLeft = t.position()
		triforce(t, newsize)

		t.pu()
		t.goto(topRight)
		t.setheading(-60)
		t.forward(newsize)
		t.pd()



triforce(t,300)
# snowflake(t, 300)
window.exitonclick()
