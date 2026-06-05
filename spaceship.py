import pygame


class SpaceShip(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(
            'sprites/Pixel SHMUP Free/metalic_02.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.image = pygame.transform.scale(
            self.image, (self.rect.width * 1.5, self.rect.height * 1.5))


class PLayerProjectile(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(
            'sprites/SHMUP-Asset-Pack-1/PNG/Projectiles/Bullets/Bullets-1.png').convert_alpha()
        self.speed = 12
        self.rect = self.image.get_rect()

    def update(self):
        self.rect.y -= self.speed
