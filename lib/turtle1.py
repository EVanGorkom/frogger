import pygame
from pygame.locals import *

class Turtle1(pygame.sprite.Sprite):
  def __init__(self, x, y):
    pygame.sprite.Sprite.__init__(self)
    self.image = pygame.image.load('img/turtle.png')
    self.rect = self.image.get_rect()
    self.rect.x = x
    self.rect.y = y
  
  def update(self):
    self.rect.x += 1
    if self.rect.right > 800:
      self.kill()