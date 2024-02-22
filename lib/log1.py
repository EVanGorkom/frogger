import pygame
from pygame.locals import *

class Log1(pygame.sprite.Sprite):
  def __init__(self, x, y, speed):
    pygame.sprite.Sprite.__init__(self)
    self.image = pygame.image.load('img/log.png')
    self.rect = self.image.get_rect()
    self.rect.x = x
    self.rect.y = y
    self.speed = speed
  
  def update(self):
    self.rect.x -= self.speed
    if self.rect.right < 0:
      self.kill()