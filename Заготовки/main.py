import sys
from time import sleep

import pygame
from PyQt5.QtWidgets import QApplication

import Classes
import Authorize
import Testing_files
import Answering_question


turn = True
def is_on_click(pos, x, y, w, h):
    return x < pos[0] < x + w and y < pos[1] < y + h


def move_is_valid(pos, arg1, arg2):
    return arg1[0] <= pos[0] <= arg1[1] and arg2[0] <= pos[1] <= arg2[1]


def movement(x, y, player_sprite, items, player, level, screen, next_level, dict_res):
    global turn
    if turn and x == -30:
        player.image = pygame.transform.flip(player.image, True, False)
        turn = False
    elif not turn and x == 30:
        player.image = pygame.transform.flip(player.image, True, False)
        turn = True
    sleep(0.075)
    player.player_move(x, y, level, dict_res)
    if not player.flag_dialog:
        screen.fill(pygame.Color((255, 255, 255)))
        level.ground_sprites.draw(screen)
        level.decoration_sprites.draw(screen)
        player_sprite.draw(screen)
        level.pers_1.draw(screen)
        level.pers_2.draw(screen)
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
    return remaining_text


def boss_func():
    dict_task = {1: False, 2: False, 3: False}
    running = True
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
                if move_is_valid(event.pos, (450, 586), (875, 919)) and not dict_task[1]:
                    ex_4 = Testing_files.Example(87178291200)
                    ex_4.show()
                    if ex_4.finished:
                        dict_task[1] = True
                if move_is_valid(event.pos, (965, 1101), (875, 919)) and not dict_task[2]:
                    ex_5 = Testing_files.Example(3927)
                    ex_5.show()
                    if ex_5.finished:
                        dict_task[2] = True
                if move_is_valid(event.pos, (1505, 1641), (875, 919)) and not dict_task[3]:
                    ex_6 = Testing_files.Example(23)
                    ex_6.show()
                    if ex_6.finished:
                        dict_task[3] = True


if __name__ == '__main__':
    app = QApplication(sys.argv)
    #authorizing = Authorize.Authorize()
    #authorizing.show()
    #if not authorizing.exec_() and authorizing.authorized:
    #num_level = authorizing.num_level
    num_level = 2
    quit = False
    #id = authorizing.id[0]
    id = 1
    if True:
        turn = True
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
                if event.type == pygame.QUIT:
                    pygame.quit()
                if event.type == pygame.MOUSEBUTTONDOWN and is_on_click(event.pos, 700, 400, 1300, 650):
                    running1 = False
                    break
                if event.type == pygame.MOUSEBUTTONDOWN and move_is_valid(event.pos, (1840, 1910), (10, 80)):
                    pygame.quit()
                else:
                    continue
        if num_level == 1:
            screen.fill((255, 255, 255))
            flag_book = False
            text = []
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
            image_pers = Classes.Image('pers5.png', (420, 480),
                                       (85, 100), None, level.pers_1)
            image_pers = Classes.Image('pers6.png', (1690, 980),
                                       (75, 101), None, level.pers_2)
            level.decoration_sprites.draw(screen)
            level.pers_1.draw(screen)
            level.pers_2.draw(screen)
            buttons.draw(screen)
            player_sprite.draw(screen)
            next_level.draw(screen)
            con = sqlite3.connect("project_db.sqlite")
            cur = con.cursor()
            cur.execute("UPDATE Players SET current_level=? WHERE id=?", (current_level := num_level, id := id))
            con.commit()
            con.close()
            pygame.display.flip()
            Classes.main_cycle(player, player_sprite, level, buttons, book, num_level, next_level, id)
            num_level = 2
            
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
            pygame.display.flip()
            dict_res = {1: False, 2: False}
            Classes.main_cycle(player, player_sprite, level, buttons, book, num_level, next_level, id)
            num_level = 3
    
        if num_level == 3 and not quit:
            #dict_task = {1: False, 2: False, 3: False}
            screen.fill((255, 255, 255))
            boss = pygame.sprite.Group()
            task = pygame.sprite.Group()
            task_1 = pygame.sprite.Group()
            task_2 = pygame.sprite.Group()
            task_3 = pygame.sprite.Group()
            boss_image = Classes.Image('boss2.png', (566, 100), (788, 572), -1, boss)
            level = Classes.Level(screen, 'data\Texts\level_boss.txt', 20, 11, 100)
            image_task = Classes.Image('dialog_task.png', (215, 250), (430, 700), -1, task_1)
            image_task = Classes.Image('dialog_task.png', (730, 250), (430, 700), -1, task_2)
            image_task = Classes.Image('dialog_task.png', (1260, 250), (430, 700), -1, task_3)
            with open('data\Texts\Текста диалогов2.txt', mode='r', encoding='utf8') as file:
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
            draw_text(text_1, 30, 245, 275, 20, 28)
            draw_text(text_2, 30, 760, 275, 20, 28)
            draw_text(text_3, 30, 1290, 275, 20, 28)
            pygame.display.flip()
            boss_func()
    
    
    pygame.quit()
    # sys.exit(app.exec_())
