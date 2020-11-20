import pygame
import random


class Comet(pygame.sprite.Sprite):

    def __init__(self, game):
        pygame.sprite.Sprite.__init__(self)
        self.game = game
        # définir l'image associé à cette comette
        self.image = pygame.transform.scale(pygame.image.load("img/comet.png"), (100, 100))
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(0, 1900 - 100)
        self.rect.y = random.randrange(-500, -400)
        self.speed_y = random.randrange(2, 8)

    def boundary(self):
        if self.rect.y >= 750:
            self.kill()
            self.spawn_new_meteor()

    def spawn_new_meteor(self):
        self.rect.x = random.randrange(0, 1900 - 100)
        self.rect.y = random.randrange(-500, -400)
        self.speed_y = random.randrange(2, 8)

    def update(self):
        self.rect.y += self.speed_y
        if self.game.check_collision(self, self.game.all_players):
            self.remove()
            self.game.player.damage(10)
        self.boundary()
