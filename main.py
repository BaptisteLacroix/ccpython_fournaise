from game import Game
import pygame


pygame.init()

# charger le jeu
game = Game()

# Affichage écran
pygame.display.set_caption("Dodo")
screen = pygame.display.set_mode((game.W, game.H))

background = pygame.image.load("img/1_37.png")

# Position de l'image
x = 0

# Coordonnées play_button
play_button_x_min = 691
play_button_x_max = 1210
play_button_y_min = 503
play_button_y_max = 683

# importer/charger la bannière
banner = pygame.image.load("C:/Users/k/Desktop/Langage informatique/programmation/Python/CodingClubLive/cc_sonic_run"
                           "-1.0/img/Banniere/banner0.jpg")
banner = pygame.transform.scale(banner, (game.W, game.H))
banner_rect = banner.get_rect()


#########

running = True

#################

frame = 0

# Boucle tant que condition est vraie
while running:

    keys = pygame.key.get_pressed()
    game.player.process_movement_animation(keys)

    # Appliquer l'arrère plan et le faire bouger
    screen.blit(background, (0, 0))

    # vérifier si le jeu a commencé
    if game.is_playing:
        # délencher les instructions de la partie
        game.update(screen)
        game.all_sprites.update()
        game.all_sprites.draw(screen)
    # vérifier si le jeu n'a pas commencé
    else:
        # ajouter l'écran de bienvenue
        screen.blit(banner, banner_rect)

    # Mise a jour de la fenêtre
    pygame.display.flip()

    # Si le joueur ferme la fenêtre
    for event in pygame.event.get():
        # vérifier la fermeture de la fenêtre
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()

        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            print(pygame.mouse.get_pos())
            x_mouse, y_mouse = pygame.mouse.get_pos()
            # Vérification si clique sur le bouton
            if play_button_x_min < x_mouse < play_button_x_max and play_button_y_max > y_mouse > play_button_y_min:
                # mettre le jeu en mode "lancé"
                game.start()
