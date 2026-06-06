import pygame
import random
from enemies import Enemy, EnemyProjectile
from spaceship import SpaceShip, PLayerProjectile
from explosion import Explosion
pygame.init()
pygame.font.init()

pygame.font.get_init()

GAME_FONT = pygame.font.Font(pygame.font.get_default_font(), size=50)

USERNAME = 'wnsnk'
score = 0
kills = 0
lives = 5
SCREEN_WIDTH = 720
SCREEN_HEIGHT = 1080
MOVEMENT_SPEED = 10
player_shot = False
player_reload = 0
player_reload_speed = 40
enemy_shot = False
enemy_reload = 0
enemy_move_speed = 100
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Space Invaders')
clock = pygame.time.Clock()
delta_time = clock.tick(60) / 1000

all_sprites_list = pygame.sprite.Group()

# shooting


def shoot(player_x, player_y):
    global player_reload, player_shot
    if not player_shot:
        player_shot = True
        player_reload = player_reload_speed
        bullet = PLayerProjectile()
        bullet.rect.x = (player.rect.x + (player.rect.width / 2)) + 7
        bullet.rect.y = player_y + 10
        all_sprites_list.add(bullet)
        player_bullet_list.append(bullet)
        return bullet


def shoot_enemy(enemy_x, enemy_y):
    global enemy_shot

    if not enemy_shot:
        enemy_shot == True
        enemy_bullet = EnemyProjectile()
        enemy_bullet.rect.x = enemy_x + (enemy.rect.width / 2)
        enemy_bullet.rect.y = enemy_y + 10
        all_sprites_list.add(enemy_bullet)
        enemy_bullet_list.append(enemy_bullet)
        return enemy_bullet


# player
player = SpaceShip()
player.rect.x = SCREEN_WIDTH / 2
player.rect.y = (SCREEN_HEIGHT - (player.image.height * 3))
all_sprites_list.add(player)

# enemies
enemies_list = []

enemy = Enemy()


def create_enemies():
    width_enemy = Enemy().image.width
    empty_space_x = SCREEN_WIDTH / width_enemy
    num_aliens_x = (SCREEN_WIDTH - (empty_space_x * 2)) / \
        (width_enemy + empty_space_x)
    num_aliens_x += 1
    alien_x = empty_space_x
    alien_y = 20
    for row in range(5):
        for column in range(int(num_aliens_x)):
            enemy = Enemy()
            enemy.rect.x = alien_x
            alien_x += (enemy.image.width + empty_space_x)
            enemy.rect.y = alien_y
            all_sprites_list.add(enemy)
            enemies_list.append(enemy)
        alien_y += 50
        alien_x = empty_space_x


create_enemies()

# collision detection


def check_player_wall_collision():
    if player.rect.right > (screen.width - (player.rect.width / 2)):
        player.rect.x -= MOVEMENT_SPEED
    if player.rect.left < 0:
        player.rect.x += MOVEMENT_SPEED


def check_if_player_bullet_hit_enemy(enemy_list):
    global enemy_move_speed, score
    for enemy in enemy_list:
        for bullet in player_bullet_list:
            if enemy.rect.left < bullet.rect.x < enemy.rect.right and enemy.rect.top < bullet.rect.y < enemy.rect.bottom:
                explosion = Explosion(bullet.rect.x, bullet.rect.y)
                all_sprites_list.add(explosion)
                player_bullet_list.remove(bullet)
                enemies_list.remove(enemy)
                all_sprites_list.remove(bullet)
                all_sprites_list.remove(enemy)
                enemy_move_speed -= 2

                score += 5


def check_if_player_bullet_out_of_sceen():
    for bullet in player_bullet_list:
        if bullet.rect.y < 0:
            player_bullet_list.remove(bullet)
            all_sprites_list.remove(bullet)


def check_if_enemy_bullet_out_of_screen():
    for bullet in enemy_bullet_list:
        if bullet.rect.y > screen.height:
            enemy_bullet_list.remove(bullet)
            all_sprites_list.remove(bullet)


def check_if_player_got_hit():
    global lives
    for bullet in enemy_bullet_list:
        if player.rect.left < bullet.rect.x < player.rect.right and player.rect.top < bullet.rect.y < player.rect.bottom:
            lives -= 1
            print(lives)
            explosion = Explosion(bullet.rect.x, bullet.rect.y)

            all_sprites_list.add(explosion)
            all_sprites_list.update()
            enemy_bullet_list.remove(bullet)
            all_sprites_list.remove(bullet)

            if lives <= 0:
                # TODO FIX
                game_over_text = f'Game Over\nScore: {score}'
                game_over_render = GAME_FONT.render(
                    game_over_text, True, 'white')
                text_width, text_height = GAME_FONT.size(game_over_text)
                screen.blit(game_over_render, (screen.width / 2,
                            (screen.height / 2) - text_height))


def check_collisions():
    check_player_wall_collision()
    check_if_player_bullet_hit_enemy(enemies_list)
    check_if_player_bullet_out_of_sceen()
    check_if_enemy_bullet_out_of_screen()
    check_if_player_got_hit()


player_bullet_list = []
enemy_bullet_list = []
count = 0
enemy_steps_taken = 0
enemy_go_to_left = False
enemy_go_down = False
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill('black')
    all_sprites_list.update()
    all_sprites_list.draw(screen)
    delta_time = clock.tick(60) / 1000

    if count >= enemy_move_speed:
        if enemy_go_down:
            for enemy in enemies_list:
                enemy.rect.y += 15
            enemy_go_down = False
        elif not enemy_go_to_left:
            for enemy in enemies_list:
                enemy.rect.x += 5
            enemy_steps_taken += 1
            if enemy_steps_taken >= 4:
                enemy_go_to_left = True
                enemy_go_down = True
        elif enemy_go_to_left:
            for enemy in enemies_list:
                enemy.rect.x -= 5
            enemy_steps_taken -= 1
            if enemy_steps_taken <= 0:
                enemy_go_to_left = False
                enemy_go_down = True

        count = 0

    keys = pygame.key.get_pressed()
    if keys[pygame.K_a] or keys[pygame.K_LEFT]:
        player.rect.x -= (MOVEMENT_SPEED)
    if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
        player.rect.x += (MOVEMENT_SPEED)
    # if keys[pygame.K_w] or keys[pygame.K_UP]:
    #     player.rect.y -= (MOVEMENT_SPEED)
    # if keys[pygame.K_s] or keys[pygame.K_DOWN]:
    #     player.rect.y += (MOVEMENT_SPEED)
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
    if len(enemies_list) > 0:
        random_num = random.randint(1, 10)
        if random_num == 1:
            random_enemy = random.choice(enemies_list)
            shoot_enemy(random_enemy.rect.x, random_enemy.rect.y)

    scoreboard_text = f'Score: {score}'
    scoreboard = GAME_FONT.render(scoreboard_text, True, 'white')
    score_text_width, score_text_height = GAME_FONT.size(scoreboard_text)
    screen.blit(scoreboard, (0, (SCREEN_HEIGHT - score_text_height)))
    lives_text = f'lives: {lives}'
    lives_render = GAME_FONT.render(lives_text, True, 'white')
    lives_text_width, lives_text_height = GAME_FONT.size(lives_text)
    screen.blit(lives_render, ((screen.width - (lives_text_width + 10),
                (SCREEN_HEIGHT - lives_text_height))))

    # collisions
    check_collisions()
    pygame.display.update()
    count += 1


pygame.quit()
