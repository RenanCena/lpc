import pygame

pygame.init()

# criação da janela
width = 893
height = 1000
size = (width, height)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Breakout Game")
# controlar o tempo
clock = pygame.time.Clock()
fps_rate = 68

# cores utilizadas (rgb)
white = (255, 255, 255)
grey = (212, 218, 212)
black = (0, 0, 0)
blue = (0, 97, 148)

red = (162, 8, 8)
orange = (183, 119, 0)
green = (0, 127, 33)
yellow = (197, 199, 37)

# tamanho das raquetes
paddle_width = 54
paddle_height = 20

# classe para armazenar objetos
all_spites_list = pygame.sprite.Group()

# criacao dos bricks (tijolos)
brick_width = 55
brick_height  16
x_gap = 7
y_gap = 5
wall_width = 16

def main()
    clock.tick(fps_rate)

    run = True
    while run:
        for event in pygame.event.get()
            if event.type == pygame.QUIT
                rub - False

            all_spites_list.update()
