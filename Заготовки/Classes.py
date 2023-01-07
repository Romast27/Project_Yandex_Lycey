import os
import sys
from time import sleep

import pygame


turn = True
pygame.init()
size = width, height = 800, 800
screen = pygame.display.set_mode(size)
screen.fill((255, 255, 255))


def is_on_click(pos, x, y, w, h):
    return x < pos[0] < x + w and y < pos[1] < y + h


def move_is_valid(pos, arg1, arg2):
    return arg1[0] <= pos[0] <= arg1[1] and arg2[0] <= pos[1] <= arg2[1]


def movement(x, y, player_sprite, items, player, level, screen):
    global turn
    if turn and x == -10:
        player.image = pygame.transform.flip(player.image, True, False)
        turn = False
    elif not turn and x == 10:
        player.image = pygame.transform.flip(player.image, True, False)
        turn = True
    sleep(0.075)
    screen.fill(pygame.Color('white'))
    level.draw_level_ground('ground sprite.png', 'dec.png')
    player.player_move(x, y, level)
    player_sprite.draw(screen)
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
    st = ''
    remaining_text = []
    text_x = 310
    text_y = 110
    k = 0
    font = pygame.font.SysFont("Segoe UI Black", 17)
    for word in text:
        if len(st + ' ' + word) > 60 and not (k > 30 and text_x != 970) and not (k > 28 and text_x == 970):
            string = font.render(st, False, (0, 0, 0))
            text_y += 25
            screen.blit(string, (text_x, text_y))
            st = ''
            k += 1
        st += ' ' + word
        if k > 30 and text_x != 970:
            text_x = 970
            text_y = 110
            k = 0
        elif k > 28 and text_x == 970:
            remaining_text.append(word)
    if remaining_text:
        string = font.render(st, False, (0, 0, 0))
        text_y += 25
        screen.blit(string, (text_x, text_y))
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

    def draw_level_ground(self, ground_sprite, decorations_sprite):
        for u in range(self.width):
            for i in range(self.height):
                try:
                    if self.ground_file[i][u] == '#':
                        image_gr = Image(ground_sprite, (self.cell_size * u, self.cell_size * i),
                                         (50, 50), None, self.ground_sprites)
                    if self.ground_file[i][u] == '0':
                        image_gr = Image(ground_sprite, (self.cell_size * u, self.cell_size * i),
                                         (50, 50), None, self.ground_sprites)
                        image_dec = Image(decorations_sprite, (self.cell_size * u, self.cell_size * i),
                                          (50, 50), -1, self.decoration_sprites)
                    if self.ground_file[i][u] == '-':
                        screen.fill(pygame.Color('black'), (self.cell_size * u, self.cell_size * i,
                                                            self.cell_size, self.cell_size))
                except IndexError:
                    pass
        self.ground_sprites.draw(self.screen)
        self.decoration_sprites.draw(self.screen)


class Player(pygame.sprite.Sprite):
    image = load_image('player.jpg', -1)

    def __init__(self, game_screen, pos, game_board, *group):
        super().__init__(*group)
        self.image = pygame.transform.scale(Player.image, (50, 50))
        self.player_x = pos[0]
        self.player_y = pos[1]
        self.game_board = game_board
        self.rect = self.image.get_rect()
        self.rect.x = self.player_x
        self.rect.y = self.player_y
        self.game_screen = game_screen
        self.list_items = []
        self.mask = pygame.mask.from_surface(self.image)

    def player_move(self, dif_x, dif_y, level):
        self.player_y += dif_y
        self.player_x += dif_x
        self.rect = self.image.get_rect()
        self.rect.x = self.player_x
        self.rect.y = self.player_y
        if not pygame.sprite.spritecollideany(self, level.decoration_sprites):
            return
        else:
            self.player_y -= dif_y
            self.player_x -= dif_x
            self.rect = self.image.get_rect()
            self.rect.x = self.player_x
            self.rect.y = self.player_y

    def add_item(self, item):
        self.list_items.append(item)


class Image(pygame.sprite.Sprite):
    def __init__(self, name_image, pos, size, colorkey, *group):
        super().__init__(*group)
        image = load_image(name_image, colorkey)
        self.image = pygame.transform.scale(image, size)
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]
