import sys

import pygame
from PyQt5.QtWidgets import QApplication

import Classes
import Authorize


if __name__ == '__main__':
    app = QApplication(sys.argv)
    authorizing = Authorize.Authorize()
    authorizing.show()
    if not authorizing.exec_() and authorizing.authorized:
        running = True
        turn = True
        break_while = False
        width, height = 1920, 1080
        pygame.init()
        screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        screen.fill((255, 255, 255))

        menu_ground = pygame.sprite.Group()
        player_sprite = pygame.sprite.Group()
        items = pygame.sprite.Group()
        ground_sprites = pygame.sprite.Group()
        image_btn = Classes.Image('close_button.png', (1860, 10), (50, 50), items)
        image_bg = Classes.Image('background.jpg', (0, 0), (1920, 1080), menu_ground)
        image_text = Classes.Image('start.png', (680, 400), (600, 170), menu_ground)
        player = Classes.Player(screen, (0, 0), None, player_sprite)
        items.draw(screen)
        menu_ground.draw(screen)
        pygame.display.flip()

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN and Classes.is_on_click(event.pos, 700, 400, 1300, 650):
                    break_while = True
                    break
                if event.type == pygame.MOUSEBUTTONDOWN and Classes.move_is_valid(event.pos, (1840, 1910), (10, 80)):
                    running = False
                else:
                    continue
            if break_while:
                break

        screen.fill((255, 255, 255))
        while running:
            level = Classes.Level(screen, 'level.txt', 8, 8, 50)
            level.draw_level_ground('ground sprite.png', 'dec.png')
            player_sprite.draw(screen)
            items.draw(screen)
            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN and Classes.move_is_valid(event.pos, (1840, 1910), (10, 80)):
                    running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        while event.type == pygame.KEYDOWN and Classes.move_is_valid((player.player_x - 10,
                                                                                      player.player_y),
                                                                                     (0, width - 75),
                                                                                     (0, height - 75)):
                            for event in pygame.event.get():
                                pass
                            Classes.movement(-10, 0, player_sprite, items, player, level, screen)
                    elif event.key == pygame.K_RIGHT:
                        while event.type == pygame.KEYDOWN and Classes.move_is_valid((player.player_x + 10,
                                                                                      player.player_y),
                                                                                     (0, width - 75),
                                                                                     (0, height - 75)):
                            for event in pygame.event.get():
                                pass
                            Classes.movement(10, 0, player_sprite, items, player, level, screen)
                    elif event.key == pygame.K_DOWN:
                        while event.type == pygame.KEYDOWN and Classes.move_is_valid((player.player_x,
                                                                                      player.player_y + 10),
                                                                                     (0, width - 75),
                                                                                     (0, height - 75)):
                            for event in pygame.event.get():
                                pass
                            Classes.movement(0, 10, player_sprite, items, player, level, screen)
                    elif event.key == pygame.K_UP:
                        while event.type == pygame.KEYDOWN and Classes.move_is_valid((player.player_x,
                                                                                      player.player_y - 10),
                                                                                     (0, width - 75),
                                                                                     (0, height - 75)):
                            for event in pygame.event.get():
                                pass
                            Classes.movement(0, -10, player_sprite, items, player, level, screen)
            pygame.display.flip()

    pygame.quit()
    sys.exit(app.exec_())
