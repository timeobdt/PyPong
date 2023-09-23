from Player import *

pygame.init()

player1 = player(1)
player2 = player(2)

player_group = pygame.sprite.Group()
player_group.add(player1)
player_group.add(player2)

screen = pygame.display.set_mode((1280, 720))
class ball(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.surf = pygame.Surface((50, 50))
        self.surf.fill((255, 255, 255))
        self.image = pygame.image.load("Assets/ball_image/ball.png")
        self.rect = self.image.get_rect()
        self.Xvitesse = 0
        self.Yvitesse = 0
        self.rect.center = (640, 360)
        self.wall_sound = pygame.mixer.Sound('Assets/sound/wall.wav')
        self.paddle_sound = pygame.mixer.Sound('Assets/sound/paddle.wav')
        self.score_sound = pygame.mixer.Sound('Assets/sound/score.wav')

    def ball_movement(self):

        # movement with screen border
        self.rect.x += self.Xvitesse
        self.rect.y += self.Yvitesse

        if self.rect.y == screen.get_height() - self.rect.height:
            self.Yvitesse *= -1
            self.wall_sound.play()

        if self.rect.y <= 0:
            self.Yvitesse *= -1
            self.wall_sound.play()

        if self.rect.x == screen.get_width() - self.rect.width:
            self.rect.center = (
            640, 360)  # teleporte the ball to the center of the screen if it goes to far on the right
            # stop the ball when a player score
            self.Xvitesse = 0
            self.Yvitesse = 0
            player2.score += 1
            self.score_sound.play()

        if self.rect.x <= 0:
            self.rect.center = (
            640, 360)  # teleporte the ball to the center of the screen if it goes to far on the left
            # stop the ball when a player score
            self.Xvitesse = 0
            self.Yvitesse = 0
            player1.score += 1
            self.score_sound.play()

    def check_collision(self):
        if pygame.sprite.spritecollide(self, player_group, False):
            self.Xvitesse *= -1  # Inverse la direction horizontale de la balle
            self.paddle_sound.play()

    def update(self):
        if self.Xvitesse == 0 and self.Yvitesse == 0:
            self.Xvitesse += 5
            self.Yvitesse += 5

        self.ball_movement()
        self.check_collision()
