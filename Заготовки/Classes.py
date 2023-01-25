import os
import sys
from time import sleep

from PyQt5.QtWidgets import QApplication
from PyQt5 import QtCore
import pygame
import sqlite3

import Answering_question
import Testing_files
import Authorize



dict_res = {}
turn = True
with open('data\Texts\Текста диалогов.txt', mode='r', encoding='utf8') as file:
    text_dialog = file.read()
    text_dialog = text_dialog.split('\n')
pygame.init()
size = width, height = 1920, 1080
screen = pygame.display.set_mode(size)
screen.fill((255, 255, 255))
horizontal_borders = pygame.sprite.Group()
vertical_borders = pygame.sprite.Group()


def is_on_click(pos, x, y, w, h):
    return x < pos[0] < x + w and y < pos[1] < y + h


def move_is_valid(pos, arg1, arg2):
    return arg1[0] <= pos[0] <= arg1[1] and arg2[0] <= pos[1] <= arg2[1]


def movement(x, y, player_sprite, items, player, level, screen, next_level, dict_res, num_level):
    global turn
    if turn and x == -30:
        player.image = pygame.transform.flip(player.image, True, False)
        turn = False
    elif not turn and x == 30:
        player.image = pygame.transform.flip(player.image, True, False)
        turn = True
    sleep(0.05)
    player.player_move(x, y, level, dict_res, num_level)
    if not player.flag_dialog:
        screen.fill(pygame.Color((255, 255, 255)))
        level.ground_sprites.draw(screen)
        level.decoration_sprites.draw(screen)
        player_sprite.draw(screen)
        level.pers_1.draw(screen)
        level.pers_2.draw(screen)
        level.pers_3.draw(screen)
        items.draw(screen)
        next_level.draw(screen)
        pygame.display.flip()


def load_image(name, colorkey=None):
    fullname = os.path.join('data\Images', name)
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    if colorkey is not None:
        image = image.convert()
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    else:
        image = image.convert_alpha()
    return image


def draw_text(text, font, text_x, text_y, len_st, dif_y):
    remaining_st = ''
    st = ''
    k = 0
    text = text.split(' ')
    font = pygame.font.SysFont("Segoe UI Black", font)
    for word in text:
        if k > 30 and text_x != 970:
            text_x = 970
            text_y = 110
            k = 0
        elif k > 28 and text_x == 970:
            remaining_st += word + ' '
        elif len(st + ' ' + word) > len_st and not (k > 30 and text_x != 970) and not (k > 28 and text_x == 970):
            string = font.render(st, False, (0, 0, 0))
            text_y += dif_y
            screen.blit(string, (text_x, text_y))
            st = ''
            k += 1
        st += ' ' + word
    if st and k < 28:
        string = font.render(st, False, (0, 0, 0))
        text_y += dif_y
        screen.blit(string, (text_x, text_y))
    pygame.display.flip()


def make_dialog(dialog_text):
    dialog = pygame.sprite.Group()
    image = Image('dialog.png', (250, 500),
                  (1420, 480), -1, dialog)
    image = Image('next.png', (1450, 900),
                  (136, 44), -1, dialog)
    image = Image('close.png', (1250, 900),
                  (150, 44), -1, dialog)
    dialog.draw(screen)
    draw_text(dialog_text, 45, 280, 530, 50, 40)
    pygame.display.flip()


def open_book(book, text):
    screen.fill((211, 10, 17), (240, 120, 1400, 800))
    screen.fill((255, 193, 83), (270, 130, 1340, 780))
    screen.fill((255, 201, 106), (280, 130, 1320, 780))
    screen.fill((255, 212, 135), (290, 130, 1300, 780))
    screen.fill((255, 221, 161), (300, 130, 1280, 780))
    screen.fill((237, 197, 126), (920, 130, 40, 780))
    screen.fill((215, 173, 99), (930, 130, 20, 780))
    book.draw(screen)
    flag = True
    remaining_st = ''
    remaining_text = []
    text_x = 310
    text_y = 110
    k = 0
    font = pygame.font.SysFont("Segoe UI Black", 17)
    for num, item in enumerate(text):
        if not flag:
            break
        item = item.split(' ')
        k += 1
        st = ''
        for word in item:
            if k > 30 and text_x != 970:
                text_x = 970
                text_y = 110
                k = 0
            elif k > 28 and text_x == 970:
                remaining_st += word + ' '
                flag = False
            elif len(st + ' ' + word) > 60 and not (k > 30 and text_x != 970) and not (k > 28 and text_x == 970):
                string = font.render(st, False, (0, 0, 0))
                text_y += 25
                screen.blit(string, (text_x, text_y))
                st = ''
                k += 1
            st += ' ' + word
        if st and k < 28:
            string = font.render(st, False, (0, 0, 0))
            text_y += 25
            screen.blit(string, (text_x, text_y))
    pygame.display.flip()
    if remaining_st:
        remaining_text.append(remaining_st)
    remaining_text.extend(text[num:])
    if len(remaining_text) == 1:
        remaining_text = []
    return remaining_text


