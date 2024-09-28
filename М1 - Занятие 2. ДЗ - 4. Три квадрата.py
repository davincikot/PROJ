import turtle as t

t.colormode(255)
t.bgcolor(100, 100, 100)
t.color(0, 255, 0)
t.pensize(3)

# Перемещение на исходную позицию для отрисовки первого квадрата.
t.penup()
t.goto(-75, 100)
t.pendown()

# Отрисовка первого квадрата.
for i in range(4):
    t.fd(30)
    t.left(90)

# Перемещение на исходную позицию для отрисовки второго квадрата.
t.penup()
t.fd(60)
t.pendown()

# Отрисовка второго квадрата.
for i in range(4):
    t.fd(30)
    t.left(90)

# Перемещение на исходную позицию для отрисовки третьего квадрата.
t.penup()
t.fd(60)
t.pendown()

# Отрисовка третьего квадрата.
for i in range(4):
    t.fd(30)
    t.left(90)

# Завершение программы.
t.hideturtle()
t.done()
