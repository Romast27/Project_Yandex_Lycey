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
    font = pygame.font.SysFont('EpilepsySansBold', 21)
    text = font.render(m, True, pygame.Color('green'))
    text_x = 150 + x1
    text_y = 40 + y1
    text_w = text.get_width()
    text_h = text.get_height()
    screen.blit(text, (text_x, text_y))
    if k is True:
        font1 = pygame.font.SysFont('EpilepsySansBold', 21)
        text1 = font1.render('C:\easycod\ending> ', True, pygame.Color('green'))
        text_x1 = 10
        text_y1 = 40 + y1
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
    font2 = pygame.font.SysFont('EpilepsySansBold', 21)
    text2 = font2.render("C:\easycod\ending> please hold down any button", True, pygame.Color('green'))
    text_x2 = 10
    text_y2 = 10
    text_w2 = text2.get_width()
    text_h2 = text2.get_height()
    screen.blit(text2, (text_x2, text_y2))
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