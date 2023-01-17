import os
import sys
from time import sleep

from PyQt5.QtWidgets import QApplication
from PyQt5 import QtCore
import pygame
import sqlite3

import Answering_question
import Testing_files


turn = True
dict_res = {}
with open('data\Текста диалогов2.txt', mode='r', encoding='utf8') as file:
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


def movement(x, y, player_sprite, items, player, level, screen, next_level):
    global turn
    if turn and x == -30:
        player.image = pygame.transform.flip(player.image, True, False)
        turn = False
    elif not turn and x == 30:
        player.image = pygame.transform.flip(player.image, True, False)
        turn = True
    sleep(0.075)
    player.player_move(x, y, level)
    screen.fill(pygame.Color('white'))
    level.ground_sprites.draw(screen)
    level.decoration_sprites.draw(screen)
    player_sprite.draw(screen)
    level.pers_1.draw(screen)
    level.pers_2.draw(screen)
    items.draw(screen)
    next_level.draw(screen)
    pygame.display.flip()


def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
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


def draw_text(text, font):
    remaining_st = ''
    st = ''
    k = 0
    text = text.split(' ')
    font = pygame.font.SysFont("Segoe UI Black", font)
    text_x = 280
    text_y = 530
    for word in text:
        if k > 30 and text_x != 970:
            text_x = 970
            text_y = 110
            k = 0
        elif k > 28 and text_x == 970:
            remaining_st += word + ' '
        elif len(st + ' ' + word) > 50 and not (k > 30 and text_x != 970) and not (k > 28 and text_x == 970):
            string = font.render(st, False, (0, 0, 0))
            text_y += 40
            screen.blit(string, (text_x, text_y))
            st = ''
            k += 1
        st += ' ' + word
    if st and k < 28:
        string = font.render(st, False, (0, 0, 0))
        text_y += 40
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
    draw_text(dialog_text, 45)


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
    return remaining_text


def main_cycle(player, player_sprite, level, buttons, book, num_level, next_level, id):
    global dict_res
    dict_res = {1: False, 2: False}
    con = sqlite3.connect("project_db.sqlite")
    cur = con.cursor()
    cur.execute("UPDATE Players SET current_level=? WHERE id=?", (current_level:=num_level, id:=id))
    con.commit()
    con.close()
    running = True
    while running:
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if move_is_valid(event.pos, (1860, 1910), (10, 60)):
                    running = False
                    return True
                if move_is_valid(event.pos, (1860, 1910), (70, 120)):
                    name_book = 'data\Знакомство с циклом while.txt'
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
                if move_is_valid(event.pos, (1700, 1750), (100, 150)) and flag_book:
                    flag_book = False
                    screen.fill((255, 255, 255))
                    level.ground_sprites.draw(screen)
                    level.decoration_sprites.draw(screen)
                    player_sprite.draw(screen)
                    buttons.draw(screen)
                    level.pers_1.draw(screen)
                    level.pers_2.draw(screen)
                    next_level.draw(screen)
                    pygame.display.flip()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    while event.type == pygame.KEYDOWN and move_is_valid((player.player_x - 10,
                                                                          player.player_y),
                                                                         (0, width - 100),
                                                                         (0, height - 100)):
                        for event in pygame.event.get():
                            pass
                        movement(-30, 0, player_sprite, buttons, player, level, screen, next_level)
                        if player.flag_dialog:
                            break
                elif event.key == pygame.K_RIGHT:
                    while event.type == pygame.KEYDOWN and move_is_valid((player.player_x + 10,
                                                                          player.player_y),
                                                                         (0, width - 100),
                                                                         (0, height - 100)):
                        for event in pygame.event.get():
                            pass
                        movement(30, 0, player_sprite, buttons, player, level, screen, next_level)
                        if player.flag_dialog:
                            break
                elif event.key == pygame.K_DOWN:
                    while event.type == pygame.KEYDOWN and move_is_valid((player.player_x,
                                                                          player.player_y + 10),
                                                                         (0, width - 100),
                                                                         (0, height - 100)):
                        for event in pygame.event.get():
                            pass
                        movement(0, 30, player_sprite, buttons, player, level, screen, next_level)
                        if player.flag_dialog:
                            break
                elif event.key == pygame.K_UP:
                    while event.type == pygame.KEYDOWN and move_is_valid((player.player_x,
                                                                          player.player_y - 10),
                                                                         (0, width - 100),
                                                                         (0, height - 100)):
                        for event in pygame.event.get():
                            pass
                        movement(0, -30, player_sprite, buttons, player, level, screen, next_level)
                        if player.flag_dialog:
                            break
        pygame.display.flip()
        if player.flag_next_level:
            return True


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
                        screen.fill(pygame.Color('black'), (self.cell_size * u, self.cell_size * i,
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
        self.mask = pygame.mask.from_surface(self.image)

    def player_move(self, dif_x, dif_y, level):
        self.player_y += dif_y
        self.player_x += dif_x
        self.rect = self.image.get_rect()
        self.rect.x = self.player_x
        self.rect.y = self.player_y
        if move_is_valid((self.player_x, self.player_y), (810, 996), (20, 60)) and all(dict_res.items()):
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
            make_dialog(text_dialog[0])
            answer = '1, 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97'
            running = True
            while running:
                for event in pygame.event.get():
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if move_is_valid(event.pos, (1450, 1586), (900, 944)):
                            app = QApplication(sys.argv)
                            ex = Testing_files.Example(answer)
                            ex.show()
                            if ex.finished:
                                dict_res[1] = True
                                running = False
                        if move_is_valid(event.pos, (1250, 1400), (900, 944)):
                            running = False
            self.flag_dialog = True
            return
        if pygame.sprite.spritecollideany(self, level.pers_2) and not dict_res[2] and not self.flag_dialog:
            self.player_y -= dif_y
            self.player_x -= dif_x
            self.rect = self.image.get_rect()
            self.rect.x = self.player_x
            self.rect.y = self.player_y
            make_dialog(text_dialog[1])
            running = True
            while running:
                for event in pygame.event.get():
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if move_is_valid(event.pos, (1450, 1586), (900, 944)):
                            app = QApplication(sys.argv)
                            answering = Answering_question.AnsweringQuestion('break',
                                                                             'Как называется оператор прерывающий цикл?')
                            answering.show()
                            if not answering.exec_() and answering.finished:
                                dict_res[2] = True
                                running = False
                        if move_is_valid(event.pos, (1250, 1400), (900, 944)):
                            running = False
            self.flag_dialog = True
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
