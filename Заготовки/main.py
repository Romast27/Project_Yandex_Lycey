import sys

import pygame
from PyQt5.QtWidgets import QApplication

import Classes
import Authorize


if __name__ == '__main__':
    # app = QApplication(sys.argv)
    # authorizing = Authorize.Authorize()
    # authorizing.show()
    # if not authorizing.exec_() and authorizing.authorized:
    if True:
        running = True
        turn = True
        break_while = False
        width, height = 1920, 1080
        pygame.init()
        screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        screen.fill((255, 255, 255))

        menu_ground = pygame.sprite.Group()
        player_sprite = pygame.sprite.Group()
        buttons = pygame.sprite.Group()
        ground_sprites = pygame.sprite.Group()
        book = pygame.sprite.Group()
        close_button = Classes.Image('close_button.png', (1860, 10), (50, 50), None, buttons)
        background = Classes.Image('background.jpg', (0, 0), (1920, 1080), None, menu_ground)
        start_text = Classes.Image('start.png', (680, 400), (600, 170), None, menu_ground)
        menu_ground.draw(screen)
        buttons.draw(screen)
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
        flag_book = False
        text = []
        dict_books = {1: '', 2: 'Знакомство с циклом while.txt'}
        player = Classes.Player(screen, (0, 0), None, player_sprite)
        level = Classes.Level(screen, 'level.txt', 20, 11, 100)
        button_book = Classes.Image('book_button.png', (1860, 70), (50, 50), -1, buttons)
        cross = Classes.Image('cross.png', (1700, 100), (50, 50), -1, book)
        arrow = Classes.Image('arrow.png', (1500, 860), (70, 50), -1, book)
        level.draw_level_ground('ground sprite.png', 'dec.png', player, player_sprite)
        buttons.draw(screen)
        player_sprite.draw(screen)
        while running:
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if Classes.move_is_valid(event.pos, (1860, 1910), (10, 60)):
                        running = False
                    if Classes.move_is_valid(event.pos, (1450, 1586), (900, 944)) and player.flag_dialog:
                        print(10)
                    if Classes.move_is_valid(event.pos, (1860, 1910), (70, 120)):
                        name_book = dict_books[2]
                        with open(name_book, encoding="utf8", mode='r') as f:
                            data = f.read()
                            text = data.split('\n')
                        remaining_text = Classes.open_book(book, text)
                        flag_book = True
                        break_loop = False
                        while not break_loop:
                            for event in pygame.event.get():
                                if event.type == pygame.MOUSEBUTTONDOWN:
                                    if Classes.move_is_valid(event.pos, (1700, 1750), (100, 150)):
                                        break_loop = True
                                        break
                                    if Classes.move_is_valid(event.pos, (1500, 1570), (860, 910)):
                                        if remaining_text:
                                            remaining_text = Classes.open_book(book, remaining_text)
                    if Classes.move_is_valid(event.pos, (1700, 1750), (100, 150)) and flag_book:
                        flag_book = False
                        screen.fill((255, 255, 255))
                        level.ground_sprites.draw(screen)
                        level.decoration_sprites.draw(screen)
                        player_sprite.draw(screen)
                        buttons.draw(screen)
                        pygame.display.flip()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        while event.type == pygame.KEYDOWN and Classes.move_is_valid((player.player_x - 10,
                                                                                      player.player_y),
                                                                                     (0, width - 100),
                                                                                     (0, height - 100)):
                            for event in pygame.event.get():
                                pass
                            Classes.movement(-30, 0, player_sprite, buttons, player, level, screen)
                    elif event.key == pygame.K_RIGHT:
                        while event.type == pygame.KEYDOWN and Classes.move_is_valid((player.player_x + 10,
                                                                                      player.player_y),
                                                                                     (0, width - 100),
                                                                                     (0, height - 100)):
                            for event in pygame.event.get():
                                pass
                            Classes.movement(30, 0, player_sprite, buttons, player, level, screen)
                    elif event.key == pygame.K_DOWN:
                        while event.type == pygame.KEYDOWN and Classes.move_is_valid((player.player_x,
                                                                                      player.player_y + 10),
                                                                                     (0, width - 100),
                                                                                     (0, height - 100)):
                            for event in pygame.event.get():
                                pass
                            Classes.movement(0, 30, player_sprite, buttons, player, level, screen)
                    elif event.key == pygame.K_UP:
                        while event.type == pygame.KEYDOWN and Classes.move_is_valid((player.player_x,
                                                                                      player.player_y - 10),
                                                                                     (0, width - 100),
                                                                                     (0, height - 100)):
                            for event in pygame.event.get():
                                pass
                            Classes.movement(0, -30, player_sprite, buttons, player, level, screen)
            pygame.display.flip()

    pygame.quit()
    sys.exit(app.exec_())
