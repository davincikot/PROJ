import turtle as t

t.ht()
t.pensize(5)
t.colormode(255)
t.speed(0)

# Круги.
t.penup()
t.goto(0, 200)
t.pendown()
for a in range(40, 0, -10):
  for _ in range(6):
    t.color(255, 165, a * 6)
    t.fillcolor(162, a * 6, 255)
    t.begin_fill()
    t.circle(a)
    t.end_fill()
    t.rt(60)

# Квадраты.
sq = 4
t.penup()
t.goto(0, 0)
t.left(45)
t.pendown()
for a in range(40, 0, -10):
  for _ in range(6):
    t.color(255, 165, a * 6)
    t.fillcolor(162, a * 6, 255)
    t.begin_fill()
    for _ in range(sq):
     t.fd(a*1.5)
     t.left(360 / sq)
    t.end_fill()
    t.rt(60)

# Треугольники.
tr  = 3
t.penup()
t.goto(0, -200)
t.left(-45)
t.pendown()
for a in range(40, 0, -10):
  for _ in range(6):
    t.color(255, 165, a * 6)
    t.fillcolor(162, a * 6, 255)
    t.begin_fill()
    for _ in range(tr):
     t.fd(a*2)
     t.left(360 / tr)
    t.end_fill()
    t.rt(60)

t.done()
