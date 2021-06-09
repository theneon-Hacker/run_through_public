# ------------------------------------------Importing and assigning constants-----------------------------------

import random

import images
import music_acceptor
import pygame

info = pygame.display.Info()
WIDTH = info.current_w
HEIGHT = info.current_h
FPS = 30
pygame.init()
pygame.mixer.pre_init(44100, 16, 2, 4096)
pygame.mixer.init()

global score
score = [0]
inventory = []

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (225, 225, 0)


# ---------------------------------------------Creating of classes objects and methods-----------------------


def bg_set():
    """ Setting up the background image """
    global WIDTH, HEIGHT
    background = pygame.transform.scale(pygame.image.load_extended("images/bg.png").convert_alpha(), (WIDTH, HEIGHT))
    pygame.display.update()
    return background


def borders(w, h):
    """ Creating the borders of game field """
    pygame.draw.line(window, WHITE, [25, 0], [25, h - 50], 6)
    pygame.draw.line(window, WHITE, [w - 25, 0], [w - 25, h - 50], 6)
    pygame.draw.line(window, WHITE, [25, h - 50], [w - 25, h - 50], 6)
    pygame.draw.line(window, WHITE, [25, 25], [w - 25, 25], 6)


def changes(screen):
    """ Displays changes on the screen """
    global inventory
    screen.blit(bg, (0, 0))
    Sprites.draw(screen)
    Sprites.update()
    ammo.draw(screen)
    ammo.update()
    prt.check_trying_using()
    if inventory.count('score {}'.format(id(score_0))) == 0:
        score_0.pick(inventory, player, Sprites, score)
    if inventory.count('score {}'.format(id(score_1))) == 0:
        score_1.pick(inventory, player, Sprites, score)
    if inventory.count('boost {}'.format(id(sp))) == 0:
        sp.boost(inventory, player, Sprites)
    borders(WIDTH, HEIGHT)
    see_score(score)
    key_0.pick(inventory, player, Sprites)
    pygame.display.flip()


def see_score(score_):
    """ Allows to see score on screen """
    pygame.font.init()
    myfont = pygame.font.SysFont('Comic Sans MS', 20)

    textsurface_score = myfont.render('Score: {}'.format(score_[len(score_) - 1]), False, WHITE)
    window.blit(textsurface_score, (30, 0))


def assign_leftLimit():
    """ Set leftLimit for player """
    player.rect.x = 25


def assign_rightLimit():
    """ Set rightLimit for player """
    player.rect.x = WIDTH - 75


def assign_upLimit():
    """ Set upLimit for player """
    player.rect.y = 25


def assign_downLimit():
    """ Set downLimit for player """
    player.rect.y = 100


def mainTurn(keys):
    """ Handles all clicks on keyboard: shooting, pausing, moving """
    global paused
    if keys[pygame.K_e]:
        if len(ammo) <= 5:
            player.shoot()
            music_acceptor.shoot()
    elif keys[pygame.K_d] and player.rect.x < WIDTH - 75:
        player.move_r()
    elif keys[pygame.K_a] and player.rect.x > 25:
        player.move_l()
    elif keys[pygame.K_w] and player.rect.y > 25:
        player.move_up()
    elif keys[pygame.K_s] and player.rect.y < HEIGHT - 100:
        player.move_down()
    elif player.rect.x < 25:
        assign_leftLimit()
    elif player.rect.x > WIDTH - 55:
        assign_rightLimit()
    elif player.rect.y < 25:
        assign_upLimit()
    elif player.rect.y > HEIGHT - 100:
        assign_downLimit()


