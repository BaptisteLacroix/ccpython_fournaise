import pygame
from player import Player
from comet import Comet

run_right_path = "img/dodo"
img_extension = ".png"


# Classe qui représente le jeu
class Game:
    W = 1900
    H = 1000

    def __init__(self):
        # définir si le jeu a commencé ou non
        self.is_playing = False
        # position du fond
        self.background_origin_x = 0
        # grouper tous les sprites
        self.all_sprites = pygame.sprite.Group()
        # générer le joueur
        self.all_players = pygame.sprite.Group()
        self.player = Player(self)
        self.all_players.add(self.player)
        # grouper toutes les météorites
        self.all_comets = pygame.sprite.Group()
        self.pressed = {}
        # récupérer les comets du jeu
        for i in range(9):
            """Création de 9 météorites"""
            comet = Comet(self)
            self.all_comets.add(comet)
            self.all_sprites.add(comet)

    def start(self):
        self.is_playing = True

    def game_over(self):
        # remettre le jeu à zéro
        self.player.health = self.player.max_health
        self.is_playing = False

    def remove(self):
        self.all_comets.remove(self)

    def update(self, screen):
        # appliquer l'image du joueur
        screen.blit(self.player.image, self.player.rect)

        # Actualiser la barre de vie du joueur
        self.player.update_health_bar(screen)

        # vérifier si le joueur veut aller à gauche ou à droite
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_d] and self.player.rect.x < Game.W:
            self.player.move_right()
        if keystate[pygame.K_a] and self.player.rect.x > 0:
            self.player.move_left()

    def check_collision(self, sprite, group):
        return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask)
