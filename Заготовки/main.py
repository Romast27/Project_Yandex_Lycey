import sys
import time
import sqlite3

import pygame
from PyQt5.QtWidgets import QApplication

import Classes
import Authorize


if __name__ == '__main__':
    app = QApplication(sys.argv)
    authorizing = Authorize.Authorize()
    authorizing.show()
    if not authorizing.exec_() and authorizing.authorized:
        num_level = authorizing.num_level
        num_level = 3
        id = authorizing.id[0]
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

        running1 = True
        while running1:
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN and Classes.is_on_click(event.pos, 700, 400, 1300, 650):
                    running1 = False
                    break
                if event.type == pygame.MOUSEBUTTONDOWN and Classes.move_is_valid(event.pos, (1840, 1910), (10, 80)):
                    pygame.quit()
                    running1 = False
                    num_level = 0

        screen.fill((255, 255, 255))
        k = 1
        robot = pygame.sprite.Group()
        dialog = pygame.sprite.Group()
        menu = pygame.sprite.Group()
        robot_image = Classes.Image('robot.png', (50, 380), (426, 469), -1, robot)
        dialog_image = Classes.Image('dialog.png', (500, 500), (1220, 350), -1, robot)
        background = Classes.Image('background.jpg', (0, 0), (1920, 1080), None, menu)
        menu.draw(screen)
        buttons.draw(screen)
        robot.draw(screen)
        with open('data\Texts\Первый диалог.txt', 'r', encoding='utf8') as file:
            text_dialog = file.read()
            text_dialog = text_dialog.split('\n')
        Classes.draw_text(' '.join(text_dialog[:4]), 35, 545, 510, 55, 35)
        pygame.display.flip()
        running2 = True
        while running2:
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN and Classes.move_is_valid(event.pos, (1840, 1910), (10, 80)):
                    pygame.quit()
                    running2 = False
                    num_level = 0
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if k == 1:
                        robot.draw(screen)
                        Classes.draw_text(' '.join(text_dialog[4:9]), 35, 545, 510, 55, 35)
                        pygame.display.flip()
                        k = 2
                    elif k == 2:
                        robot.draw(screen)
                        Classes.draw_text(' '.join(text_dialog[9:]), 35, 545, 510, 55, 35)
                        pygame.display.flip()
                        k = 3
                    elif k == 3:
                        running2 = False

#--------First level----------
        if num_level == 1:
            flag_book = False
            text = []
            screen.fill((255, 255, 255))
            player = Classes.Player(screen, (700, 500), None, player_sprite)
            level = Classes.Level(screen, 'data\level_1.txt', 20, 11, 100)
            button_book = Classes.Image('book_button.png', (1860, 70), (50, 50), -1, buttons)
            cross = Classes.Image('cross.png', (1700, 100), (50, 50), -1, book)
            arrow = Classes.Image('arrow.png', (1500, 860), (70, 50), -1, book)
            level.draw_level_ground('floor1.png', 'dec1.png', player, player_sprite)
            for item in ((113, 175), (813, 275), (1213, 475), (813, 875), (1813, 475)):
                image_tv = Classes.Image('TV.png', (item[0], item[1]),
                                         (75, 75), None, level.decoration_sprites)
            for item in ((413, 75), (1013, 75), (1513, 75), (1713, 375)):
                image_pc = Classes.Image('comp.png', (item[0], item[1]),
                                         (75, 75), None, level.decoration_sprites)
            for item in ((513, 375),):
                image_pc2 = Classes.Image('fra.png', (item[0], item[1]),
                                          (75, 75), None, level.decoration_sprites)
            for item in ((1770, 930), (1802, 855)):
                image_rad = Classes.Image('radiation.png', (item[0], item[1]),
                                          (75, 75), None, level.decoration_sprites)
            for item in ((1845, 1005), (1845, 930), (1770, 1005)):
                image_el = Classes.Image('elec.png', (item[0], item[1]),
                                         (75, 75), None, level.decoration_sprites)
            image_pers = Classes.Image('pers1.png', (420, 480),
                                       (85, 100), None, level.pers_1)
            image_pers = Classes.Image('pers2.png', (1690, 980),
                                       (75, 101), None, level.pers_2)
            image_pers = Classes.Image('pers3.png', (1690, 980),
                                       (75, 101), None, level.pers_3)            
            level.decoration_sprites.draw(screen)
            level.pers_1.draw(screen)
            level.pers_2.draw(screen)
            level.pers_3.draw(screen)
            buttons.draw(screen)
            player_sprite.draw(screen)
            next_level.draw(screen)
            pygame.display.flip()
            Classes.main_cycle(player, player_sprite, level, buttons, book, num_level, next_level, id)
            if player.flag_next_level:
                num_level = 2
