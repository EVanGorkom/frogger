import pygame
from pygame.locals import *
from frog import Frog
from car1 import Car1
from car2 import Car2
from truck import Truck
import random

pygame.init()

# Screen dimensions
SCREEN_WIDTH = 700
SCREEN_HEIGHT = 800
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Frogger")

# Game variables
game_over = False
variance = random.randint(0, 500)
car1_frequency = 1500
last_car1 = pygame.time.get_ticks() - car1_frequency
car2_frequency = 1000
last_car2 = pygame.time.get_ticks() - car2_frequency
truck_frequency = 2000
last_truck = pygame.time.get_ticks() - truck_frequency

# Image variables
background = pygame.image.load('img/background.png')
fitted_background = pygame.transform.scale(background, (SCREEN_WIDTH, SCREEN_HEIGHT))

# Object starting positions
frog = Frog(SCREEN_WIDTH // 2, (SCREEN_HEIGHT // 2) + 370, SCREEN_WIDTH, SCREEN_HEIGHT)
# car1 = Car1(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)

# Groups
car1_group = pygame.sprite.Group()
car2_group = pygame.sprite.Group()
truck_group = pygame.sprite.Group()

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

  time_now = pygame.time.get_ticks()
  if time_now - last_car1 > car1_frequency:
    last_car1 = time_now
    car1 = Car1(SCREEN_WIDTH, 682) # position on the screen
    car_1 = Car1(SCREEN_WIDTH, 497) # position on the screen
    car1_group.add(car1, car_1)
  elif time_now - last_car2 > car2_frequency:
    last_car2 = time_now
    car2 = Car2(-100, 437) # position on the screen
    car2_group.add(car2)
  elif time_now - last_truck > truck_frequency:
    last_truck = time_now
    truck = Truck(-160, 560) # position on the screen
    truck_group.add(truck)

  # Update cars
  car1_group.update()
  car2_group.update()
  truck_group.update()

  # render image variables
  screen.blit(fitted_background, (0,0))
  screen.blit(frog.image, frog.rect)
  car1_group.draw(screen)
  car2_group.draw(screen)
  truck_group.draw(screen)

  pygame.display.update()

pygame.quit()