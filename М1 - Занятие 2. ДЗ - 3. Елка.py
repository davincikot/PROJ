import turtle as t

t.colormode(255)
t.bgcolor(100, 100, 100)

# Перемещение на исходную позицию для отрисовки первого трреугольника.
t.penup()
t.goto(-60, 100)
t.pendown()

# Отрисовка первого треугольника.
t.begin_fill()
t.color(0, 150, 0)
for i in range(3):
    t.fd(120)
    t.left(120)
t.end_fill()

# Перемещение на исходную позицию для отрисовки второго трреугольника.
t.penup()
t.goto(0, 150)
t.left(-120)
t.pendown()

# Отрисовка второго треугольника.
t.begin_fill()
t.color(0, 150, 0)
for i in range(3):
    t.fd(150)
    t.left(120)
t.end_fill()

# Перемещение на исходную позицию для отрисовки третьего трреугольника.
t.penup()
t.goto(0,90)
t.pendown()

# Отрисовка третьего треугольника.
t.begin_fill()
t.color(0, 150, 0)
for i in range(3):
    t.fd(210)
    t.left(120)
t.end_fill()

# Завершение программы.
t.hideturtle()
t.done()
