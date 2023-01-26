import  Classes
import pygame
import main


pygame.init()
screen = pygame.display.set_mode((1960, 1080, pygame.FULLSCREEN))
screen.fill((255, 255, 255))
        flag_book = False
        text = []
        player = Classes.Player(screen, (700, 500), None, main.player_sprite)
        level = Classes.Level(screen, 'data\level_1.txt', 20, 11, 100)
        button_book = Classes.Image('book_button.png', (1860, 70), (50, 50), -1, main.buttons)
        cross = Classes.Image('cross.png', (1700, 100), (50, 50), -1, main.book)
        arrow = Classes.Image('arrow.png', (1500, 860), (70, 50), -1, main.book)
        level.draw_level_ground('floor1.png', 'dec1.png', player, main.player_sprite)
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
        main.buttons.draw(screen)
        main.player_sprite.draw(screen)
        main.next_level.draw(screen)
        Classes.main_cycle(player, main.player_sprite, level, main.buttons, main.book, 2, main.next_level, id)
        screen.fill((255, 255, 255))
        boss = pygame.sprite.Group()
        boss_image = Classes.Image('boss2.png', (566, 100), (788, 572), -1, boss)
        level = Classes.Level(screen, 'data\level_boss.txt', 20, 11, 100)
        image_task = Classes.Image('dialog_task.png', (215, 250), (430, 600), -1, boss)
        image_task = Classes.Image('dialog_task.png', (730, 250), (430, 600), -1, boss)
        image_task = Classes.Image('dialog_task.png', (1260, 250), (430, 600), -1, boss)
        level.draw_level_ground('ground sprite.png', 'dec.png', player, main.player_sprite)
        level.ground_sprites.draw(screen)
        level.decoration_sprites.draw(screen)
        boss.draw(screen)
        main.player_sprite.draw(screen)
        main.buttons.draw(screen)
        pygame.display.flip()
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                if event.type == pygame.MOUSEBUTTONDOWN and Classes.move_is_valid(event.pos, (1840, 1910),
                                                                                  (10, 80)):
                    pygame.quit()