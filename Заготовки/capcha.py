import pygame
import os
import sys


class Captcha:
    def __init__(self, game_screen, image, image1, size_x, size_y):
        pygame.sprite.Sprite.__init__(self)
        self.screen = game_screen
        self.image = image
        self.image1 = image1
        self.rect = self.image.get_rect()
        self.rect.x = size_x
        self.rect.y = size_y
        self.flag = False
        self.cell_size = 140

    def output(self):
        self.screen.blit(self.image, self.rect)
        self.flag = False

    def output2(self):
        self.screen.blit(self.image1, self.rect)
        self.flag = True

    def checking(self, x_pos, y_pos):
        if self.rect.x < x_pos < self.rect.x + self.cell_size \
                and self.rect.y < y_pos < self.rect.y + self.cell_size:
            if  not self.flag:
                self.output2()
            else:
                self.output()


def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    if not os.path.isfile(fullname):
        print(f"Image file '{fullname}' not found")
        sys.exit()
    image = pygame.image.load(fullname)
    return image


def show_captcha():
    pygame.init()
    screen = pygame.display.set_mode((600, 700))
    screen.fill('white')

    captcha_sprites = pygame.sprite.Group()
    sprite_image = load_image('Captcha.png')
    image1 = pygame.transform.scale(sprite_image, (600, 50))
    sprite = pygame.sprite.Sprite(captcha_sprites)
    sprite.image = image1
    sprite.rect = sprite.image.get_rect()
    sprite.rect.x = 0
    sprite.rect.y = 0
    sprite_image = load_image('Ca.png')
    image1 = pygame.transform.scale(sprite_image, (600, 40))
    sprite = pygame.sprite.Sprite(captcha_sprites)
    sprite.image = image1
    sprite.rect = sprite.image.get_rect()
    sprite.rect.x = 0
    sprite.rect.y = 40
    sprite_image = load_image('Captcha_button.png')
    image1 = pygame.transform.scale(sprite_image, (120, 40))
    sprite = pygame.sprite.Sprite(captcha_sprites)
    sprite.image = image1
    sprite.rect = sprite.image.get_rect()
    sprite.rect.x = 400
    sprite.rect.y = 640
    captcha_sprites.draw(screen)

    image_1 = Captcha(screen, pygame.transform.scale(pygame.image.load('data/image_1.jpg'), (140, 140)),
             pygame.transform.scale(pygame.image.load('data/Select.png'), (140, 140)), 45, 95)
    image_2 = Captcha(screen, pygame.transform.scale(pygame.image.load('data/image_2.jpg'), (140, 140)),
                      pygame.transform.scale(pygame.image.load('data/Select.png'), (140, 140)), 230, 95)
    image_3 = Captcha(screen, pygame.transform.scale(pygame.image.load('data/image_3.jpg'), (140, 140)),
                      pygame.transform.scale(pygame.image.load('data/Select.png'), (140, 140)), 425, 95)
    image_4 = Captcha(screen, pygame.transform.scale(pygame.image.load('data/image_4.jpg'), (140, 140)),
                      pygame.transform.scale(pygame.image.load('data/Select.png'), (140, 140)), 45, 275)
    image_5 = Captcha(screen, pygame.transform.scale(pygame.image.load('data/image_5.jpg'), (140, 140)),
                      pygame.transform.scale(pygame.image.load('data/Select.png'), (140, 140)), 230, 275)
    image_6 = Captcha(screen, pygame.transform.scale(pygame.image.load('data/image_6.jpg'), (140, 140)),
                      pygame.transform.scale(pygame.image.load('data/Select.png'), (140, 140)), 425, 275)
    image_7 = Captcha(screen, pygame.transform.scale(pygame.image.load('data/image_7.jpg'), (140, 140)),
                      pygame.transform.scale(pygame.image.load('data/Select.png'), (140, 140)), 45, 490)
    image_8 = Captcha(screen, pygame.transform.scale(pygame.image.load('data/image_8.jpg'), (140, 140)),
                      pygame.transform.scale(pygame.image.load('data/Select.png'), (140, 140)), 230, 490)
    image_9 = Captcha(screen, pygame.transform.scale(pygame.image.load('data/image_9.jpg'), (140, 140)),
                      pygame.transform.scale(pygame.image.load('data/Select.png'), (140, 140)), 425, 490)

    running = True
    show = True
    image_1.output()
    image_2.output()
    image_3.output()
    image_4.output()
    image_5.output()
    image_6.output()
    image_7.output()
    image_8.output()
    image_9.output()
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if 400 < x < 520 and 640 < y < 680 and show is True:
                    show = False
                    if image_1.flag is False and image_2.flag is True and image_3.flag is False and \
                            image_4.flag is True and image_5.flag is False and image_6.flag is True and \
                            image_7.flag is False and image_8.flag is True and image_9.flag is False:
                        screen.fill('white')
                        captcha_results = pygame.sprite.Group()
                        sprite_image = load_image('Captcha_win.png')
                        image1 = pygame.transform.scale(sprite_image, (600, 700))
                        sprite = pygame.sprite.Sprite(captcha_results)
                        sprite.image = image1
                        sprite.rect = sprite.image.get_rect()
                        sprite.rect.x = 0
                        sprite.rect.y = 0
                        sprite_image = load_image('glitch.png')
                        image1 = pygame.transform.scale(sprite_image, (300, 150))
                        sprite = pygame.sprite.Sprite(captcha_results)
                        sprite.image = image1
                        sprite.rect = sprite.image.get_rect()
                        sprite.rect.x = 150
                        sprite.rect.y = 0
                        captcha_results.draw(screen)
                    elif show is True:
                        screen.fill('white')
                        captcha_results = pygame.sprite.Group()
                        sprite_image = load_image('Captcha_lose.png')
                        image1 = pygame.transform.scale(sprite_image, (600, 700))
                        sprite = pygame.sprite.Sprite(captcha_results)
                        sprite.image = image1
                        sprite.rect = sprite.image.get_rect()
                        sprite.rect.x = 0
                        sprite.rect.y = 0
                        sprite_image = load_image('Captcha_restart.png')
                        image1 = pygame.transform.scale(sprite_image, (200, 40))
                        sprite = pygame.sprite.Sprite(captcha_results)
                        sprite.image = image1
                        sprite.rect = sprite.image.get_rect()
                        sprite.rect.x = 380
                        sprite.rect.y = 620
                        captcha_results.draw(screen)
                    pygame.display.flip()

                else:
                    image_1.checking(x, y)
                    image_2.checking(x, y)
                    image_3.checking(x, y)
                    image_4.checking(x, y)
                    image_5.checking(x, y)
                    image_6.checking(x, y)
                    image_7.checking(x, y)
                    image_8.checking(x, y)
                    image_9.checking(x, y)

        pygame.draw.line(screen, pygame.Color('green'), (50, 0), (50, 700))
        pygame.draw.line(screen, pygame.Color('green'), (150, 0), (150, 700))
        pygame.draw.line(screen, pygame.Color('green'), (154, 0), (154, 700))
        pygame.draw.line(screen, pygame.Color('red'), (155, 0), (155, 700))
        pygame.draw.line(screen, pygame.Color('green'), (156, 0), (156, 700))
        pygame.draw.line(screen, pygame.Color('green'), (556, 0), (556, 700))
        pygame.draw.line(screen, pygame.Color('green'), (559, 0), (559, 700))
        pygame.display.flip()
    pygame.quit()


show_captcha()