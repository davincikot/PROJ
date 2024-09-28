import turtle as t

t.colormode(255)
t.bgcolor(100, 100, 100)

# Перемещение на исходную позицию для отрисовки прямоугольника.
t.penup()
t.goto(-50, 200)
t.pendown()

# Отрисовка прямоугольника.
t.begin_fill()
t.color(255, 0, 0)
t.fd(100)
t.right(90)
t.fd(50)
t.right(90)
t.fd(100)
t.right(90)
t.fd(50)
t.end_fill()

# Перемещение на позицию для отрисовки ромба.
t.penup()
t.goto(0, 100)
t.right(120)
t.pendown()

# Отрисовка ромба.
t.begin_fill()
t.color(0, 255, 0)
t.fd(100)
t.right(120)
t.fd(100)
t.right(60)
t.fd(100)
t.right(120)
t.fd(100)
t.end_fill()

# Перемещение на позицию для отрисовки трапеции.
t.penup()
t.goto(90, -100)
t.right(210)
t.pendown()

# Отрисовка трапеции.
t.begin_fill()
t.color(0, 0, 255)
t.fd(180)
t.right(120)
t.fd(60)
t.right(60)
t.fd(120)
t.right(60)
t.fd(60)
t.end_fill()

# Завершение программы.
t.hideturtle()
t.done()
