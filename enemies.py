import pygame


class Alien(pygame.sprite.Sprite):
    # This class represents a car. It derives from the "Sprite" class in Pygame.

    def __init__(self):
        # Call the parent class (Sprite) constructor
        super().__init__()
        self.image = pygame.image.load(
            'sprites/Pixel SHMUP Free/enemy_1_1.png').convert_alpha()

        # Fetch the rectangle object that has the dimensions of the image.
        self.rect = self.image.get_rect()

        # self.image = pygame.transform.scale(
        #     self.image, (screen_width/20, screen_height/20))
