import turtle
import math


def fractal_fibo(n):
    # variaveis para os quadrados e a espiral
    spiral_a = 0
    spiral_b = 1
    square_a = spiral_a
    square_b = spiral_b

    # Cor das linhas dos quadrados
    x.pencolor("green")

    # Primeiro quadrado
    x.forward(square_b * factor)
    x.left(90)
    x.forward(square_b * factor)
    x.left(90)
    x.forward(square_b * factor)
    x.left(90)
    x.forward(square_b * factor)

    # Seguindo sequencia para os quadrados
    temp = square_b
    square_b = square_b + square_a
    square_a = temp

    # Quadrados restantes
    for i in range(1, n):
        x.backward(square_a * factor)
        x.right(90)
        x.forward(square_b * factor)
        x.left(90)
        x.forward(square_b * factor)
        x.left(90)
        x.forward(square_b * factor)

        # Seguindo sequencia para os quadrados
        temp = square_b
        square_b = square_b + square_a
        square_a = temp

    # Pincel para o incio da spiral
    x.penup()
    x.setposition(factor, 0)
    x.seth(0)
    x.pendown()

    # Cor da espiral
    x.pencolor("red")

    # Desenho da fibonacci
    # Printar fibonacci no terminal
    x.left(90)
    for i in range(n):
        print(spiral_b)
        fdwd = math.pi * spiral_b * factor / 2
        fdwd /= 90

        for j in range(90):
            x.forward(fdwd)
            x.left(1)

        # Seguindo com a  fibonacci
        temp = spiral_a
        spiral_a = spiral_b
        spiral_b = temp + spiral_b


factor = 5  # Fator - escala dos quadrados

# Entrada de quantidade de numeros da fibonacci
quant_fib = int(input('Digite o número para a interação (deve ser > 1): '))

# Checar se o numero recebido é valido
if quant_fib > 0:
    print("Fibonacci series for", quant_fib, "elements :")
    x = turtle.Turtle()
    x.speed(100)
    fractal_fibo(quant_fib)
    turtle.done()
else:
    print("Number of iterations must be > 0")
