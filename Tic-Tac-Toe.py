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




# game loop
running = True

while running:
    screen.fill((41, 38, 38))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            sys.exit()

    # Draw horizontal lines
    pygame.draw.line(screen, "Red", (150, 330), (650, 330), 20)
    pygame.draw.line(screen, "Red", (150, 500), (650, 500), 20)
    # Draw Vertical lines
    pygame.draw.line(screen, "Red", (500, 200), (500, 630), 20)
    pygame.draw.line(screen, "Red", (300, 200), (300, 630), 20)



    pygame.display.update()

pygame.quit()