class Player(pygame.sprite.Sprite):
    """ A class that designates and prescribes the capabilities of the player """

    def __init__(self):
        """ Initializing class's copy """
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(pygame.image.load_extended("images/playerImage_right.png").convert_alpha(),
                                            (50, 50))
        self.image.set_colorkey((255, 255, 255))
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 2, HEIGHT / 2)
        self.lastMove = 'right'
        self.speed = 25
        self.health = 3

    def move_r(self):
        """ Allows to moving right """
        self.image = pygame.transform.scale(pygame.image.load_extended("images/playerImage_right.png").convert_alpha(),
                                            (50, 50))
        self.image.set_colorkey((255, 255, 255))
        self.rect.x += self.speed
        self.lastMove = 'right'
        pygame.time.delay(10)

    def move_l(self):
        """ Allows to moving left """
        self.image = pygame.transform.scale(pygame.image.load_extended("images/playerImage_left.png").convert_alpha(),
                                            (50, 50))
        self.image.set_colorkey((255, 255, 255))
        self.rect.x = self.rect.x - self.speed
        self.lastMove = 'left'

    def move_up(self):
        """ Allows to moving up """
        self.image = pygame.transform.scale(pygame.image.load_extended("images/playerImage_up.png").convert_alpha(),
                                            (50, 50))
        self.image.set_colorkey((255, 255, 255))
        self.rect.y -= self.speed
        self.lastMove = 'up'

    def move_down(self):
        """ Allows to moving down """
        self.image = pygame.transform.scale(pygame.image.load_extended("images/playerImage_down.png").convert_alpha(),
                                            (50, 50))
        self.image.set_colorkey((255, 255, 255))
        self.rect.y += self.speed
        self.lastMove = 'down'

    def shoot(self):
        """ Allows to shoot with another special class, Bullet """
        bullet = Bullet(self.rect.centerx, self.rect.top)
        ammo.add(bullet)

    def blit(self, screen):
        """ Show player on screen """
        self.image.blit(screen, (self.rect.x, self.rect.y))
        pygame.display.update()

    def check_health(self, screen):
        """ Control player's health """
        if self.health <= 0:
            screen.fill(BLACK)
            pygame.quit()


class Bullet(pygame.sprite.Sprite):
    """ Class describing of behavior of the bullet which used to shooting by the Player """

    def __init__(self, x, y):
        """ Initializing the bullet """
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((10, 20))
        self.image.fill(BLUE)
        self.rect = self.image.get_rect()
        self.rect.bottom = y
        self.rect.centerx = x
        self.speedy = -10
        self.__var__ = player.lastMove

    def update(self):
        """ Updating bullet's position every turn and control bullet out-of-screen"""
        if self.__var__ == 'right':
            self.rect.x -= self.speedy
        elif self.__var__ == 'left':
            self.rect.x += self.speedy
        elif self.__var__ == 'up':
            self.rect.y += self.speedy
        elif self.__var__ == 'down':
            self.rect.y -= self.speedy
        if self.rect.x > WIDTH or self.rect.x < 0 or self.rect.y > HEIGHT or self.rect.y < 0:
            ammo.remove(self)


class Portal(pygame.sprite.Sprite):
    """ Class for creating the Portal which will teleporting the player if key was picked up """

    def __init__(self, x, y, opportunity=True):
        """ Initializing """
        pygame.sprite.Sprite.__init__(self)
        self.opportunity = opportunity
        self.image = pygame.transform.scale(pygame.image.load_extended("images/redPortal.png").convert_alpha(),
                                            (50, 75))
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x

    def update(self):
        """ Checking every turn if the Portal is unlocked """
        if self.opportunity or 'key' in inventory:
            self.image = pygame.transform.scale(pygame.image.load_extended("images/greenPortal.png").convert_alpha(),
                                                (50, 75))
            self.image.set_colorkey((255, 255, 255))
        elif not self.opportunity:
            self.image = pygame.transform.scale(pygame.image.load_extended("images/redPortal.png").convert_alpha(),
                                                (50, 75))
            self.image.set_colorkey((255, 255, 255))

    def check_trying_using(self):
        """ Teleporting player if Portal was on and player is located in Portal's teleporting area """
        if self.opportunity or 'key' in inventory:
            if self.rect.colliderect(player):
                music_acceptor.usingPortalSound()
                player.rect.x = random.randrange(75, WIDTH - 125)
                player.rect.y = random.randrange(25, HEIGHT - 100)


class Key(pygame.sprite.Sprite):
    """ Object for unlocking the Portal """

    def __init__(self, x, y):
        """ Declare starting conditions """
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(pygame.image.load_extended("images/remote control.png").convert_alpha(),
                                            (50, 50))
        self.image.set_colorkey((255, 255, 255))
        self.rect = self.image.get_rect()
        self.rect.bottom = y
        self.rect.centerx = x
        self.__cooldown = 0

    def pick(self, inv, pl, group):
        """ Need for appearance of possibility of the Player pick up this key"""
        if self.rect.colliderect(pl):
            group.remove(self)
            if inv.count('key') == 0:
                inv += ['key']
                music_acceptor.activatedPortalSound()

    def update(self):
        """ Teleporting self in random point every 45 turns for difficulty to catch it """
        if self.__cooldown % 45 == 0:
            self.rect.x = random.randrange(75, WIDTH - 125)
            self.rect.y = random.randrange(25, HEIGHT - 100)
        self.__cooldown += 1
        self.image.blit(window, (self.rect.x, self.rect.y))


