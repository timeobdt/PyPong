from sys import exit

import pygame

from game_init import *

pygame.init()

screenLoad()

game_menu = True
game_active = False
game_paused = False
game_color = False

class GameState:

    PAUSED = 0
    RUNNING = 1
    MENU = 2

    CURRENT = MENU

    @staticmethod
    def next():
        GameState.CURRENT = abs(GameState.CURRENT - 1)

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if event.type == pygame.KEYDOWN:
            if ((event.key == pygame.K_SPACE and
                GameState.CURRENT == GameState.MENU) or
                    (event.key == pygame.K_ESCAPE and
                     GameState.CURRENT != GameState.MENU)):
                GameState.next()
            elif GameState.CURRENT == GameState.RUNNING and event.key == pygame.K_F1:
                game_color = True

        """
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
                game_active = True
                game_paused = False
        """

    if GameState.CURRENT == GameState.MENU:
        DisplayStartMenu()
        pygame.display.update()
    elif GameState.CURRENT == GameState.PAUSED:
        DisplayPause()
        pygame.display.update()
    else:
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
