from sys import exit

from Ball import *

pygame.init()


def Change_Icon():
    pass

def Display_score():
    score_player1_surf = font.render(f"{player1.score:02d}", False, (255,255,255))
    score_player1_rect = score_player1_surf.get_rect(topleft = (650,50))
    score_player2_surf = font.render(f"{player2.score:02d}", False, (255,255,255))
    score_player2_rect = score_player2_surf.get_rect(topright = (630,50))
    screen.blit(score_player1_surf,score_player1_rect)
    screen.blit(score_player2_surf,score_player2_rect)

def screenLoad():
    global screen, font, clock
    screen = pygame.display.set_mode((1280, 720))
    pygame.display.set_caption('Pong')
    Change_Icon()
    font = pygame.font.Font('Assets/font/bit5x3.ttf', 40)
    clock = pygame.time.Clock()

def DisplayStartMenu():
    game_name = font.render('pong', False, (255,255,255))
    game_name_rect = game_name.get_rect(center = (640,150))
    game_message = font.render('Press space to play', False, (255,255,255))
    game_message_rect = game_message.get_rect(center = (640,200))
    pygame.draw.rect(screen, 'white', pygame.Rect(0,0,1280,720), 4)
    screen.blit(game_message, game_message_rect)
    screen.blit(game_name, game_name_rect)
    #ball.draw(screen)

screenLoad()

game_active = False

ball_group = pygame.sprite.GroupSingle()
ball_group.add(ball())

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

        # field creation
        pygame.draw.rect(screen, 'white', pygame.Rect(0, 0, 1280, 720), 4)
        pygame.draw.line(screen, 'white', (640, 0), (640, 720), 4)
        Display_score()

        ball_group.draw(screen)
        ball.update(screen)

        player_group.draw(screen)

        player1.player_input()
        player2.player_input()
        player.update()

        pygame.display.update()
        clock.tick(60)

    else:
        DisplayStartMenu()
        pygame.display.update()