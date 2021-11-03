import turtle as trtl
import random as rand

trtl.speed(0)
wn = trtl.Screen()
wn.bgcolor("black")
#-------------------maze and turtle config variables-----------------
screen_h = 400
screen_w = 420
startx = 0
starty = 0
turtle_scale = 1.5

#---------------------------GHOST COMMANDS---------------------------
#------ red ghost commands

#----- init screen

trtl.setup(width=screen_w, height=screen_h)
HuTao_image = "HuTao.gif"
trtl.addshape(HuTao_image)

#----- init ghost
hutao = trtl.Turtle(shape=HuTao_image)
hutao.hideturtle()
hutao.pencolor("red")
hutao.penup()
hutao.setheading(90)
hutao.turtlesize(turtle_scale, turtle_scale)
hutao.goto(0, 0)
hutao.speed(2)
hutao.showturtle()

#-----game functions--------
 
 
def change_position():
  new_xpos = rand.randint(-200, 200)
  new_ypos = rand.randint(-150, 150)
  hutao.hideturtle()
  hutao.goto(new_xpos, new_ypos)
  hutao.showturtle()
 
def s_clicked(x, y):
  change_position()
 
#-----events----------------
hutao.penup()
hutao.onclick(s_clicked)
 
 
wn = trtl.Screen()
wn.mainloop()
