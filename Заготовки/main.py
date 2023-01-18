import sys
import time

import pygame
from PyQt5.QtWidgets import QApplication

import Classes
import Authorize
import Testing_files


if __name__ == '__main__':
    app = QApplication(sys.argv)
    authorizing = Authorize.Authorize()
    authorizing.show()
    if not authorizing.exec_() and authorizing.authorized:
        id = authorizing.id
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
        next_level = pygame.sprite.Group()
        close_button = Classes.Image('close_button.png', (1860, 10), (50, 50), None, buttons)
        background = Classes.Image('background.jpg', (0, 0), (1920, 1080), None, menu_ground)
        start_text = Classes.Image('start.png', (680, 400), (600, 170), None, menu_ground)
        next_level_image = Classes.Image('next_level.png', (810, 30), (186, 75), None, next_level)
        menu_ground.draw(screen)
        buttons.draw(screen)
        pygame.display.flip()

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                if event.type == pygame.MOUSEBUTTONDOWN and Classes.is_on_click(event.pos, 700, 400, 1300, 650):
                    break_while = True
                    break
                if event.type == pygame.MOUSEBUTTONDOWN and Classes.move_is_valid(event.pos, (1840, 1910), (10, 80)):
                    pygame.quit()
                else:
                    continue
            if break_while:
                break
        id = 2
        if id == 2:
            screen.fill((255, 255, 255))
            flag_book = False
            text = []
            player = Classes.Player(screen, (0, 0), None, player_sprite)
            level = Classes.Level(screen, 'data\level_2.txt', 20, 11, 100)
            button_book = Classes.Image('book_button.png', (1860, 70), (50, 50), -1, buttons)
            cross = Classes.Image('cross.png', (1700, 100), (50, 50), -1, book)
            arrow = Classes.Image('arrow.png', (1500, 860), (70, 50), -1, book)
            level.draw_level_ground('ground sprite.png', 'dec.png', player, player_sprite)
            for item in ((113, 75), (713, 75), (1313, 75), (513, 475), (1813, 475)):
                image_tv = Classes.Image('TV.png', (item[0], item[1]),
                                         (75, 75), None, level.decoration_sprites)
            for item in ((413, 75), (1013, 75), (1613, 75), (1713, 475)):
                image_pc = Classes.Image('comp.png', (item[0], item[1]),
                                         (75, 75), None, level.decoration_sprites)
            for item in ((413, 375), ):
                image_pc2 = Classes.Image('fra.png', (item[0], item[1]),
                                          (75, 75), None, level.decoration_sprites)
            for item in ((1770, 930), (1802, 855)):
                image_rad = Classes.Image('radiation.png', (item[0], item[1]),
                                          (75, 75), None, level.decoration_sprites)
            for item in ((1845, 1005), (1845, 930), (1770, 1005)):
                image_el = Classes.Image('elec.png', (item[0], item[1]),
                                         (75, 75), None, level.decoration_sprites)
            image_pers = Classes.Image('pers1.png', (420, 480),
                                       (75, 111), None, level.pers_1)
            image_pers = Classes.Image('pers2.png', (1690, 980),
                                       (75, 101), None, level.pers_2)
            level.decoration_sprites.draw(screen)
            level.pers_1.draw(screen)
            level.pers_2.draw(screen)
            buttons.draw(screen)
            player_sprite.draw(screen)
            next_level.draw(screen)
            Classes.main_cycle(player, player_sprite, level, buttons, book, 2, next_level, id)

            dict_task = {1: False, 2: False, 3: False}
            screen.fill((255, 255, 255))
            boss = pygame.sprite.Group()
            task = pygame.sprite.Group()
            task_1 = pygame.sprite.Group()
            task_2 = pygame.sprite.Group()
            task_3 = pygame.sprite.Group()
            boss_image = Classes.Image('boss2.png', (566, 100), (788, 572), -1, boss)
            level = Classes.Level(screen, 'data\level_boss.txt', 20, 11, 100)
            image_task = Classes.Image('dialog_task.png', (215, 250), (430, 700), -1, task_1)
            image_task = Classes.Image('dialog_task.png', (730, 250), (430, 700), -1, task_2)
            image_task = Classes.Image('dialog_task.png', (1260, 250), (430, 700), -1, task_3)
            with open('data\Текста диалогов2.txt', mode='r', encoding='utf8') as file:
                text_dialog = file.read()
                text_dialog = text_dialog.split('\n')
            text_1 = text_dialog[2]
            text_2 = text_dialog[3]
            text_3 = text_dialog[4]
            image_next = Classes.Image('next.png', (450, 875), (136, 44), -1, task)
            image_next = Classes.Image('next.png', (965, 875), (136, 44), -1, task)
            image_next = Classes.Image('next.png', (1505, 875), (136, 44), -1, task)
            level.draw_level_ground('ground sprite.png', 'dec.png', player, player_sprite)
            level.ground_sprites.draw(screen)
            level.decoration_sprites.draw(screen)
            boss.draw(screen)
            player_sprite.draw(screen)
            buttons.draw(screen)
            task_1.draw(screen)
            task_2.draw(screen)
            task_3.draw(screen)
            task.draw(screen)
            Classes.draw_text(text_1, 30, 245, 275, 20, 28)
            Classes.draw_text(text_2, 30, 760, 275, 20, 28)
            Classes.draw_text(text_3, 30, 1290, 275, 20, 28)
            pygame.display.flip()
            running = True
            while running:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if Classes.move_is_valid(event.pos, (1840, 1910), (10, 60)):
                            pygame.quit()
                        if Classes.move_is_valid(event.pos, (450, 586), (875, 919)) and not dict_task[1]:
                            app_1 = QApplication(sys.argv)
                            ex_1 = Testing_files.Example(87178291200)
                            ex_1.show()
                            if ex_1.finished:
                                dict_task[1] = True
                        if Classes.move_is_valid(event.pos, (965, 1101), (875, 919)) and not dict_task[2]:
                            app_2 = QApplication(sys.argv)
                            ex_2 = Testing_files.Example(3927)
                            ex_2.show()
                            if ex_2.finished:
                                dict_task[2] = True
                        if Classes.move_is_valid(event.pos, (1505, 1641), (875, 919)) and not dict_task[3]:
                            app_3 = QApplication(sys.argv)
                            ex_3 = Testing_files.Example(23)
                            ex_3.show()
                            if ex_3.finished:
                                dict_task[3] = True
                if all(dict_task.values()):
                    print('Победа')
                    break


    # pygame.quit()
    # sys.exit(app.exec_())
