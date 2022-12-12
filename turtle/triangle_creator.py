import turtle

wn = turtle.Screen()

tess = turtle.Turtle()


# Função para criação dos triangulos
def triangle(x, y):
    tess.penup()
    # Posição do mouse
    tess.goto(x, y)
    tess.pendown()

    # Desenhando o triangulo onde ocorreu o click
    for i in range(3):
        tess.forward(100)
        tess.left(120)
        tess.forward(100)


# Recebendo as cordenadas do mouse
turtle.onscreenclick(triangle, 1)
turtle.listen()

turtle.done()