#--------First level----------

#--------Second level----------
        if num_level == 2:
            screen.fill((255, 255, 255))
            flag_book = False
            text = []
            player_sprite = pygame.sprite.Group()
            player = Classes.Player(screen, (0, 0), None, player_sprite)
            level = Classes.Level(screen, 'data\Texts\level_2.txt', 20, 11, 100)
            button_book = Classes.Image('book_button.png', (1860, 70), (50, 50), -1, buttons)
            cross = Classes.Image('cross.png', (1700, 100), (50, 50), -1, book)
            arrow = Classes.Image('arrow.png', (1500, 860), (70, 50), -1, book)
            level.draw_level_ground('ground sprite.png', 'dec.png', player, player_sprite)
            for item in ((113, 175), (713, 175), (1313, 175), (513, 475), (1813, 475)):
                image_tv = Classes.Image('TV.png', (item[0], item[1]),
                                         (75, 75), None, level.decoration_sprites)
            for item in ((413, 175), (1013, 175), (1613, 175), (1713, 475), (1413, 75)):
                image_pc = Classes.Image('comp.png', (item[0], item[1]),
                                         (75, 75), None, level.decoration_sprites)
            for item in ((413, 375), (1513, 75)):
                image_pc2 = Classes.Image('fra.png', (item[0], item[1]),
                                          (75, 75), None, level.decoration_sprites)
            for item in ((1770, 930), (1802, 855)):
                image_rad = Classes.Image('radiation.png', (item[0], item[1]),
                                          (75, 75), None, level.decoration_sprites)
            for item in ((1845, 1005), (1845, 930), (1770, 1005)):
                image_el = Classes.Image('elec.png', (item[0], item[1]),
                                         (75, 75), None, level.decoration_sprites)
            image_pers = Classes.Image('pers4.png', (420, 480),
                                       (75, 111), None, level.pers_1)
            image_pers = Classes.Image('pers5.png', (1690, 980),
                                       (75, 101), None, level.pers_2)
            image_pers = Classes.Image('pers6.png', (1463, 175),
                                       (75, 101), None, level.pers_3)
            level.decoration_sprites.draw(screen)
            level.pers_1.draw(screen)
            level.pers_2.draw(screen)
            level.pers_3.draw(screen)
            buttons.draw(screen)
            player_sprite.draw(screen)
            next_level.draw(screen)
            pygame.display.flip()
            dict_res = {1: False, 2: False}
            # Classes.main_cycle(player, player_sprite, level, buttons, book, num_level, next_level, id)
            if player.flag_next_level:
                num_level = 3
# --------Second level----------

#---------Boss level----------
        if num_level == 3:
            screen.fill((255, 255, 255))
            boss = pygame.sprite.Group()
            task = pygame.sprite.Group()
            task_1 = pygame.sprite.Group()
            task_2 = pygame.sprite.Group()
            task_3 = pygame.sprite.Group()
            player_sprite = pygame.sprite.Group()
            player = Classes.Player(screen, (0, 0), None, player_sprite)            
            boss_image = Classes.Image('boss2.png', (566, 100), (788, 572), -1, boss)
            level = Classes.Level(screen, 'data\Texts\level_boss.txt', 20, 11, 100)
            image_task = Classes.Image('dialog_task.png', (215, 250), (430, 700), -1, task_1)
            image_task = Classes.Image('dialog_task.png', (730, 250), (430, 700), -1, task_2)
            image_task = Classes.Image('dialog_task.png', (1260, 250), (430, 700), -1, task_3)
            with open('data\Texts\Текста диалогов.txt', mode='r', encoding='utf8') as file:
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
            con = sqlite3.connect("project_db.sqlite")
            cur = con.cursor()
            cur.execute("UPDATE Players SET current_level=? WHERE id=?", (current_level := num_level, id := id))
            con.commit()
            con.close()            
            start = time.time()
            Classes.boss_func()
            end = time.time()
            time_boss = end - start
            con = sqlite3.connect("project_db.sqlite")
            cur = con.cursor()
            cur.execute("UPDATE Players SET time_boss=? WHERE id=?", (time_boss := time_boss, id := id))
            con.commit()
            con.close()
#---------Boss level----------


    pygame.quit()
    sys.exit(app.exec_())
