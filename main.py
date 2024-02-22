import pygame
from pygame.locals import *
from lib.frog import Frog
from lib.car1 import Car1
from lib.car2 import Car2
from lib.truck import Truck
from lib.truck_rev import TruckRev
from lib.log1 import Log1
from lib.log2 import Log2
from lib.log3 import Log3
from lib.turtle1 import Turtle1
from lib.turtle2 import Turtle2
import random

pygame.init()

# Screen dimensions
SCREEN_WIDTH = 700
SCREEN_HEIGHT = 800
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Frogger")

# Game variables
lives = 3
game_over = False
# variance = random.randint(0, 500)
car1_frequency = 1500
last_car1 = pygame.time.get_ticks() - car1_frequency
car2_frequency = 1000
last_car2 = pygame.time.get_ticks() - car2_frequency
truck_frequency = 2000
last_truck = pygame.time.get_ticks() - truck_frequency
truck_rev_frequency = 4000
last_truck_rev = pygame.time.get_ticks() - truck_rev_frequency
log1_frequency = 2250
last_log1 = pygame.time.get_ticks() - log1_frequency
log2_frequency = 4000
last_log2 = pygame.time.get_ticks() - log2_frequency
log3_frequency = 4000
last_log3 = pygame.time.get_ticks() - log3_frequency
turtle1_frequency = 1500
last_turtle1 = pygame.time.get_ticks() - turtle1_frequency
turtle2_frequency = 1500
last_turtle2 = pygame.time.get_ticks() - turtle2_frequency

# Image variables
background = pygame.image.load('img/background.png')
fitted_background = pygame.transform.scale(background, (SCREEN_WIDTH, SCREEN_HEIGHT))

# Object starting positions
frog = Frog(SCREEN_WIDTH // 2, (SCREEN_HEIGHT // 2) + 370, SCREEN_WIDTH, SCREEN_HEIGHT)

# Groups
frog_group = pygame.sprite.GroupSingle()
frog_group.add(frog)
car1_group = pygame.sprite.Group()
car2_group = pygame.sprite.Group()
truck_group = pygame.sprite.Group()
truck_rev_group = pygame.sprite.Group()
log1_group = pygame.sprite.Group()
log2_group = pygame.sprite.Group()
log3_group = pygame.sprite.Group()
turtle1_group = pygame.sprite.Group()
turtle2_group = pygame.sprite.Group()

# Button booleans
key_pressed = {
  pygame.K_UP: False,
  pygame.K_DOWN: False,
  pygame.K_LEFT: False,
  pygame.K_RIGHT: False
}



### Main Game Loop
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

  # Collision
  if pygame.sprite.groupcollide(frog_group, car1_group, True, False):
    lives -= 1
    frog = Frog(SCREEN_WIDTH // 2, (SCREEN_HEIGHT // 2) + 370, SCREEN_WIDTH, SCREEN_HEIGHT)
    frog_group.add(frog)
    if lives == 0:
      game_over = True
      lives = 3

  if pygame.sprite.groupcollide(frog_group, car2_group, True, False):
    lives -= 1
    frog = Frog(SCREEN_WIDTH // 2, (SCREEN_HEIGHT // 2) + 370, SCREEN_WIDTH, SCREEN_HEIGHT)
    frog_group.add(frog)
    if lives == 0:
      game_over = True
      lives = 3

  if pygame.sprite.groupcollide(frog_group, truck_group, True, False):
    lives -= 1
    frog = Frog(SCREEN_WIDTH // 2, (SCREEN_HEIGHT // 2) + 370, SCREEN_WIDTH, SCREEN_HEIGHT)
    frog_group.add(frog)
    if lives == 0:
      game_over = True
      lives = 3

  if pygame.sprite.groupcollide(frog_group, truck_rev_group, True, False):
    lives -= 1
    frog = Frog(SCREEN_WIDTH // 2, (SCREEN_HEIGHT // 2) + 370, SCREEN_WIDTH, SCREEN_HEIGHT)
    frog_group.add(frog)
    if lives == 0:
      game_over = True
      lives = 3

  # Spacing out all of the objects
  time_now = pygame.time.get_ticks()
  if time_now - last_car1 > car1_frequency:
    last_car1 = time_now
    car1 = Car1(SCREEN_WIDTH, 682) # position on the screen
    car_1 = Car1(SCREEN_WIDTH, 497) # position on the screen
    car1_group.add(car1, car_1)
  
  if time_now - last_car2 > car2_frequency:
    last_car2 = time_now
    car2 = Car2(-100, 437) # position on the screen
    car2_group.add(car2)
  
  if time_now - last_truck > truck_frequency:
    last_truck = time_now
    truck = Truck(-160, 560) # position on the screen
    truck_group.add(truck)
  
  if time_now - last_truck_rev > truck_rev_frequency:
    last_truck_rev = time_now
    truck_rev = TruckRev(SCREEN_WIDTH, 620) # position on the screen
    truck_rev_group.add(truck_rev)

  if time_now - last_log1 > log1_frequency:
    last_log1 = time_now
    log1 = Log1(SCREEN_WIDTH, 310) # position on the screen
    log1_group.add(log1)

  if time_now - last_log2 > log2_frequency:
    last_log2 = time_now
    log2 = Log2(SCREEN_WIDTH, 186) # position on the screen
    log2_group.add(log2)

  if time_now - last_log3 > log3_frequency:
    last_log3 = time_now
    log3 = Log3(SCREEN_WIDTH, 60) # position on the screen
    log3_group.add(log3)

  if time_now - last_turtle1 > turtle1_frequency:
    last_turtle1 = time_now
    turtle1 = Turtle1(-100, 248) # position on the screen
    turtle1_group.add(turtle1)

  if time_now - last_turtle2 > turtle2_frequency:
    last_turtle2 = time_now
    turtle2 = Turtle2(-100, 122) # position on the screen
    turtle2_group.add(turtle2)

  # Update cars
  car1_group.update()
  car2_group.update()
  truck_group.update()
  truck_rev_group.update()
  log1_group.update()
  log2_group.update()
  log3_group.update()
  turtle1_group.update()
  turtle2_group.update()

  # render image variables
  screen.blit(fitted_background, (0,0))
  screen.blit(frog.image, frog.rect)
  car1_group.draw(screen)
  car2_group.draw(screen)
  truck_group.draw(screen)
  truck_rev_group.draw(screen)
  log1_group.draw(screen)
  log2_group.draw(screen)
  log3_group.draw(screen)
  turtle1_group.draw(screen)
  turtle2_group.draw(screen)

  pygame.display.update()

pygame.quit()