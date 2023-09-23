from sys import exit

from game_init import *

pygame.init()

screenLoad()

game_active = False

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if not game_active:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                game_active = True

    if game_active:

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

    else:
        DisplayStartMenu()
        pygame.display.update()