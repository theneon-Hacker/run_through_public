import pygame, music_acceptor

WIDTH = 800
HEIGHT = 800
pygame.font.init()
pygame.mixer.init()
pygame.display.set_caption('MENU!')
myfont = pygame.font.SysFont('Comic Sans MS', 30)


def begin():
    screen = pygame.display.set_mode((1000, 600))
    im = pygame.image.load_extended("images\Begin.png").convert_alpha()
    im = pygame.transform.scale(im, (1000, 600))
    screen.blit(im, (0, 0))
    pygame.display.update()
    music_acceptor.begin()
    pygame.time.delay(2000)


def mainMenu():
    pygame.font.init()
    pygame.mixer.init()
    pygame.display.set_caption('MENU!')
    myfont = pygame.font.SysFont('Comic Sans MS', 30)
    window = pygame.display.set_mode((WIDTH, HEIGHT))
    menu = pygame.image.load_extended("images\main_menu.png").convert_alpha()
    show = True
    music_acceptor.menuMusic()
    textsurface_version = myfont.render('Alpha 0.4.0', False, (255, 255, 255))
    font = pygame.font.SysFont('Comic Sans MS', 60)
    text_button = font.render('Play', 1, (255, 255, 255))
    rect_button = text_button.get_rect(center=window.get_rect().center)
    window.blit(text_button, rect_button)
    while show:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1 and 350 < event.pos[0] < 435 and 350 < event.pos[1] < 435:
                    music_acceptor.playButton()
                    pygame.time.delay(300)
                    show = False
                    break
            window.blit(menu, (0, 0))
            window.blit(textsurface_version, (0, 600))
            window.blit(text_button, rect_button)
            pygame.display.update()
    pygame.display.quit()


if __name__ == '__main__':
    raise FutureWarning('Better to import this file but you run this')
