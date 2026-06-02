import pygame
import random
from enemies import Alien, EnemyProjectile
from spaceship import SpaceShip, PLayerProjectile
pygame.init()
pygame.font.init()

print(pygame.font.get_init())

GAME_FONT = pygame.font.Font(pygame.font.get_default_font(), size=50)

USERNAME = 'wnsnk'
score = 0

SCREEN_WIDTH = 720
SCREEN_HEIGHT = 1280
MOVEMENT_SPEED = 10
player_shot = False
player_reload = 0
enemy_shot = False
enemy_reload = 0
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Space Invaders')
clock = pygame.time.Clock()
delta_time = clock.tick(60) / 1000

all_sprites_list = pygame.sprite.Group()


def shoot(player_x, player_y):
    global player_reload, player_shot
    if not player_shot:
        player_shot = True
        player_reload = 5
        bullet = PLayerProjectile()
        bullet.rect.x = (player.rect.x + (player.rect.width / 2)) + 7
        bullet.rect.y = player_y + 10
        all_sprites_list.add(bullet)
        return bullet


def shoot_enemy(enemy_x, enemy_y):
    global enemy_shot

    if not enemy_shot:
        # random_num = random.randint(1, 1000)
        # print(random_num)

        enemy_shot == True
        enemy_bullet = EnemyProjectile()
        enemy_bullet.rect.x = enemy_x + (enemy.rect.width / 2)
        enemy_bullet.rect.y = enemy_y + 10
        all_sprites_list.add(enemy_bullet)
        return enemy_bullet


# player
player = SpaceShip()
player.rect.x = SCREEN_WIDTH / 2
player.rect.y = (SCREEN_HEIGHT - (player.image.height * 2))
all_sprites_list.add(player)

# enemies
enemies_list = []
width_enemy = Alien().image.width
empty_space_x = SCREEN_WIDTH / width_enemy
num_aliens_x = (SCREEN_WIDTH - (empty_space_x * 2)) / \
    (width_enemy + empty_space_x)
num_aliens_x += 1
alien_x = empty_space_x
alien_y = 20
for _ in range(int(num_aliens_x)):
    enemy = Alien()
    enemy.rect.x = alien_x
    alien_x += (enemy.image.width + empty_space_x)
    enemy.rect.y = alien_y
    all_sprites_list.add(enemy)
    enemies_list.append(enemy)

player_bullet_list = []

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill('black')
    all_sprites_list.update()
    all_sprites_list.draw(screen)
    delta_time = clock.tick(60) / 1000

    keys = pygame.key.get_pressed()
    if keys[pygame.K_a] or keys[pygame.K_LEFT]:
        player.rect.x -= (MOVEMENT_SPEED)
    if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
        player.rect.x += (MOVEMENT_SPEED)
    if keys[pygame.K_w] or keys[pygame.K_UP]:
        player.rect.y -= (MOVEMENT_SPEED)
    if keys[pygame.K_s] or keys[pygame.K_DOWN]:
        player.rect.y += (MOVEMENT_SPEED)
    if keys[pygame.K_SPACE]:
        bullet = shoot(player_x=player.rect.x, player_y=player.rect.y)

    if player_shot:
        player_reload -= 1
        if player_reload == 0:
            player_shot = False
    if enemy_shot:
        enemy_reload -= 1
        if enemy_reload == 0:
            enemy_shot = False
    random_num = random.randint(1, 5)
    if random_num == 1:
        random_enemy = random.choice(enemies_list)
        shoot_enemy(random_enemy.rect.x, random_enemy.rect.y)
    pygame.display.update()


pygame.quit()
