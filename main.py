import pygame
from pygame.locals import *
from frog import Frog

pygame.init()

# Screen dimensions
SCREEN_WIDTH = 700
SCREEN_HEIGHT = 800
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Frogger")

# Image variables
background = pygame.image.load('img/background.png')
fitted_background = pygame.transform.scale(background, (SCREEN_WIDTH, SCREEN_HEIGHT))
frog = Frog(SCREEN_WIDTH // 2, (SCREEN_HEIGHT // 2) + 370, SCREEN_WIDTH, SCREEN_HEIGHT)

# Button booleans
key_pressed = {
  pygame.K_UP: False,
  pygame.K_DOWN: False,
  pygame.K_LEFT: False,
  pygame.K_RIGHT: False
}

# Main Game Loop
running = True
while running:

  # exiting the game
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
    # Button limiters
    elif event.type == pygame.KEYDOWN:
      if event.key in key_pressed:
        key_pressed[event.key] = True
        # Move the frog
        if key_pressed[pygame.K_UP]:
          frog.update_direction("up")
          frog.move(0, -62)
        elif key_pressed[pygame.K_DOWN]:
          frog.update_direction("down")
          frog.move(0, 62)
        elif key_pressed[pygame.K_LEFT]:
          frog.update_direction("left")
          frog.move(-62, 0)
        elif key_pressed[pygame.K_RIGHT]:
          frog.update_direction("right")
          frog.move(62, 0)
    elif event.type == pygame.KEYUP:
      if event.key in key_pressed:
        key_pressed[event.key] = False

  # render image variables
  screen.blit(fitted_background, (0,0))
  screen.blit(frog.image, frog.rect)

  pygame.display.update()

pygame.quit()