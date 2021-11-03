#-----import statements-----
import turtle as trtl
import random as rand
 
#-----game configuration----
wn = trtl.Screen()
wn.setup(width=997, height=700)
scolor = "red"
wn.addshape("HuTaoSmug.gif")
s = "circle"
ssize = 2
 
#-----initialize turtle-----
sturt = trtl.Turtle()
sturt.speed(0)
sturt.shape(s)
sturt.color(scolor)
sturt.shapesize(ssize)
 
#-----game functions--------
 
 
def change_position():
  new_xpos = rand.randint(-200, 200)
  new_ypos = rand.randint(-150, 150)
  sturt.hideturtle()
  sturt.goto(new_xpos, new_ypos)
  sturt.showturtle()
 
def s_clicked(x, y):
  change_position()
 
#-----events----------------
sturt.penup()
sturt.onclick(s_clicked)
 
 
wn = trtl.Screen()
wn.mainloop()
