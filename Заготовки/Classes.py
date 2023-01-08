import os
import sys
from time import sleep

import pygame


turn = True
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


def movement(x, y, player_sprite, items, player, level, screen):
    global turn
    if turn and x == -30:
        player.image = pygame.transform.flip(player.image, True, False)
        turn = False
    elif not turn and x == 30:
        player.image = pygame.transform.flip(player.image, True, False)
        turn = True
    sleep(0.075)
    screen.fill(pygame.Color('white'))
    level.ground_sprites.draw(screen)
    level.decoration_sprites.draw(screen)
    player.player_move(x, y, level)
    player_sprite.draw(screen)
    level.personages.draw(screen)
    items.draw(screen)
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


class Level:
    def __init__(self, game_screen, ground_file_name, level_width=5, level_height=5, cell_size=20):
        self.screen = game_screen
        self.ground_file = list(map(lambda x: x.strip('\n'), open(ground_file_name).readlines()))
        self.width = level_width
        self.height = level_height
        self.cell_size = cell_size
        self.ground_sprites = pygame.sprite.Group()
        self.decoration_sprites = pygame.sprite.Group()
        self.personages = pygame.sprite.Group()

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
        for item in ((113, 75), (713, 75), (1313, 75), (513, 475), (1813, 475)):
            image_tv = Image('TV.png', (item[0], item[1]),
                             (75, 75), None, self.decoration_sprites)
        for item in ((413, 75), (1013, 75), (1613, 75), (1713, 475)):
            image_pc = Image('comp.png', (item[0], item[1]),
                             (75, 75), None, self.decoration_sprites)
        for item in ((413, 375), ):
            image_pc2 = Image('fra.png', (item[0], item[1]),
                              (75, 75), None, self.decoration_sprites)
        for item in ((1770, 930), (1802, 855)):
            image_rad = Image('radiation.png', (item[0], item[1]),
                              (75, 75), None, self.decoration_sprites)
        for item in ((1845, 1005), (1845, 930), (1770, 1005)):
            image_el = Image('elec.png', (item[0], item[1]),
                             (75, 75), None, self.decoration_sprites)
        image_pers = Image('pers1.png', (420, 480),
                           (75, 111), None, self.personages)
        image_pers = Image('pers1.png', (1690, 980),
                           (75, 101), None, self.personages)
        self.ground_sprites.draw(self.screen)
        self.decoration_sprites.draw(self.screen)
        self.personages.draw(self.screen)


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
        self.mask = pygame.mask.from_surface(self.image)

    def player_move(self, dif_x, dif_y, level):
        self.player_y += dif_y
        self.player_x += dif_x
        self.rect = self.image.get_rect()
        self.rect.x = self.player_x
        self.rect.y = self.player_y
        if pygame.sprite.spritecollideany(self, level.decoration_sprites):
            self.player_y -= dif_y
            self.player_x -= dif_x
            self.rect = self.image.get_rect()
            self.rect.x = self.player_x
            self.rect.y = self.player_y
            self.flag_dialog = False
        if pygame.sprite.spritecollideany(self, level.personages):
            self.dialog = pygame.sprite.Group()
            image_pers = Image('dialog.png', (250, 500),
                               (1420, 480), -1, self.dialog)
            image_pers = Image('next.png', (1450, 900),
                               (136, 44), -1, self.dialog)
            self.dialog.draw(screen)
            self.player_y -= dif_y
            self.player_x -= dif_x
            self.rect = self.image.get_rect()
            self.rect.x = self.player_x
            self.rect.y = self.player_y
            self.flag_dialog = True
        else:
            self.flag_dialog = False
            return


class Image(pygame.sprite.Sprite):
    def __init__(self, name_image, pos, size, colorkey, *group):
        super().__init__(*group)
        image = load_image(name_image, colorkey)
        self.image = pygame.transform.scale(image, size)
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]
