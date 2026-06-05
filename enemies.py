import pygame
import random


class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(
            'sprites/Pixel SHMUP Free/enemy_1_1.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.has_shot = False


class EnemyProjectile(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(
            'sprites/SHMUP-Asset-Pack-1/PNG/Projectiles/Flameshot/Flameshot-1.png').convert_alpha()
        # self.image = pygame.transform.rotate(self.image, 180)
        self.speed = 6
        self.rect = self.image.get_rect()

    def update(self):
        self.rect.y += self.speed
