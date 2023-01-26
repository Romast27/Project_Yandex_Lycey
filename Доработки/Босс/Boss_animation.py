import pygame

SIZE = WIDTH, HEIGHT = 550, 650  # the width and height of our screen
BACKGROUND_COLOR = pygame.Color('white')  # The background colod of our window
FPS = 10  # Frames per second


class MySprite(pygame.sprite.Sprite):
    def __init__(self):
        super(MySprite, self).__init__()

        self.images = []
        self.images.append(pygame.transform.scale(pygame.image.load('data/boss1.png'), (480, 640)))
        self.images.append(pygame.transform.scale(pygame.image.load('data/boss2.png'), (480, 640)))
        self.images.append(pygame.transform.scale(pygame.image.load('data/boss3.png'), (480, 640)))
        self.images.append(pygame.transform.scale(pygame.image.load('data/boss4.png'), (480, 640)))
        self.images.append(pygame.transform.scale(pygame.image.load('data/boss5.png'), (480, 640)))
        self.images.append(pygame.transform.scale(pygame.image.load('data/boss6.png'), (480, 640)))

        self.index = 0

        self.image = self.images[self.index]

        self.rect = pygame.Rect(5, 5, 150, 198)

    def update(self):
        self.index += 1

        if self.index >= len(self.images):
            self.index = 0

        self.image = self.images[self.index]


def main():
    pygame.init()
    screen = pygame.display.set_mode(SIZE)
    my_sprite = MySprite()
    my_group = pygame.sprite.Group(my_sprite)
    clock = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        my_group.update()
        screen.fill(BACKGROUND_COLOR)
        my_group.draw(screen)
        pygame.display.update()
        clock.tick(6)


if __name__ == '__main__':
    main()
