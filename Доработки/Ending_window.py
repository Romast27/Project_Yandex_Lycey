import pygame


def end_window():
    global y1, m1
    m = n1[n2]
    x1 = 10 * m1
    if m == '\n':
        y1 += 15
        m1 = 0
    font = pygame.font.Font(None, 16)
    text = font.render(m, True, pygame.Color('green'))
    text_x = 10 + x1
    text_y = 10 + y1
    text_w = text.get_width()
    text_h = text.get_height()
    screen.blit(text, (text_x, text_y))


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