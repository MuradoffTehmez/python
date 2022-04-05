import turtle
pp=turtle.Turtle()
p=turtle.getscreen()
p.bgcolor('silver')
for x in range(300):
    import random
    color=['red','green','orange','blue','yellow' ,'violet','indigo','gold','brown']
    pcolor=random.choice(color)
    pp.speed(0)
    pp.color(pcolor)
    pp.pensize(2)
    pp.left(90)
    pp.circle(60-x)
turtle.mainloop()