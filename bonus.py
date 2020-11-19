import pygame
import random


class Bonus(pygame.sprite.Sprite):

    def __init__(self, bonus_event):
        super().__init__()
        # définir l'image associé à cette bonus
        self.image = pygame.image.load("img/Star.png")
        self.rect = self.image.get_rect()
        self.velocity = random.randint(1, 3)
        self.rect.x = random.randint(10, 1800)
        self.rect.y = -300
        self.bonus_event = bonus_event

    def remove(self):
        self.bonus_event.all_bonus.remove(self)

        # vérifier si le nombre de bonus est 0
        if len(self.bonus_event.all_bonus) == 0:
            # remettre la barre à 0
            self.bonus_event.reset_percent()
            # faire apparaitre à nouveau les2 premiers bonus
            self.bonus_event.game.comet()

    def fall(self):
        self.rect.y += self.velocity

        # ne tombe pas sur le sol
        if self.rect.y >= 610:
            # retirer la boule de feu
            self.remove()

            # si il n'y a plus de boule de feu sur le jeu
            if len(self.bonus_event.all_bonus) == 0:
                # remettre la jauge de vie au départ
                self.bonus_event.reset_percent()
                self.bonus_event.fall_mode = False

        # vérifier si la boule de feu touche le joueur
        if self.bonus_event.game.check_collision(
                self, self.bonus_event.game.all_players
        ):
            # retirer la boule de feu
            self.remove()
            # subir des dégats
            self.bonus_event.game.player.damage(20)
