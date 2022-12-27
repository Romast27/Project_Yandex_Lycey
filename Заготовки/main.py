import sys
import os
import time

import pygame
from PyQt5.QtWidgets import QApplication

import Player
import Authorize


def is_on_click(pos, x, y, w, h):
    if x < pos[0] < x + w and y < pos[1] < y + h:
        return True
    return False


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


def move_is_valid(pos, arg1, arg2):
    if arg1[0] <= pos[0] <= arg1[1] and arg2[0] <= pos[1] <= arg2[1]:
        return True
    else:
        return False


def movement(x, y, player):
    global turn
    if turn and x == -10:
        player.image = pygame.transform.flip(player.image, True, False)
        turn = False
    elif not turn and x == 10:
        player.image = pygame.transform.flip(player.image, True, False)
        turn = True
    time.sleep(0.075)
    player.player_move(x, y)
    player_sprite.draw(screen)
    items.draw(screen)
    pygame.display.flip()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    authorizing = Authorize.Authorize()
    authorizing.show()
    if not authorizing.exec_() and authorizing.authorized:
        width, height = 1920, 1080
        pygame.init()
        screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        screen.fill((255, 255, 255))
        back_ground = pygame.sprite.Group()
        player_sprite = pygame.sprite.Group()
        items = pygame.sprite.Group()
        running = True
        turn = True
        break_while = False
        btn = Player.CloseButton(items)
        bg = Player.BackGround(back_ground)
        text = Player.BeginText(back_ground)
        player = Player.Player(screen, (0, 0), None, player_sprite)
        back_ground.draw(screen)
        items.draw(screen)
        pygame.display.flip()
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN and is_on_click(event.pos, 700, 400, 1300, 650):
                    break_while = True
                    break
                if event.type == pygame.MOUSEBUTTONDOWN and move_is_valid(event.pos, (1840, 1910), (10, 80)):
                    running = False
                else:
                    continue
            if break_while:
                break
        while running:
            screen.fill((255, 255, 255))
            player_sprite.draw(screen)
            items.draw(screen)
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN and move_is_valid(event.pos, (1840, 1910), (10, 80)):
                    running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        while event.type == pygame.KEYDOWN and move_is_valid((player.player_x - 10, player.player_y),
                                                                             (0, width - 75), (0, height - 75)):
                            for event1 in pygame.event.get():
                                pass
                            movement(-10, 0, player)
                    elif event.key == pygame.K_RIGHT:
                        while event.type == pygame.KEYDOWN and move_is_valid((player.player_x + 10, player.player_y),
                                                                             (0, width - 75), (0, height - 75)):
                            for event1 in pygame.event.get():
                                pass
                            movement(10, 0, player)
                    elif event.key == pygame.K_DOWN:
                        while event.type == pygame.KEYDOWN and move_is_valid((player.player_x, player.player_y + 10),
                                                                             (0, width - 75), (0, height - 75)):
                            for event1 in pygame.event.get():
                                pass
                            movement(0, 10, player)
                    elif event.key == pygame.K_UP:
                        while event.type == pygame.KEYDOWN and move_is_valid((player.player_x, player.player_y - 10),
                                                                             (0, width - 75), (0, height - 75)):
                            for event1 in pygame.event.get():
                                pass
                            movement(0, -10, player)
            pygame.display.flip()
    pygame.quit()
    sys.exit(app.exec_())
