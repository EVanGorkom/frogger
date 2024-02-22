import pygame
from pygame.locals import *

class Truck(pygame.sprite.Sprite):
  def __init__(self, x, y):
    pygame.sprite.Sprite.__init__(self)
    self.image = pygame.image.load('img/truck.png')
    self.rect = self.image.get_rect()
    self.rect.x = x
    self.rect.y = y
  
  def update(self):
    self.rect.x += 2
    if self.rect.right > 870:
      self.kill()