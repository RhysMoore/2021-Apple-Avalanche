#   a123_apple_1.py
import turtle as trtl

#-----setup-----
apple_image = "apple.gif" # Store the file name of your shape

xcor = 0
ycor = 0

wn = trtl.Screen()
wn.setup(width=1.0, height=1.0)
wn.addshape(apple_image) # Make the screen aware of the new file
wn.bgpic("background.gif")
apple = trtl.Turtle()

#-----functions-----
# given a turtle, set that turtle to be shaped by the image file
def draw_apple(active_apple):
  active_apple.shape(apple_image)
  wn.update()

def draw_an_A(active_apple):
  active_apple.penup()
  active_apple.goto(xcor-20, ycor)
  active_apple.color("white")
  active_apple.write("A", font=("Arial", 55, "bold"))

def drop_apple(active_apple):
  apple.penup()
  apple.goto(xcor, ycor-160)

#-----function calls-----
draw_apple(apple)
draw_an_A(drop_apple, "a")
wn.mainloop()