class Score(pygame.sprite.Sprite):
    """ Represents the bonus: score """

    def __init__(self, x, y):
        """ Initializing self """
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(pygame.image.load_extended("images/scoreBonus.png").convert_alpha(),
                                            (48, 32))
        self.image.set_colorkey((0, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.bottom = y
        self.rect.centerx = x
        self.__randomize = True
        self.used = False

    def pick(self, inv, pl, group, sc):
        """ Checking for picking up, then remove from window, then score grown up """
        if self.rect.colliderect(pl) and not self.used:
            group.remove(self)
            inv += ['score {}'.format(id(self))]
            sc += [sc[len(sc) - 1] + 100]
            self.used = True

    def update(self):
        """ Updating self every turn and randomizing self's position in beginning of game once """
        if self.__randomize:
            self.rect.x = random.randrange(75, WIDTH - 125)
            self.rect.y = random.randrange(25, HEIGHT - 100)
            self.__randomize = False
        self.image.blit(window, (self.rect.x, self.rect.y))


class Speed(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(pygame.image.load_extended("images/speedUp.png").convert_alpha(), (50, 50))
        self.image.set_colorkey((255, 255, 255))
        self.rect = self.image.get_rect()
        self.rect.bottom = y
        self.rect.centerx = x
        self.__randomize = True
        self.__cooldown = 0
        self.used = False

    def boost(self, inv, pl, group):
        if self.rect.colliderect(pl) and not self.used:
            group.remove(self)
            if inv.count('boost {}'.format(id(self))) == 0:
                pygame.time.set_timer(pygame.USEREVENT, 3000)
                inv += ['boost {}'.format(id(self))]
            self.used = True

    def update(self):
        if self.__cooldown % 15 == 0 and not self.used:
            self.boost(inventory, player, Sprites)
        if self.__randomize:
            self.rect.x = random.randrange(75, WIDTH - 125)
            self.rect.y = random.randrange(25, HEIGHT - 100)
            self.__randomize = False
        self.__cooldown += 1


# ---------------------------------------------Last assingment---------------------------
pygame.init()


def create():
    """ Create first level """
    global window
    global clock, Sprites, ammo, bg
    global player, prt, key_0, score_0, score_1, sp
    global running, counter_boost, paused
    paused = False
    window = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
    pygame.display.set_caption("Run through")
    clock = pygame.time.Clock()
    Sprites = ammo = pygame.sprite.Group()
    bg = bg_set()

    player = Player()
    prt = Portal(25, 75, False)
    key_0 = Key(400, 580)
    score_0 = Score(200, 700)
    score_1 = Score(300, 50)
    sp = Speed(700, 700)
    Sprites.add(player, prt, key_0, score_0, score_1, sp)

    running, counter_boost = True, 3


images.begin()
images.mainMenu()
create()
music_acceptor.menuStop()
music_acceptor.mainMusic()


# ---------------------------------------------Playing cycle------------------------------
def cycle(isrun, counter):
    """ This is playing loop """
    global window
    global paused
    while isrun:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.USEREVENT:
                if counter > 0:
                    player.speed = 50
                elif counter == 0:
                    player.speed = 25
                counter -= 1
            if event.type == pygame.KEYDOWN:
                print(event.key, pygame.K_p, sep='\t')
                if event.key == pygame.K_p:
                    paused = not paused
                    if not paused:
                        music_acceptor.mainCont()
                        continue
                    else:
                        music_acceptor.mainStop()
            elif event.type == pygame.QUIT:
                isrun = False
            elif event.type == pygame.VIDEORESIZE:
                window = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)
                pygame.display.update()
        if not paused:
            keys = pygame.key.get_pressed()
            mainTurn(keys)
            changes(window)


cycle(running, counter_boost)
pygame.quit()
