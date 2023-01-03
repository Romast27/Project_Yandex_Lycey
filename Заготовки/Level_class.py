import pygame
import sys
import os


def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    if not os.path.isfile(fullname):
        print(f"Image file '{fullname}' not found")
        sys.exit()
    image = pygame.image.load(fullname)
    return image


class Level:
    def __init__(self, game_screen, ground_file_name, decoration_file_name, level_width=5, level_height=5, cell_size=20):
        self.screen = game_screen
        self.ground_file = list(map(lambda x: x.strip('\n'), open(ground_file_name).readlines()))
        self.decoration_file = list(map(lambda x: x.strip('\n'), open(decoration_file_name).readlines()))
        self.width = level_width
        self.height = level_height
        self.cell_size = cell_size

    def draw_level_ground(self, ground_sprite):
        ground_sprites = pygame.sprite.Group()
        sprite_image = load_image(ground_sprite)
        image1 = pygame.transform.scale(sprite_image, (self.cell_size, self.cell_size))
        for u in range(self.width):
            for i in range(self.height):
                try:
                    if self.ground_file[i][u] == '#':
                        sprite = pygame.sprite.Sprite(ground_sprites)
                        sprite.image = image1
                        sprite.rect = sprite.image.get_rect()
                        sprite.rect.x = self.cell_size * u
                        sprite.rect.y = self.cell_size * i
                except IndexError:
                    pass
        ground_sprites.draw(screen)

    def draw_level_decorations(self, decorations_sprite):
        decoration_sprites = pygame.sprite.Group()
        sprite_image = load_image(decorations_sprite)
        sprite_image = sprite_image.convert_alpha(self.screen)
        sprite_image = pygame.transform.scale(sprite_image, (self.cell_size, self.cell_size))
        for u in range(self.width):
            for i in range(self.height):
                try:
                    if self.decoration_file[i][u] == '0':
                        sprite = pygame.sprite.Sprite(decoration_sprites)
                        sprite.image = sprite_image
                        sprite.rect = sprite.image.get_rect()
                        sprite.rect.x = self.cell_size * u
                        sprite.rect.y = self.cell_size * i
                except IndexError:
                    pass
        decoration_sprites.draw(screen)


pygame.init()
size = width, height = 400, 400
screen = pygame.display.set_mode(size)
running = True
level = Level(screen, 'level.txt', 'level_decorations.txt', 8, 8, 50)
level.draw_level_ground('ground sprite.png')
level.draw_level_decorations('dec.png')
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.display.flip()
pygame.quit()