from turtle import *
setup(900,600,0,0)
#国旗底面
penup()
fillcolor("red")
begin_fill()
pencolor("red")
fd(-150)
pendown()
seth(90)
fd(100)
seth(0)
fd(300)
seth(-90)
fd(200)
seth(180)
fd(300)
seth(90)
fd(100)
end_fill()

#星星1 
penup()
seth(90)
fd(80)
seth(0)
fd(50)
seth(-72)
pendown()
color('yellow')
begin_fill()
for i in range(5):
    fd(58)
    right(144)
end_fill()

#星星2
penup()
seth(0)
fd(60)
seth(-162)
pendown()
color('yellow')
begin_fill()
for i in range(5):
    fd(18)
    right(144)
end_fill()

#星星3

penup()
seth(0)
fd(10)
seth(-90)
fd(25)
seth(90)
pendown()
color('yellow')
begin_fill()
for i in range(5):
    fd(18)
    right(144)
end_fill()

#星星4

penup()
seth(0)
fd(5)
seth(-90)
fd(10)
seth(-75)
pendown()
color('yellow')
begin_fill()
for i in range(5):
    fd(18)
    right(144)
end_fill()

#星星5

penup()
seth(180)
fd(10)
seth(-90)
fd(30)
seth(-162)
pendown()
color('yellow')
begin_fill()
for i in range(5):
    fd(18)
    right(144)
end_fill()

ht()