def draw_game(screen, level, player_sprite, buttons, next_level):
    screen.fill(pygame.Color((255, 255, 255)))
    level.ground_sprites.draw(screen)
    level.decoration_sprites.draw(screen)
    player_sprite.draw(screen)
    level.pers_1.draw(screen)
    level.pers_2.draw(screen)
    level.pers_3.draw(screen)
    buttons.draw(screen)
    next_level.draw(screen)
    pygame.display.flip()


def boss_func():
    dict_task = {1: False, 2: False, 3: False}
    running = True
    broken = pygame.sprite.Group()
    while running:
        if all(dict_task.values()):
            print('Победа')
            running = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if move_is_valid(event.pos, (1840, 1910), (10, 60)):
                    pygame.quit()
                    running = False
                    num_level = 0
                elif move_is_valid(event.pos, (450, 586), (875, 919)) and not dict_task[1]:
                    ex_4 = Testing_files.Example(87178291200)
                    ex_4.show()
                    if ex_4.finished:
                        dict_task[1] = True
                        image_broken = Image('dialog_task_broken.png', (215, 250), (430, 700), -1, broken)
                elif move_is_valid(event.pos, (965, 1101), (875, 919)) and not dict_task[2]:
                    ex_5 = Testing_files.Example(3927)
                    ex_5.show()
                    if ex_5.finished:
                        dict_task[2] = True
                        image_broken = Image('dialog_task_broken.png', (730, 250), (430, 700), -1, broken)
                elif move_is_valid(event.pos, (1505, 1641), (875, 919)) and not dict_task[3]:
                    ex_6 = Testing_files.Example(23)
                    ex_6.show()
                    if ex_6.finished:
                        dict_task[3] = True
                        image_broken = Image('dialog_task_broken.png', (1260, 250), (430, 700), -1, broken)
        broken.draw(screen)
        pygame.display.flip()


