import pygame
from pygame.locals import *
import sys
from frog import Frog

pygame.init()

# Screen dimensions
SCREEN_WIDTH = 750
SCREEN_HEIGHT = 850
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Frogger")

# Image variables
background = pygame.image.load('img/background.png')
fitted_background = pygame.transform.scale(background, (SCREEN_WIDTH, SCREEN_HEIGHT))
frog = Frog(SCREEN_WIDTH // 2, (SCREEN_HEIGHT // 2) + 400)


# Main Game Loop
running = True
while running:

  # render image variables
  screen.blit(fitted_background, (0,0))
  screen.blit(frog.image, frog.rect)

  # Get keys pressed
  keys = pygame.key.get_pressed()

  # Move the frog
  if keys[pygame.K_UP]:
    frog.update_direction("up")
    frog.move(0, -5)
  elif keys[pygame.K_DOWN]:
    frog.update_direction("down")
    frog.move(0, 5)
  elif keys[pygame.K_LEFT]:
    frog.update_direction("left")
    frog.move(-5, 0)
  elif keys[pygame.K_RIGHT]:
    frog.update_direction("right")
    frog.move(5, 0)

  # exiting the game
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
      
  
  pygame.display.update()

pygame.quit()