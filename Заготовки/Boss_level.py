import pygame


class Boss:
    def __init__(self, *tasks):
        self.tasks = tasks


class Boss_level:
    pass


class Special_levels:
    def __init__(self, level_type, game_screen, ground_file_name, decoration_file_name, player, level_width=5,
                 level_height=5, cell_size=20):
        self.level_type = level_type
        self.screen = game_screen
        self.ground_file = list(map(lambda x: x.strip('\n'), open(ground_file_name).readlines()))
        self.decoration_file = list(map(lambda x: x.strip('\n'), open(decoration_file_name).readlines()))
        self.width = level_width
        self.height = level_height
        self.cell_size = cell_size
        self.player = player

    def draw_level(self):
        if self.level_type == 'square':
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
                ground_sprites.draw(self.screen)