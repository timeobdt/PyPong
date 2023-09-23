import pygame
from Ball import *

ball = ball()
ball_group = pygame.sprite.GroupSingle()
ball_group.add(ball)

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
    pygame.display.set_caption('Pong')
    Change_Icon()
def DisplayStartMenu():
    game_name = font.render('pong', False, (255,255,255))
    game_name_rect = game_name.get_rect(center = (640,150))
    game_message = font.render('Press space to play', False, (255,255,255))
    game_message_rect = game_message.get_rect(center = (640,200))
    pygame.draw.rect(screen, 'white', pygame.Rect(0,0,1280,720), 4)
    screen.blit(game_message, game_message_rect)
    screen.blit(game_name, game_name_rect)
    credit_message = font.render('Version 1.0 github.com/timeobdt', False, (255,255,255))
    credit_message_rect = credit_message.get_rect(center = (640, 700))
    screen.blit(credit_message, credit_message_rect)

def DisplayPause():
        game_message = font.render('Game is paused', False, (255, 255, 255))
        game_message_rect = game_message.get_rect(center=(640, 200))
        pygame.draw.rect(screen, 'white', pygame.Rect(0, 0, 1280, 720), 4)
        screen.blit(game_message, game_message_rect)

def field_creation():
    pygame.draw.rect(screen, 'white', pygame.Rect(0, 0, 1280, 720), 4)
    pygame.draw.line(screen, 'white', (640, 0), (640, 720), 4)
    Display_score()

font = pygame.font.Font('Assets/font/bit5x3.ttf', 40)
clock = pygame.time.Clock()



