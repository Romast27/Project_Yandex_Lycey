import pygame


class BlueMangoose:
    def __init__(self, screen, image, image1, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.screen = screen
        self.image = image
        self.image1 = image1
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.blue = True

    def output(self):
        self.screen.blit(self.image, self.rect)
        self.blue = True

    def output2(self):
        self.screen.blit(self.image1, self.rect)
        self.blue = False


pygame.init()
screen = pygame.display.set_mode((400, 400))
b1 = BlueMangoose(screen, pygame.transform.scale(pygame.image.load('data/ground.png'), (50, 50)), pygame.transform.scale(pygame.image.load('data/boom.png'), (50, 50)), 0, 0)
run = True
b1.output()
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            if 0 < x < 50 and 0 < y < 50:
                if b1.blue:
                    b1.output2()
                else:
                    b1.output()
    pygame.display.flip()
pygame.quit()
