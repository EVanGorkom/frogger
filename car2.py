import pygame
from pygame.locals import *

class Car2(pygame.sprite.Sprite):
  def __init__(self, x, y):
    pygame.sprite.Sprite.__init__(self)
    self.image = pygame.image.load('img/car2.png')
    self.rect = self.image.get_rect()
    self.rect.x = x
    self.rect.y = y
  
  def update(self):
    self.rect.x += 8
    if self.rect.right > 750:
      self.kill()