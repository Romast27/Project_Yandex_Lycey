import pygame


def end_window():
    global y1, m1, k
    m = n1[n2]
    x1 = 10 * m1
    if m == '*':
        y1 += 30
        m1 = 0
        k = True
        m = '\n'
    font = pygame.font.SysFont('EpilepsySansBold', 20)
    text = font.render(m, True, pygame.Color('green'))
    text_x = 150 + x1
    text_y = 10 + y1
    text_w = text.get_width()
    text_h = text.get_height()
    screen.blit(text, (text_x, text_y))
    if k is True:
        font1 = pygame.font.SysFont('EpilepsySansBold', 21)
        text1 = font1.render('C:\easycod\ending> ', True, pygame.Color('green'))
        text_x1 = 10
        text_y1 = 10 + y1
        text_w1 = text1.get_width()
        text_h1 = text1.get_height()
        screen.blit(text1, (text_x1, text_y1))
    k = False


if __name__ == '__main__':
    pygame.init()
    size = x, y = 1960, 1080
    screen = pygame.display.set_mode(size, pygame.FULLSCREEN)
    running = True
    n = open('end_text.txt', 'r', encoding='utf8')
    n1 = n.read()
    n2 = 0
    m1 = 0
    y1 = 0
    clock = pygame.time.Clock()
    '''font = pygame.font.SysFont('EpilepsySansBold', 32)
    text = font.render('Press any button', True, pygame.Color('white'))
    text_x = 800
    text_y = 950
    text_w = text.get_width()
    text_h = text.get_height()
    screen.blit(text, (text_x, text_y))'''
    k = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                running = False
            if n2 < len(n1):
                end_window()
            n2 += 1
            m1 += 1
        pygame.display.flip()
        clock.tick(15)
    pygame.quit()