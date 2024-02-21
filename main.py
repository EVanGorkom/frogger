import pygame
from pygame.locals import *

pygame.init()

# Screen dimensions
SCREEN_WIDTH = 750
SCREEN_HEIGHT = 850

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Frogger")

background = pygame.image.load('img/background.png')
fitted_background = pygame.transform.scale(background, (SCREEN_WIDTH, SCREEN_HEIGHT))


# Main Game Loop
run = True
while run:

  # render the background
  screen.blit(fitted_background, (0,0))


  # exiting the game
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      run = False
  
  pygame.display.update()

pygame.quit()