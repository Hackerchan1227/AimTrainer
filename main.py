
import turtle as trtl
import random as rand
from turtle import Screen, Turtle

#-----game configuration----
wn = trtl.Screen()
wn.bgpic("Wuwan Hill.png")
smug = "HuTao.webp-2.gif"
screen = Screen()
screen.addshape(smug)
HuTao = Turtle(smug)
score = 0
font_setup = ("Times",20,"normal")
timer = 5
counter_interval = 1000
timer_up = False
 
#-----initialize turtle-----
HuTao.speed(0)
HuTao.penup()
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
  score_writer.color("Red")
  score_writer.write(score,font=font_setup)
  HuTao.clear()
  HuTao.color("White")
  HuTao.write("Yahooo!",font=font_setup)

counter.color("White")
def countdown():
  global timer, timer_up
  counter.clear()
  if timer <= 0:
    counter.penup()
    counter.goto(150,150)
    counter.hideturtle()
    counter.write("Time's Up", font=font_setup)
    counter.goto(120,120)
    counter.write("You lost the 50/50 lol.", font=font_setup)
    timer_up = True
    HuTao.hideturtle()
  else:
    counter.penup()
    counter.goto(150,150)
    counter.hideturtle()
    counter.write("Timer: " + str(timer), font=font_setup)
    timer -= 1
    counter.getscreen().ontimer(countdown, counter_interval)
 
def s_clicked(x, y):
  change_position()
  update_score()
  print("Yahoooo")
 
def change_position():
  new_xpos = rand.randint(-150, 150)
  new_ypos = rand.randint(-150, 150)
  HuTao.hideturtle()
  HuTao.goto(new_xpos, new_ypos)
  HuTao.showturtle()
 
 
#-----events----------------
HuTao.penup()
counter.hideturtle()
countdown()
HuTao.onclick(s_clicked)
wn = trtl.Screen()
wn.mainloop()
