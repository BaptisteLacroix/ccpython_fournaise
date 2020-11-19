import pygame
from bonus import Bonus


class BonusFallEvent:

    # lors du chargement -> créer un compteur
    def __init__(self, game):
        self.percent = 0
        self.percent_speed = 5
        self.game = game
        self.fall_mode = False
        # définir un groupe de sprite pour stocker les comettes
        self.all_bonus = pygame.sprite.Group()

    def add_percent(self):
        self.percent += self.percent_speed / 10

    def is_full_loaded(self):
        return self.percent >= 100

    def bonus_fall(self):
        # apparaitre une première boule de feu
        self.all_bonus.add(Bonus(self))

    def attempt_fall(self):
        # la jauge d'évènement est totalement chargé
        if self.is_full_loaded():
            self.bonus_fall()
            if self.game.comet_event.is_full_loaded():
                self.all_bonus.remove(self)

                # appel de la méthode pour essayer de déclencher la pluie de cometes
                self.attempt_fall()
            self.fall_mode = True  # activer l'évènement

    def reset_percent(self):
        self.percent = 0

    def update_bar(self, surface):

        # ajouter du pourcentage à la bar
        self.add_percent()

        # appel de la méthode pour essayer de déclancher la pluie de cometes
        self.attempt_fall()

        # barre noir (en arrière plan)
        pygame.draw.rect(surface, (0, 0, 0), [
            0,  # l'axe des x
            surface.get_height() - 20,  # l'axe des y
            surface.get_width(),  # longueur de la fenetre
            10  # epaisseur de la barre
        ])
        # barre rouge (jauge d'évènement)
        pygame.draw.rect(surface, (187, 11, 11), [
            0,  # l'axe des x
            surface.get_height() - 20,  # l'axe des y
            (surface.get_width() / 100) * self.percent,  # longueur de la fenetre
            10  # epaisseur de la barre
        ])
