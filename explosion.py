import pygame


class Explosion(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.images = []
        for num in range(8):
            num += 1
            image = pygame.image.load(
                f'sprites/SHMUP-Asset-Pack-1/PNG/VFX/Explosion/Explosion-{num}.png').convert_alpha()
            self.images.append(image)

        self.index = 0
        self.image = self.images[self.index]
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]
        self.counter = 0
        self.image = pygame.transform.scale(
            self.image, (self.rect.width * 2, self.rect.height * 2))

    def update(self):
        explosion_speed = 4
        self.counter += 1
        if self.counter >= explosion_speed and self.index < len(self.images) - 1:
            self.counter = 0
            self.index += 1
            self.image = self.images[self.index]
            self.image = pygame.transform.scale(
                self.image, (self.rect.width * 2, self.rect.height * 2))

        if self.index >= len(self.images) - 1 and self.counter >= explosion_speed:
            self.kill()
