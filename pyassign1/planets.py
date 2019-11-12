#!/usr/bin/env python3

"""planets.py: A dimulation of planets' motion.

__author__ = "Fujinyu"
__pkuid__  = "1900011813"
__email__  = "Fyun@pku.edu.cn"
"""


import turtle

wn = turtle.Screen()
wn.bgcolor("black")
wn.screensize(800, 800)

r = turtle.Turtle()
r.color("red")
r.shape("circle")
r.shapesize(2)
r.home

s = turtle.Turtle()
s.shape("circle")
s.shapesize(1)
s.speed(11)
s.penup
s.goto(0, -50)
s.pendown
s.color("white")

j = turtle.Turtle()
j.shape("circle")
j.shapesize(1.2)
j.speed(11)
j.penup
j.goto(0, -100)
j.pendown
j.color("yellow")

d = turtle.Turtle()
d.shape("circle")
d.shapesize(1.3)
d.speed(11)
d.penup
d.goto(0, -150)
d.pendown
d.color("sea green")

h = turtle.Turtle()
h.shape("circle")
h.shapesize(1.2)
h.speed(11)
h.penup
h.goto(0, -200)
h.pendown
h.color("grey")

m = turtle.Turtle()
m.shape("circle")
m.shapesize(2.2)
m.speed(11)
m.penup
m.goto(0, -250)
m.pendown
m.color("orange")

t = turtle.Turtle()
t.shape("circle")
t.shapesize(1.8)
t.speed(11)
t.penup
t.goto(0, -310)
t.pendown
t.color("brown")

s.circle(50, 360)
j.circle(100, 360)
d.circle(150, 360)
h.circle(200, 360)
m.circle(250, 360)
t.circle(310, 360)

n = int(turtle.numinput("planets", "speed(Please give a integer between 1 \
                                          and 15)", 7, minval=1, maxval=15))

for i in range(99999999):
    s.circle(50, 4.17*n)
    j.circle(100, 1.61*n)
    d.circle(150, 1*n)
    h.circle(200, 0.53*n)
    m.circle(250, 0.085*n)
    t.circle(310, 0.034*n)

# Here we don't need to test this program, so main module has been deleted.
