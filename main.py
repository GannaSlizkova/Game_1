import pygame
import random

from pygame.constants import QUIT

pygame.init()

FPS = pygame.time.Clock()
HEIGHT = 800
WIGHT = 1200
color_black = (0, 0, 0)
color_white = (255, 255, 255)
player_size = (10, 10)

main_display = pygame.display.set_mode((WIGHT, HEIGHT))

player = pygame.Surface(player_size)
player.fill(color_white)
player_rect = player.get_rect()
player_speed = [1, 1]


playing = True

while playing:
    FPS.tick(400)
    for event in pygame.event.get():
        if event.type == QUIT:
            playing = False

    main_display.fill(color_black)

    if player_rect.bottom >= HEIGHT:
        player_speed = random.choice(([1, -1]), ([-1, -1]))

    if player_rect.right >= WIGHT:
        player_speed = random.choice(([-1, -1]), ([-1, 1]))

    if player_rect.top <= 0:
        player_speed = random.choice(([-1, 1]), ([1, 1]))

    if player_rect.left <= 0:
        player_speed = random.choice(([1, -1]), ([1, 1]))


    main_display.blit(player, player_rect)

    player_rect = player_rect.move(player_speed)

    pygame.display.flip()