def main_cycle(player, player_sprite, level, buttons, book, num_level, next_level, id):
    global dict_res
    con = sqlite3.connect("project_db.sqlite")
    cur = con.cursor()
    cur.execute("UPDATE Players SET current_level=? WHERE id=?", (current_level := num_level, id := id))
    con.commit()
    con.close()    
    dict_res = {1: False, 2: False, 3: False}
    running = True
    while running:
        if player.flag_next_level:
            running = False
            break        
        for event in pygame.event.get():
            print(player.running_level)
            if event.type == pygame.MOUSEBUTTONDOWN:
                if move_is_valid(event.pos, (1250, 1400), (900, 944)):
                    player.flag_dialog = False
                    draw_game(screen, level, player_sprite, buttons, next_level)
                if move_is_valid(event.pos, (1450, 1586), (900, 944)) and player.flag_dialog:
                    if player.running_level == 1:
                        if num_level == 1:
                            answering = Answering_question.AnsweringQuestion('print()', 'Напишите команду, которая используется для вывода на экран')
                            answering.show()
                            if not answering.exec_() and answering.finished:
                                dict_res[1] = True
                                draw_game(screen, level, player_sprite, buttons, next_level)
                                player.flag_dialog = False
                        if num_level == 2:
                            answering = Answering_question.AnsweringQuestion('while n != 0:', 'Напишите условия цикла while (вместе с самим while) удовлетворяющее условию задачи')
                            answering.show()
                            if not answering.exec_() and answering.finished:
                                dict_res[1] = True
                                draw_game(screen, level, player_sprite, buttons, next_level)
                                player.flag_dialog = False
                    elif player.running_level == 2:
                        if num_level == 1:
                            answering = Answering_question.AnsweringQuestion('input()', 'Напишите команду, которая используется для ввода данных с клавиатуры')
                            answering.show()
                            if not answering.exec_() and answering.finished:
                                dict_res[1] = True
                                draw_game(screen, level, player_sprite, buttons, next_level)
                                player.flag_dialog = False
                        if num_level == 2:
                            answering = Answering_question.AnsweringQuestion('n += 1', 'Напишите сокращенную форму записи оператора присваивание переменной n и числа 1')
                            answering.show()
                            if not answering.exec_() and answering.finished:
                                dict_res[2] = True
                                draw_game(screen, level, player_sprite, buttons, next_level)
                                player.flag_dialog = False
                    elif player.running_level == 3:
                        if num_level == 1:
                            answering = Answering_question.AnsweringQuestion('int()', 'Напишите функцию, которая в качестве аргумента получает строку, а на выходе возвращает число')
                            answering.show()
                            if not answering.exec_() and answering.finished:
                                dict_res[3] = True
                                draw_game(screen, level, player_sprite, buttons, next_level)
                                player.flag_dialog = False
                        if num_level == 2:
                            answering = Answering_question.AnsweringQuestion('for i in range(10, 1, -1):', 'Напишите цикл от 10 до 1')
                            answering.show()
                            if not answering.exec_() and answering.finished:
                                dict_res[3] = True
                                draw_game(screen, level, player_sprite, buttons, next_level)
                                player.flag_dialog = False
                if move_is_valid(event.pos, (1860, 1910), (10, 60)):
                    pygame.quit()
                    running = False
                    num_level = 0
                if move_is_valid(event.pos, (1860, 1910), (70, 120)) and not player.flag_dialog:
                    name_book = f'data\Texts\Книга_№2.txt'
                    with open(name_book, encoding="utf8", mode='r') as f:
                        data = f.read()
                        text = data.split('\n')
                    remaining_text = open_book(book, text)
                    flag_book = True
                    break_loop = False
                    while not break_loop:
                        for event in pygame.event.get():
                            if event.type == pygame.MOUSEBUTTONDOWN:
                                if move_is_valid(event.pos, (1700, 1750), (100, 150)):
                                    break_loop = True
                                    break
                                if move_is_valid(event.pos, (1500, 1570), (860, 910)):
                                    if remaining_text:
                                        remaining_text = open_book(book, remaining_text)
                if move_is_valid(event.pos, (1700, 1750), (100, 150)) and flag_book and not player.flag_dialog:
                    flag_book = False
                    screen.fill((255, 255, 255))
                    level.ground_sprites.draw(screen)
                    level.decoration_sprites.draw(screen)
                    player_sprite.draw(screen)
                    buttons.draw(screen)
                    level.pers_1.draw(screen)
                    level.pers_2.draw(screen)
                    level.pers_3.draw(screen)
                    next_level.draw(screen)
                    pygame.display.flip()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    while event.type == pygame.KEYDOWN and move_is_valid((player.player_x - 10,
                                                                                  player.player_y),
                                                                                 (0, width - 100),
                                                                                 (0,
                                                                                  height - 100)) and not player.flag_dialog:
                        for event in pygame.event.get():
                            pass
                        movement(-30, 0, player_sprite, buttons, player, level, screen, next_level, dict_res, num_level)
                        if player.flag_dialog:
                            break
                elif event.key == pygame.K_RIGHT:
                    while event.type == pygame.KEYDOWN and move_is_valid((player.player_x + 10,
                                                                                  player.player_y),
                                                                                 (0, width - 100),
                                                                                 (0,
                                                                                  height - 100)) and not player.flag_dialog:
                        for event in pygame.event.get():
                            pass
                        movement(30, 0, player_sprite, buttons, player, level, screen, next_level, dict_res, num_level)
                        if player.flag_dialog:
                            break
                elif event.key == pygame.K_DOWN:
                    while event.type == pygame.KEYDOWN and move_is_valid((player.player_x,
                                                                                  player.player_y + 10),
                                                                                 (0, width - 100),
                                                                                 (0,
                                                                                  height - 100)) and not player.flag_dialog:
                        for event in pygame.event.get():
                            pass
                        movement(0, 30, player_sprite, buttons, player, level, screen, next_level, dict_res, num_level)
                        if player.flag_dialog:
                            break
                elif event.key == pygame.K_UP:
                    while event.type == pygame.KEYDOWN and move_is_valid((player.player_x,
                                                                                  player.player_y - 10),
                                                                                 (0, width - 100),
                                                                                 (0,
                                                                                  height - 100)) and not player.flag_dialog:
                        for event in pygame.event.get():
                            pass
                        movement(0, -30, player_sprite, buttons, player, level, screen, next_level, dict_res, num_level)
                        if player.flag_dialog:
                            break


