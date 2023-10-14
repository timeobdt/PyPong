from sys import exit

import pygame

from game_init import *

pygame.init()

screenLoad()

game_menu = True
game_active = False
game_paused = False
game_color = False

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if not game_active and game_menu:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                game_active = True
                game_menu = False

        if game_active:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_F1:
                game_color = True

        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            game_paused = True
            game_active = False

        if not game_active and game_paused:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                game_paused = False
                game_active = True

    if game_menu:
        DisplayStartMenu()
        pygame.display.update()
    if game_paused:
        DisplayPause()
        pygame.display.update()

    if game_active:

        if game_color:
            screen.fill((55, 127, 3))
        else:
            screen.fill((0, 0, 0))

        field_creation()

        ball_group.draw(screen)
        ball.update()

        player_group.draw(screen)

        player1.player_input()
        player2.player_input()

        player1.update()
        player2.update()

        pygame.display.update()
        clock.tick(60)
