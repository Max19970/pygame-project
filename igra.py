import os
import pygame
import sys
import start_screen


class Tile(pygame.sprite.Sprite):
    def __init__(self, tile_type, pos_x, pos_y):
        super().__init__(tiles_group, all_sprites)
        self.image = tile_images[tile_type]
        self.rect = self.image.get_rect().move(
            tile_width * pos_x, tile_height * pos_y)


class Player(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__(player_group, all_sprites)
        self.coords = [pos_y, pos_x]
        self.image = player_image
        self.rect = self.image.get_rect().move(
            tile_width * pos_x + 15, tile_height * pos_y + 5)

    def move(self, direction, level_map):
        if direction == 'up':
            if level_map[int(self.coords[0] - 0.5)][int(self.coords[1])] in ['.', '@', '$']:
                self.rect.y -= 25
                self.coords[0] -= 0.5
        elif direction == 'right':
            if level_map[int(self.coords[0])][int(self.coords[1]) + 1] in ['.', '@', '$']:
                self.rect.x += 25
                self.coords[1] += 0.5
        elif direction == 'down':
            if level_map[int(self.coords[0] + 1)][int(self.coords[1])] in ['.', '@', '$']:
                self.rect.y += 25
                self.coords[0] += 0.5
        elif direction == 'left':
            if level_map[int(self.coords[0])][int(self.coords[1] - 0.5)] in ['.', '@', '$']:
                self.rect.x -= 25
                self.coords[1] -= 0.5


class Camera:
    # зададим начальный сдвиг камеры
    def __init__(self):
        self.dx = 0
        self.dy = 0

    # сдвинуть объект obj на смещение камеры
    def apply(self, obj):
        obj.rect.x += self.dx
        obj.rect.y += self.dy

    # позиционировать камеру на объекте target
    def update(self, target):
        self.dx = -(target.rect.x + target.rect.w // 2 - WIDTH // 2)
        self.dy = -(target.rect.y + target.rect.h // 2 - HEIGHT // 2)


FPS = 60


def terminate():
    pygame.quit()
    sys.exit()


def start_screen():
    intro_text = ["              ПРАВИЛА ИГРЫ", "", "",
                  "Герой передвигается по нажатию стрелок в "
                  "соответствующем направлении",
                  "Нажмите любую клавишу, чтобы начать", ]
    size = WIDTH, HEIGHT = 800, 450
    screen = pygame.display.set_mode(size)

    fon = pygame.transform.scale(load_image('box.png'), (WIDTH, HEIGHT))
    screen.blit(fon, (0, 0))
    font = pygame.font.Font(None, 30)
    text_coord = 100
    clock = pygame.time.Clock()
    for line in intro_text:
        string_rendered = font.render(line, 1, pygame.Color('black'))
        intro_rect = string_rendered.get_rect()
        text_coord += 10
        intro_rect.top = text_coord
        intro_rect.x = 10
        text_coord += intro_rect.height
        screen.blit(string_rendered, intro_rect)
    pygame.display.set_caption('Перемещение героя: Правила')

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.KEYDOWN or \
                    event.type == pygame.MOUSEBUTTONDOWN:
                return  # начинаем игру


def load_level(filename):
    filename = "data/" + filename
    # читаем уровень, убирая символы перевода строки
    with open(filename, 'r') as mapFile:
        level_map = [line.strip() for line in mapFile]

    # и подсчитываем максимальную длину
    max_width = max(map(len, level_map))

    # дополняем каждую строку пустыми клетками ('.')
    return list(map(lambda x: x.ljust(max_width, '.'), level_map))


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


def generate_level(level):
    new_player, x, y = None, None, None
    for y in range(len(level)):
        for x in range(len(level[y])):
            if level[y][x] == '.':
                Tile('empty', x, y)
            elif level[y][x] == '#':
                Tile('wall', x, y)
            elif level[y][x] == '@':
                Tile('empty', x, y)
                new_player = Player(x, y)
            elif level[y][x] == "$":
                Tile('vihod', x, y)
    # вернем игрока, а также размер поля в клетках
    return new_player, x, y

class Ball(pygame.sprite.Sprite):
    def __init__(self, radius, x, y):
        super().__init__(all_sprites)
        self.radius = radius
        self.image = pygame.Surface((2 * radius, 2 * radius),
                                    pygame.SRCALPHA, 32)
        pygame.draw.circle(self.image, pygame.Color("red"),
                           (radius, radius), radius)
        self.rect = pygame.Rect(x, y, 2 * radius, 2 * radius)
        self.vx = 1
        self.vy = 1

    def update(self):
        self.rect = self.rect.move(self.vx, self.vy)
        if pygame.sprite.spritecollideany(self, horizontal_borders):
            self.vy = -self.vy
        if pygame.sprite.spritecollideany(self, vertical_borders):
            self.vx = -self.vx


class Border(pygame.sprite.Sprite):
    # строго вертикальный или строго горизонтальный отрезок
    def __init__(self, x1, y1, x2, y2):
        super().__init__(all_sprites)
        if x1 == x2:  # вертикальная стенка
            self.add(vertical_borders)
            self.image = pygame.Surface([1, y2 - y1])
            self.rect = pygame.Rect(x1, y1, 1, y2 - y1)
        else:  # горизонтальная стенка
            self.add(horizontal_borders)
            self.image = pygame.Surface([x2 - x1, 1])
            self.rect = pygame.Rect(x1, y1, x2 - x1, 1)

all_sprites = pygame.sprite.Group()
size = width, height = 850, 350
screen = pygame.display.set_mode(size)

horizontal_borders = pygame.sprite.Group()
vertical_borders = pygame.sprite.Group()
Border(5, 5, width - 5, 5)
Border(5, height - 5, width - 5, height - 5)
Border(5, 5, 5, height - 5)
Border(width - 5, 5, width - 5, height - 5)

if __name__ == '__main__':
    screen = pygame.display.set_mode(size)
    pygame.init()
    pygame.display.init()

    tile_images = {
        'wall': load_image('box.png'),
        'empty': load_image('grass.png'),
        'vihod': load_image('grass1.png')
    }
    player_image = load_image('box.png')

    player = None

    # группы спрайтов
    all_sprites = pygame.sprite.Group()
    tiles_group = pygame.sprite.Group()
    player_group = pygame.sprite.Group()

    tile_width = tile_height = 50

    player, level_x, level_y = generate_level(load_level('level_1.txt'))
    level_map = load_level('level_1.txt')
    clock = pygame.time.Clock()
    camera = Camera()

    pygame.display.set_caption('Перемещение героя')

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    player.move('up', level_map)
                    Ball(10, 425, 175)
                elif event.key == pygame.K_RIGHT:
                    player.move('right', level_map)
                    Ball(10, 425, 175)
                elif event.key == pygame.K_DOWN:
                    player.move('down', level_map)
                    Ball(10, 425, 175)
                elif event.key == pygame.K_LEFT:
                    player.move('left', level_map)
                    Ball(10, 425, 175)
        screen.fill((0, 0, 0))
        # camera.update(player)
        # for sprite in all_sprites:
        #     camera.apply(sprite)
        tiles_group.draw(screen)
        tiles_group.update()
        player_group.draw(screen)
        player_group.update()
        pygame.display.flip()
        clock.tick(FPS)
