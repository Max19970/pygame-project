import pygame
import os
import sys


all_sprites = pygame.sprite.Group()
player_sprites = pygame.sprite.Group()
bird_sprites = pygame.sprite.Group()
cactus_sprites = pygame.sprite.Group()
ground_sprites = pygame.sprite.Group()
flag = False


def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)

    if colorkey is not None:
        image = image.convert()
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    else:
        image = image.convert_alpha()
    return image


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__(player_sprites, all_sprites)
        self.sprites = self.cut_sprites(load_image('dino.png'))
        self.duck_sprites = self.cut_duck(load_image('dino_ducking.png'))
        self.image = load_image('dinof.png')
        self.rect = self.image.get_rect().move(50, 253)

    def cut_sprites(self, sprites_file):
        sprites_cut = []
        for i in range(1):
            for j in range(5):
                sprite_location = 88 * j, 93 * i
                sprites_cut.append(sprites_file.subsurface(pygame.Rect(
                    sprite_location, (88, 93)
                )))
        return sprites_cut

    def cut_duck(self, sprites_file):
        sprites_cut = []
        for i in range(1):
            for j in range(2):
                sprite_location = 118 * j, 95 * i
                sprites_cut.append(sprites_file.subsurface(pygame.Rect(
                    sprite_location, (118, 95)
                )))
        return sprites_cut

    def jump(self, speed):
        self.rect.y -= speed
        if self.rect.y > 253:
            self.rect.y = 253

    def spawn(self):
        self.image = load_image('dinof.png')
        self.rect = self.image.get_rect().move(50, 253)


class Ground(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__(all_sprites, ground_sprites)
        self.image = load_image('ground.png')
        self.rect = self.image.get_rect().move(x, y)

    def move(self, speedgo):
        self.rect.x -= speedgo

    def spawn(self):
        self.kill()
        self.rect = self.image.get_rect().move(0, 330)


class Bird(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__(bird_sprites, all_sprites)
        self.sprites = self.cut_sprites(load_image('ptera.png'))
        self.image = self.sprites[0]
        self.rect = self.image.get_rect().move(x, y)

    def cut_sprites(self, sprites_file):
        sprites_cut = []
        for i in range(1):
            for j in range(2):
                sprite_location = 92 * j, 81 * i
                sprites_cut.append(sprites_file.subsurface(pygame.Rect(
                    sprite_location, (92, 81)
                )))
        return sprites_cut

    def move(self, speedgo):
        self.rect.x -= speedgo

    def spawn(self, x):
        self.rect = self.image.get_rect().move(x, 200)
        self.mask = pygame.mask.from_surface(self.image)

    def update(self, player):
        if pygame.sprite.collide_mask(self, player):
            global flag
            flag = True


class Cactus(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__(all_sprites, cactus_sprites)
        self.image = load_image('cactus.png')
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect().move(800, 253)

    def move(self, speedgo):
        self.rect.x -= speedgo

    def spawn(self, x):
        self.rect = self.image.get_rect().move(x, 253)
        self.mask = pygame.mask.from_surface(self.image)

    def update(self, player):
        if pygame.sprite.collide_mask(self, player):
            global flag
            flag = True


class cactusm(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__(all_sprites, cactus_sprites)
        self.image = load_image('cacti-small.png')
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect().move(x, 273)
    def move(self, speedgo):
        self.rect.x -= speedgo

    def spawn(self, x):
        self.rect = self.image.get_rect().move(x, 273)
        self.mask = pygame.mask.from_surface(self.image)


    def update(self, player):
        if pygame.sprite.collide_mask(self, player):
            global flag
            flag = True



class Cactus3(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__(all_sprites, cactus_sprites)
        self.image = load_image('cacti-3.png')
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect().move(x, 253)

    def move(self, speedgo):
        self.rect.x -= speedgo
    def spawn(self, x):
        self.rect = self.image.get_rect().move(x, 253)
        self.mask = pygame.mask.from_surface(self.image)


    def update(self, player):
        if pygame.sprite.collide_mask(self, player):
            global flag
            flag = True

class cactusm2(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__(all_sprites, cactus_sprites)
        self.image = load_image('cacti-small2.png')
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect().move(x, 273)
    def move(self, speedgo):
        self.rect.x -= speedgo

    def spawn(self, x):
        self.rect = self.image.get_rect().move(x, 273)
        self.mask = pygame.mask.from_surface(self.image)


    def update(self, player):
        if pygame.sprite.collide_mask(self, player):
            global flag
            flag = True

class Cactus4(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__(all_sprites, cactus_sprites)
        self.image = load_image('cacti-2.png')
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect().move(x, 2530)

    def move(self, speedgo):
        self.rect.x -= speedgo

    def spawn(self, x):
        self.rect = self.image.get_rect().move(x, 253)
        self.mask = pygame.mask.from_surface(self.image)


    def update(self, player):
        if pygame.sprite.collide_mask(self, player):
            global flag
            flag = True

def stolknovenie():
    global flag
    if flag == True:
        flag = False
        return True