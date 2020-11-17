import pygame
from player import Player

run_right_path = "img/dodo"
img_extension = ".png"


# Classe qui représente le jeu
class Game:
    W = 1920
    H = 1080

    def __init__(self):
        # définir si le jeu a commencé ou non
        self.is_playing = False
        # position du fond
        self.background_origin_x = 0
        # générer le joueur
        self.all_players = pygame.sprite.Group()
        self.player = Player(self)
        self.all_players.add(self.player)
        # Groupe de pics
        ### self.all_pics = pygame.sprite.Group()
        self.pressed = {}

    def start(self):
        self.is_playing = True
        # self.spawn_pics()
        # self.spawn_pics()

    def game_over(self):
        # remettre le jeu à zéro
        ### self.all_pics = pygame.sprite.Group()
        self.player.health = self.player.max_health
        self.is_playing = False

    def update(self, screen):
        # appliquer l'image du joueur
        screen.blit(self.player.image, self.player.rect)

        # Actualiser la barre de vie du joueur
        self.player.update_health_bar(screen)

        # recupérer les monstres de mon jeu
        """
        for Pics in self.all_pics:
            Pics.forward()
            Pics.update_health_bar(screen)
        """

        # appliquer l'ensemble des images de mon groupe de pics
        ### self.all_pics.draw(screen)

        # vérifier si le joueur veut aller à gauche ou à droite
        if self.pressed.get(pygame.K_d):
            print("droit")
            if self.player.rect.x < Game.W:
                print("je bouge a droite")
                self.player.move_right()
        if self.pressed.get(pygame.K_a):
            print("gauche")
            if self.player.rect.x > 0:
                print("je bouge a gauche")
                self.player.move_left()

        # print(self.player.rect.x)

    def check_collision(self, sprite, group):
        return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask)

