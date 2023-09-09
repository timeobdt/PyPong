import pygame

from sys import exit

pygame.init()

class Ball(pygame.sprite.Sprite):
    
    def __init__(self):
        super().__init__()
        self.surf = pygame.Surface((50,50))
        self.surf.fill((255, 255, 255))
        self.image = self.surf.copy()
        self.rect = self.image.get_rect()
        self.Xvitesse = 0
        self.Yvitesse = 0
        self.rect.center = (640, 360)    
        self.wall_sound = pygame.mixer.Sound('Assets/sound/wall.wav')
        self.paddle_sound = pygame.mixer.Sound('Assets/sound/paddle.wav')
        self.score_sound = pygame.mixer.Sound('Assets/sound/score.wav')
    
    def ball_movement(self):
        
        #movement with screen border
        self.rect.x += self.Xvitesse
        self.rect.y += self.Yvitesse
        
        if self.rect.y == screen.get_height() - self.rect.height:
            self.Yvitesse *= -1
            self.wall_sound.play()
            
        if self.rect.y <= 0:
            self.Yvitesse *= -1
            self.wall_sound.play()
            
        if self.rect.x == screen.get_width() - self.rect.width:
            self.rect.center = (640, 360) #teleporte the ball to the center of the screen if it goes to far on the right
            #stop the ball when a player score
            self.Xvitesse = 0
            self.Yvitesse = 0
            player2.score += 1
            self.score_sound.play()
            
        
        if self.rect.x <= 0:
            self.rect.center = (640, 360) #teleporte the ball to the center of the screen if it goes to far on the left
            #stop the ball when a player score
            self.Xvitesse = 0
            self.Yvitesse = 0
            player1.score += 1
            self.score_sound.play()
                        
    def check_collision(self):
        if pygame.sprite.spritecollide(self, player, False):
            self.Xvitesse *= -1  # Inverse la direction horizontale de la balle
            self.paddle_sound.play()
            
    
    def update(self):
        if self.Xvitesse == 0 and self.Yvitesse == 0:
            self.Xvitesse += 5
            self.Yvitesse += 5
            
        self.ball_movement()
        self.check_collision()
        
        
class Player(pygame.sprite.Sprite):
    def __init__(self, number):
        #player 1
        if number == 1:
            super().__init__()
            self.number = 1
            self.surf = pygame.Surface((50,150))
            self.surf.fill((255, 255, 255))
            self.image = self.surf.copy()
            self.rect = self.image.get_rect()
            self.rect.center = (1175, 360)
            self.score = 0
            self.control_keys = {
        1: (pygame.K_UP, pygame.K_DOWN),  # player 1 : up arrow and down arrow
        2: (pygame.K_a, pygame.K_w)  # player 2 : key A ans key W
    }   
        #Joueur 2   
        else:
            super().__init__()
            self.number = 2
            self.surf = pygame.Surface((50,150))
            self.surf.fill((255, 255, 255))
            self.image = self.surf.copy()
            self.rect = self.image.get_rect()
            self.rect.center = (100, 360)
            self.score = 0
            self.control_keys = {
        1: (pygame.K_UP, pygame.K_DOWN),  # player 1 : up arrow and down arrow
        2: (pygame.K_a, pygame.K_w)  # player 2 : key A ans key W
    } 
            
    def player_input(self):
        keys = pygame.key.get_pressed()
        up_key, down_key = self.control_keys.get(self.number)
    
        if keys[up_key]:
            self.rect.y -= 6
        
        if keys[down_key]:
            self.rect.y += 6
    
    def update(self):
        pass
        

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
    

screenLoad()

ball = pygame.sprite.GroupSingle()
ball.add(Ball())

player1 = Player(1)
player2 = Player(2)

player = pygame.sprite.Group()
player.add(player1)
player.add(player2)

game_active = False

def DisplayStartMenu():
    game_name = font.render('pong', False, (255,255,255))
    game_name_rect = game_name.get_rect(center = (640,150)) 
    game_message = font.render('Press space to play', False, (255,255,255))
    game_message_rect = game_message.get_rect(center = (640,200))
    pygame.draw.rect(screen, 'white', pygame.Rect(0,0,1280,720), 4)  
    screen.blit(game_message, game_message_rect)
    screen.blit(game_name, game_name_rect)
    ball.draw(screen)

while True:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if not game_active:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                game_active = True
    
    if game_active:
        
        
        screen.fill((0,0,0))
        
        #field creation
        pygame.draw.rect(screen, 'white', pygame.Rect(0,0,1280,720), 4)
        pygame.draw.line(screen, 'white', (640,0), (640,720), 4)
        Display_score()
          
        ball.draw(screen)
        ball.update()
    
        player.draw(screen)
    
        player1.player_input()
        player2.player_input()
        player.update()
        
        pygame.display.update()
        clock.tick(60) 

    else:
        DisplayStartMenu()
        pygame.display.update()
        
        
#pour faire attendre le jeux : pygame.time.delay(5 * 1000)