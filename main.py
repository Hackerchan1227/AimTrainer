
import turtle as trtl
import random as rand
 
#-----game configuration----
scolor = "red"
s = "circle"
ssize = 1
score = 0
font_setup = ("Times",20,"normal")
timer = 5
counter_interval = 1000
timer_up = False
 
#-----initialize turtle-----
sturt = trtl.Turtle()
sturt.speed(0)
sturt.shape(s)
sturt.color(scolor)
sturt.shapesize(ssize)
sturt.penup()
score_writer = trtl.Turtle()
score_writer.hideturtle()
score_writer.pu()
score_writer.goto(-180,140)
 
counter = trtl.Turtle()
#-----game functions--------
def update_score():
  global score
  score+=1
  score_writer.clear()
  score_writer.write(score,font=font_setup)
 
def countdown():
  global timer, timer_up
  counter.clear()
  if timer <= 0:
    counter.penup()
    counter.goto(-50,50)
    counter.hideturtle()
    counter.write("Time's Up", font=font_setup)
    timer_up = True
  else:
    counter.penup()
    counter.goto(-50,50)
    counter.hideturtle()
    counter.write("Timer: " + str(timer), font=font_setup)
    timer -= 1
    counter.getscreen().ontimer(countdown, counter_interval)
 
def s_clicked(x, y):
  change_position()
  update_score()
 
def change_position():
  new_xpos = rand.randint(-200, 200)
  new_ypos = rand.randint(-150, 150)
  sturt.hideturtle()
  sturt.goto(new_xpos, new_ypos)
  sturt.showturtle()
 
 
#-----events----------------
sturt.penup()
sturt.onclick(s_clicked)
 
 
wn = trtl.Screen()
wn.ontimer(countdown, counter_interval)
wn.mainloop()
