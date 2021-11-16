import pygame

import sys

# intitalizing pygame
pygame.init()

# creating the screen
screen = pygame.display.set_mode((800, 800))

# Title and caption
pygame.display.set_caption("Game")
icon = pygame.image.load("game-controller.png")
pygame.display.set_icon(icon)

#Creating the board
board = pygame.image.load("tic-tac-toe.png")


# game loop
running = True

while running:
    screen.fill((41, 38, 38))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            sys.exit()

    screen.blit(board, (170, 150))

    pygame.display.update()

pygame.quit()
