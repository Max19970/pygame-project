import pygame
import sys
import os
import sqlite3


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
    logo = pygame.font.Font(None, 100).render('Динозаврик "Хром"', True, pygame.Color('black'))
    new_game = font.render('НАЧАТЬ ИГРУ', True, pygame.Color('black'))
    rules = font.render('КАК ИГРАТЬ', True, pygame.Color('black'))
    scores = font.render('ОЧКИ', True, pygame.Color('black'))
    exit = font.render('ВЫЙТИ', True, pygame.Color('black'))
    screen.blit(logo, (60, 70, 300, 200))
    screen.blit(new_game, (292, 320, 500, 500))
    screen.blit(rules, (305, 380, 100, 100))
    screen.blit(scores, (357, 440, 500, 500))
    screen.blit(exit, (347, 500, 500, 500))


def main_menu():
    size = 800, 600
    screen = pygame.display.set_mode(size)
    background = pygame.Color('grey')
    screen.fill(background)

    clock = pygame.time.Clock()
    pygame.display.set_caption('Динозаврик "Хром"')
    all_sprites = pygame.sprite.Group()
    arrow = Choice_arrow(all_sprites)
    rules_show = False
    leaderboard_show = False

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
                        leaderboard_show = True
                        arrow.block = True
                        pass
                    elif arrow.choice == 2:
                        rules_show = True
                        arrow.block = True
                    else:
                        pass
                        return
                elif event.key == pygame.K_ESCAPE:
                    if rules_show:
                        rules_show = False
                        arrow.block = False
                    elif leaderboard_show:
                        leaderboard_show = False
                        arrow.block = False
        if rules_show:
            screen.blit(rules(), (0, 0, 800, 600))
        elif leaderboard_show:
            screen.blit(leaderboard(), (0, 0, 800, 600))
        else:
            screen.fill(background)
            draw_text(screen)
            all_sprites.draw(screen)
            all_sprites.update()
        pygame.display.flip()
        clock.tick(FPS)


def rules():
    rules = ['В этой игре ты управляешь динозавриком Хромом',
             'Уворачивайся от препятствий, встречающихся по пути!',
             'Прыжок - стрелка вверх',
             'Пригнуться - стрелка вниз',
             'Выйти из игры - ESC (во время игры)',
             'Назад - ESC (в меню)',
             'Выбор в меню - Enter']
    rules_screen = pygame.Surface((800, 600))
    rules_screen.fill(pygame.Color('grey'))
    font = pygame.font.Font(None, 40)
    logo = pygame.font.Font(None, 50).render('Правила', True, pygame.Color('black'))
    rules_screen.blit(logo, (100, 70, 300, 300))
    for rule in rules:
        rules_screen.blit(font.render(rule, True, pygame.Color('black')),
                          (20, 150 + 40 * rules.index(rule), 560, 60))
    return rules_screen


def leaderboard():
    lb_screen = pygame.Surface((800, 600))
    lb_screen.fill(pygame.Color('grey'))
    con = sqlite3.connect('data/leaderboard.sqlite')
    cur = con.cursor()
    players = cur.execute("""SELECT * FROM scores""").fetchall()
    con.close()
    font = pygame.font.Font(None, 40)
    logo = pygame.font.Font(None, 50).render('Таблица лидеров', True, pygame.Color('black'))
    lb_screen.blit(logo, (100, 70, 300, 300))
    for player in players:
        lb_screen.blit(font.render(f'{player[0]}. {player[1]}   -   {player[2]}', True, pygame.Color('black')),
                          (240, 150 + 40 * players.index(player), 560, 60))
    return lb_screen


class Choice_arrow(pygame.sprite.Sprite):
    def __init__(self, all_sprites):
        super().__init__(all_sprites)
        self.image = pygame.transform.scale(load_image('arrow.png'), (30, 30))
        self.rect = self.image.get_rect().move(252, 320)
        self.choice = 3
        self.block = False

    def move(self, direction):
        if not self.block:
            if direction == 'up':
                if self.choice != 3:
                    self.choice += 1
            elif direction == 'down':
                if self.choice != 0:
                    self.choice -= 1

            self.rect = self.rect.move(-self.rect.x, -self.rect.y)
            if self.choice == 0:
                self.rect.x = 307
                self.rect.y = 505
            elif self.choice == 1:
                self.rect.x = 322
                self.rect.y = 441
            elif self.choice == 2:
                self.rect.x = 267
                self.rect.y = 380
            elif self.choice == 3:
                self.rect.x = 252
                self.rect.y = 320
