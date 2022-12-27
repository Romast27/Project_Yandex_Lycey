import os
import sys

import pygame


turn = True
pygame.init()
size = width, height = 800, 800
screen = pygame.display.set_mode(size)
screen.fill((255, 255, 255))
player_sprite = pygame.sprite.Group()


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


class Player(pygame.sprite.Sprite):
    image = load_image('player.jpg', -1)

    def __init__(self, game_screen, pos, game_board, *group):
        super().__init__(*group)
        self.image = pygame.transform.scale(Player.image, (75, 75))
        self.game_screen = game_screen
        self.player_x = pos[0]
        self.player_y = pos[1]
        self.game_board = game_board
        self.rect = self.image.get_rect()
        self.rect.x = self.player_x
        self.rect.y = self.player_y
        self.list_items = []

    def player_move(self, dif_x, dif_y):
        self.game_screen.fill(pygame.Color('white'))
        self.player_y += dif_y
        self.player_x += dif_x
        self.rect = self.image.get_rect()
        self.rect.x = self.player_x
        self.rect.y = self.player_y

    def add_item(self, item):
        self.list_items.append(item)


class BackGround(pygame.sprite.Sprite):
    image = load_image('background.jpg')

    def __init__(self, *group):
        super().__init__(*group)
        self.image = pygame.transform.scale(BackGround.image, (1920, 1080))
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 0


class CloseButton(pygame.sprite.Sprite):
    image = load_image('close_button.png', -1)

    def __init__(self, *group):
        super().__init__(*group)
        self.image = pygame.transform.scale(CloseButton.image, (50, 50))
        self.rect = self.image.get_rect()
        self.rect.x = 1860
        self.rect.y = 10


class BeginText(pygame.sprite.Sprite):
    image = load_image('start.png')

    def __init__(self, *group):
        super().__init__(*group)
        self.image = pygame.transform.scale(BeginText.image, (600, 170))
        self.rect = self.image.get_rect()
        self.rect.x = 680
        self.rect.y = 400
