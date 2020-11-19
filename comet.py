import pygame
import random


class Comet(pygame.sprite.Sprite):

    def __init__(self, comet_event):
        super().__init__()
        # définir l'image associé à cette comette
        self.image = pygame.image.load("img/comet.png")
        self.rect = self.image.get_rect()
        self.velocity = random.randint(1, 3)
        self.rect.x = random.randint(10, 1800)
        self.rect.y = -300
        self.comet_event = comet_event

    def remove(self):
        self.comet_event.all_comets.remove(self)

        # vérifier si le nombre de comettes est 0
        if len(self.comet_event.all_comets) == 0:
            # remettre la barre à 0
            self.comet_event.reset_percent()
            # faire apparaitre à nouveau les 2 premiers bonus
            self.comet_event.game.bonus_event.bonus()

    def fall(self):
        self.rect.y += self.velocity

        # ne tombe pas sur le sol
        if self.rect.y >= 610:
            # retirer la boule de feu
            self.remove()

            # si il n'y a plus de boule de feu sur le jeu
            if len(self.comet_event.all_comets) == 0:
                # remettre la jauge de vie au départ
                self.comet_event.reset_percent()
                self.comet_event.fall_mode = False

        # vérifier si la boule de feu touche le joueur
        if self.comet_event.game.check_collision(
                self, self.comet_event.game.all_players
        ):
            # retirer la boule de feu
            self.remove()
            # subir des dégats
            self.comet_event.game.player.damage(30)
