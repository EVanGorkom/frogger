import pygame
from pygame.locals import *


class Frog(pygame.sprite.Sprite):
  def __init__(self, x, y, SCREEN_WIDTH, SCREEN_HEIGHT):
    super().__init__()
    self.images = {
      "up": pygame.image.load("img/frog-icon-up.png"),
      "down": pygame.image.load("img/frog-icon-down.png"),
      "left": pygame.image.load("img/frog-icon-left.png"),
      "right": pygame.image.load("img/frog-icon-right.png")
    }
    self.direction = "up"
    self.image = self.images[self.direction]
    self.rect = self.image.get_rect(center=(x, y))
    self.screen_width = SCREEN_WIDTH
    self.screen_height = SCREEN_HEIGHT

  def update_direction(self, direction):
    if direction in self.images:
      self.direction = direction
      self.image = self.images[self.direction]

  def move(self, dx, dy):
    # determine new position after move
    new_x = self.rect.x + dx
    new_y = self.rect.y + dy

    # check if the new position is within the screen's boundaries
    if 0 <= new_x <= self.screen_width - self.rect.width:
      self.rect.x = new_x
    if 0 <= new_y <= self.screen_height - self.rect.height:
      self.rect.y = new_y
    