from typing import List

import pygame
from glob import glob

img_loader = lambda img: pygame.transform.scale(pygame.image.load(img), (200, 200))
left_anim_imgs = list(map(img_loader, glob("./img/dodo*.png")))
right_anim_imgs = list(map(img_loader, glob("./img/dodo*.png")))


# Joueur Sonic
class Player(pygame.sprite.Sprite):
    left_anim_iter = iter(left_anim_imgs)
    right_anim_iter = iter(right_anim_imgs)
    anim_counter = 0

    def __init__(self, game):
        super().__init__()
        self.game = game
        self.attack = 50
        self.health = 102
        self.max_health = 102
        self.velocity = 10
        self.image = pygame.image.load("img/dodo.png")
        self.rect = self.image.get_rect()
        self.rect.x = 179
        self.rect.y = 608

    def damage(self, amount):
        if self.health - amount > amount:
            self.health -= amount
        else:
            # si le joueur n'a plus de points de vie
            self.game.game_over()

    def update_health_bar(self, surface):
        # dessiner la barre de vie
        pygame.draw.rect(surface, (60, 63, 60), [self.rect.x + 15, self.rect.y - 20, self.max_health, 7])
        pygame.draw.rect(surface, (229, 25, 25), [self.rect.x + 15, self.rect.y - 20, self.health, 7])

    def move_right(self):
        self.rect.x += self.velocity

    def move_left(self):
        self.rect.x -= self.velocity

    def process_movement_animation(self, keys: List[bool]) -> None:
        """
        Processes the character movement animation
        :type keys: list[bool]
        :param keys: Pressed keys status
        :return: None
        """
        if Player.anim_counter % self.velocity == 0:
            if keys[pygame.K_a]:
                try:
                    self.image = next(Player.left_anim_iter)
                except(StopIteration):
                    Player.left_anim_iter = iter(left_anim_imgs)
                    self.image = next(Player.left_anim_iter)
            elif keys[pygame.K_d]:
                try:
                    self.image = next(Player.right_anim_iter)
                except(StopIteration):
                    Player.right_anim_iter = iter(right_anim_imgs)
                    self.image = next(Player.right_anim_iter)
            else:
                self.image = pygame.image.load("img/dodo.png")
        Player.anim_counter += 1
