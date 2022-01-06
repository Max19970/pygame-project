import pygame, sys, os


FPS = 60


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


def draw_text(screen):
    font = pygame.font.Font(None, 50)
    logo = pygame.font.Font(None, 100).render("NEWTON'S GAME", True, pygame.Color('#ffb43c'))
    new_game = font.render('НАЧАТЬ ИГРУ', True, pygame.Color('#ffb43c'))
    rules = font.render('КАК ИГРАТЬ', True, pygame.Color('#ffb43c'))
    scores = font.render('ОЧКИ', True, pygame.Color('#ffb43c'))
    exit = font.render('ВЫЙТИ', True, pygame.Color('#ffb43c'))
    screen.blit(logo, (330, 100, 300, 500))
    screen.blit(new_game, (520, 350, 500, 500))
    screen.blit(rules, (533, 410, 500, 500))
    screen.blit(scores, (585, 470, 500, 500))
    screen.blit(exit, (575, 530, 500, 500))


def main_menu(size):
    width, height = size
    screen = pygame.display.set_mode(size)
    background = pygame.Color('black')
    screen.fill(background)

    clock = pygame.time.Clock()
    pygame.display.set_caption("Newton's Game")
    all_sprites = pygame.sprite.Group()
    arrow = Choice_arrow(all_sprites)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    arrow.move('up')
                elif event.key == pygame.K_DOWN:
                    arrow.move('down')
                elif event.key == pygame.K_RETURN:
                    if arrow.choice == 0:
                        pygame.quit()
                        sys.exit()
                    elif arrow.choice == 1:
                        # вывести текст с правилами в этом же окне
                        pass
                    else:
                        pass
                        return
        screen.fill(background)
        draw_text(screen)
        all_sprites.draw(screen)
        all_sprites.update()
        pygame.display.flip()
        clock.tick(FPS)


class Choice_arrow(pygame.sprite.Sprite):
    def __init__(self, all_sprites):
        super().__init__(all_sprites)
        self.image = pygame.transform.scale(load_image('arrow.png'), (30, 30))
        self.rect = self.image.get_rect().move(480, 350)
        self.choice = 3

    def move(self, direction):
        if direction == 'up':
            if self.choice != 3:
                self.choice += 1
        elif direction == 'down':
            if self.choice != 0:
                self.choice -= 1

        self.rect = self.rect.move(-self.rect.x, -self.rect.y)
        if self.choice == 0:
            self.rect.x = 535
            self.rect.y = 535
        elif self.choice == 1:
            self.rect.x = 550
            self.rect.y = 471
        elif self.choice == 2:
            self.rect.x = 495
            self.rect.y = 410
        elif self.choice == 3:
            self.rect.x = 480
            self.rect.y = 350
        print(self.choice)


def main():
    pygame.init()
    pygame.display.init()
    size = width, height = 1280, 720

    main_menu(size)


if __name__ == '__main__':
    main()
