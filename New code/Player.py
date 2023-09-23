import pygame

class player(pygame.sprite.Sprite):
    def __init__(self, number):
        # player 1
        if number == 1:
            super().__init__()
            self.number = 1
            self.surf = pygame.Surface((50, 150))
            self.surf.fill((255, 255, 255))
            self.image = self.surf.copy()
            self.rect = self.image.get_rect()
            self.rect.center = (1175, 360)
            self.score = 0
            self.control_keys = {
                1: (pygame.K_UP, pygame.K_DOWN),  # player 1 : up arrow and down arrow
                2: (pygame.K_a, pygame.K_w)  # player 2 : key A ans key W
            }
            # Joueur 2
        else:
            super().__init__()
            self.number = 2
            self.surf = pygame.Surface((50, 150))
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

    def player_colision(self):
        if self.rect.y < 0:
            self.rect.y = 0

        if self.rect.y > 720 - self.rect.height:
            self.rect.y = 720 - self.rect.height

    def update(self):
        self.player_colision()