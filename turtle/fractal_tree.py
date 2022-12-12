from turtle import *

speed("fastest")

rt(-90)

# O angulo dos Ramos
angle = 30


# Função de tamanho com level
def y(sz, level):
    if level > 0:
        colormode(255)

        # Cor por nivel
        pencolor(50, 235 // level, 0)

        fd(sz)

        rt(angle)

        # Recursivo para ramos da direita
        y(0.8 * sz, level - 1)
        pencolor(0, 255 // level, 0)
        lt(2 * angle)

        # Recursivo para ramos da esquerda
        y(0.8 * sz, level - 1)
        pencolor(0, 255 // level, 0)

        rt(angle)
        fd(-sz)


y(80, 10)