class Level:
    def __init__(self, game_screen, ground_file_name, level_width=5, level_height=5, cell_size=20):
        self.screen = game_screen
        self.ground_file = list(map(lambda x: x.strip('\n'), open(ground_file_name).readlines()))
        self.width = level_width
        self.height = level_height
        self.cell_size = cell_size
        self.ground_sprites = pygame.sprite.Group()
        self.decoration_sprites = pygame.sprite.Group()
        self.pers_1 = pygame.sprite.Group()
        self.pers_2 = pygame.sprite.Group()
        self.pers_3 = pygame.sprite.Group()

    def draw_level_ground(self, ground_sprite, decorations_sprite, player, player_sprite):
        for u in range(self.width):
            for i in range(self.height):
                try:
                    if self.ground_file[i][u] == '#':
                        image_gr = Image(ground_sprite, (self.cell_size * u, self.cell_size * i),
                                         (self.cell_size, self.cell_size), None, self.ground_sprites)
                    if self.ground_file[i][u] == '0':
                        image_gr = Image(ground_sprite, (self.cell_size * u, self.cell_size * i),
                                         (self.cell_size, self.cell_size), None, self.ground_sprites)
                        image_dec = Image(decorations_sprite, (self.cell_size * u, self.cell_size * i),
                                          (self.cell_size, self.cell_size), -1, self.decoration_sprites)
                    if self.ground_file[i][u] == '@':
                        image_gr = Image(ground_sprite, (self.cell_size * u, self.cell_size * i),
                                         (self.cell_size, self.cell_size), None, self.ground_sprites)
                        player.player_x = self.cell_size * u
                        player.player_y = self.cell_size * i
                        player.rect = player.image.get_rect()
                        player.rect.x = self.cell_size * u
                        player.rect.y = self.cell_size * i
                        player_sprite.draw(self.screen)
                    if self.ground_file[i][u] == '-':
                        screen.fill(pygame.Color((0, 0, 0)), (self.cell_size * u, self.cell_size * i,
                                                            self.cell_size, self.cell_size))
                except IndexError:
                    pass
        self.ground_sprites.draw(self.screen)
        self.decoration_sprites.draw(self.screen)
        self.pers_1.draw(self.screen)
        self.pers_2.draw(self.screen)


class Player(pygame.sprite.Sprite):
    image = load_image('pers.png')

    def __init__(self, game_screen, pos, game_board, *group):
        super().__init__(*group)
        self.image = pygame.transform.scale(Player.image, (75, 100))
        self.player_x = pos[0]
        self.player_y = pos[1]
        self.game_board = game_board
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]
        self.game_screen = game_screen
        self.flag_dialog = False
        self.flag_next_level = False
        self.running_level = None
        self.mask = pygame.mask.from_surface(self.image)

    def player_move(self, dif_x, dif_y, level, dict_res, num_level):
        self.player_y += dif_y
        self.player_x += dif_x
        self.rect = self.image.get_rect()
        self.rect.x = self.player_x
        self.rect.y = self.player_y
        if move_is_valid((self.player_x, self.player_y), (810, 996), (20, 60)) and all(dict_res.values()):
            self.flag_next_level = True
        if pygame.sprite.spritecollideany(self, level.decoration_sprites):
            self.player_y -= dif_y
            self.player_x -= dif_x
            self.rect = self.image.get_rect()
            self.rect.x = self.player_x
            self.rect.y = self.player_y
        if pygame.sprite.spritecollideany(self, level.pers_1) and not dict_res[1] and not self.flag_dialog:
            self.player_y -= dif_y
            self.player_x -= dif_x
            self.rect = self.image.get_rect()
            self.rect.x = self.player_x
            self.rect.y = self.player_y
            make_dialog(text_dialog[(num_level - 1) * 3])
            self.flag_dialog = True
            self.running_level = 1
            return
        if pygame.sprite.spritecollideany(self, level.pers_2) and not dict_res[2] and not self.flag_dialog:
            self.player_y -= dif_y
            self.player_x -= dif_x
            self.rect = self.image.get_rect()
            self.rect.x = self.player_x
            self.rect.y = self.player_y
            make_dialog(text_dialog[(num_level - 1) * 3 + 1])
            self.flag_dialog = True
            self.running_level = 2
            return
        if pygame.sprite.spritecollideany(self, level.pers_3) and not dict_res[3] and not self.flag_dialog:
            self.player_y -= dif_y
            self.player_x -= dif_x
            self.rect = self.image.get_rect()
            self.rect.x = self.player_x
            self.rect.y = self.player_y
            make_dialog(text_dialog[(num_level - 1) * 3 + 2])
            self.flag_dialog = True
            self.running_level = 3
            return        
        self.flag_dialog = False


class Image(pygame.sprite.Sprite):
    def __init__(self, name_image, pos, size, colorkey, *group):
        super().__init__(*group)
        image = load_image(name_image, colorkey)
        self.image = pygame.transform.scale(image, size)
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]
