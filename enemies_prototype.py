import pygame
import random


class Base_ranger(pygame.sprite.Sprite):
    """ It a base class of the ranger enemy """
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.rect = pygame.Rect(50, 50, 75, 75)
        self.rect.bottom = y
        self.rect.centerx = x
        self.bullet = Laser(self.rect.centerx, self.rect.bottom, self, None)
        self.lastMove = 'down'

    def damage(self, pl):
        if self.rect.colliderect(pl) or self.bullet.colliderect(pl):
            pl.health -= 3


class Laser(pygame.sprite.Sprite):
    """ Class describing of behavior of the bullet which used to shooting by the Player """

    def __init__(self, x, y, enemy, storage):
        """ Initializing the bullet """
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((10, 100))
        self.image.fill((0, 255, 0))
        self.rect = self.image.get_rect()
        self.rect.bottom = y
        self.rect.centerx = x
        self.speedy = -30
        self.__var__ = enemy.lastMove
        self.enemy_ammo = storage

    def update(self):
        """ Updating bullet's position every turn and control bullet out-of-screen"""
        if self.__var__ == 'right':
            self.rect.x -= self.speedy
        elif self.__var__ == 'left':
            self.rect.x += self.speedy
        elif self.__var__ == 'up':
            self.rect.y += self.speedy
        elif self.__var__ == 'down':
            self.rect.y -= self.speedy
        if self.rect.x > WIDTH or self.rect.x < 0 or self.rect.y > HEIGHT or self.rect.y < 0:
            self.enemy_ammo.remove(self)
