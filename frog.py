import pygame
from pygame.locals import *


class Frog(pygame.sprite.Sprite):
  def __init__(self, x, y):
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

  def update_direction(self, direction):
    if direction in self.images:
      self.direction = direction
      self.image = self.images[self.direction]

  def move(self, dx, dy):
    self.rect.x += dx
    self.rect.y += dy