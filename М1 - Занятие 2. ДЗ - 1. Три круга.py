import turtle as t

t.colormode(255)
t.bgcolor(100, 100, 100)

# Перемещение на исходную позицию для отрисовки первого круга.
t.penup()
t.goto(0, 150)
t.pendown()

# Отрисовка первого круга.
t.begin_fill()
t.color(255, 0, 0)
t.circle(60)
t.end_fill()

# Перемещение на позицию для отрисовке второго круга.
t.penup()
t.left(90)
t.fd(-180)
t.right(90)
t.pendown()

# Отрисовка второго круга.
t.begin_fill()
t.color(0, 255, 0)
t.circle(90)
t.end_fill()

# Перемещение на позицию для отрисовки третьего круга.
t.penup()
t.left(-90)
t.right(90)
t.pendown()

# Отрисовка третьего круга.
t.begin_fill()
t.color(0, 0, 255)
t.circle(120)
t.end_fill()

# Завершение программы.
t.hideturtle()
t.done()
