import pygame
import sys
import characters
import start_screen
from random import randint


def main():
    pygame.init()
    pygame.display.init()
    start_screen.main_menu()

    size = 800, 600
    screen = pygame.display.set_mode(size)
    background = pygame.Color('white')
    screen.fill(background)

    clock = pygame.time.Clock()
    pygame.display.set_caption('Динозаврик "Хром"')  # хромированный динозаврик
    player = characters.Player()
    ground = characters.Ground(0, 330)
    cactus = characters.Cactus(randint(500, 1200), 253)
    cactusm = characters.cactusm(randint(1100, 1300), 275)
    cactus3 = characters.Cactus3(randint(1500, 1700), 275)
    cactus4 = characters.Cactus4(randint(500, 1200), 275)
    cactusm2 = characters.cactusm2(randint(1850, 2050), 275)
    ground_further = characters.Ground(ground.rect.size[0], 330)
    speed = 0
    score = 0
    started = False
    player_jumping = False
    player_duck = False

    player_jump = pygame.USEREVENT + 1
    player_sprite_change = pygame.USEREVENT + 2
    ground_move = pygame.USEREVENT + 3
    score_count = pygame.USEREVENT + 4
    pygame.time.set_timer(player_sprite_change, 100)
    pygame.time.set_timer(ground_move, 10)
    pygame.time.set_timer(score_count, 100)
    player.image = player.sprites[0]
    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT or \
                    event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    started = True
                    player.image = player.sprites[2]
            if started:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP and not player_jumping:
                        speed = 12
                        pygame.time.set_timer(player_jump, 10)
                        player_jumping = True
                    elif event.key == pygame.K_DOWN and not player_jumping:
                        player_duck = True
                        player.image = player.duck_sprites[0]
                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_DOWN:
                        player_duck = False
                        player.image = player.sprites[2]
                elif event.type == player_jump:
                    player.jump(speed)
                    speed -= 0.5
                elif event.type == player_sprite_change:
                    if not player_duck:
                        if player.image == player.sprites[2]:
                            player.image = player.sprites[3]
                        else:
                            player.image = player.sprites[2]
                    else:
                        if player.image == player.duck_sprites[0]:
                            player.image = player.duck_sprites[1]
                        else:
                            player.image = player.duck_sprites[0]
                elif event.type == ground_move:
                    ground.move()
                    ground_further.move()
                    cactus.move()
                    cactusm.move()
                    cactus3.move()
                    cactusm2.move()
                    if ground.rect.x + ground.rect.size[0] < 0:
                        ground.rect.x = ground_further.rect.size[0]
                        cactusm.spawn(randint(800,900))
                        cactus.spawn(randint(1100, 1300))
                        cactus3.spawn(randint(1500, 1700))
                        cactusm2.spawn(randint(1850, 2050))
                        cactus4.spawn()
                    elif ground_further.rect.x + ground_further.rect.size[0] < 0:
                        ground_further.rect.x = ground.rect.size[0]
                        cactusm.spawn(randint(1500, 1700))
                        cactus.spawn(randint(1850, 2050))
                        cactus3.spawn(randint(1100, 1300))
                        cactusm2.spawn(randint(800,801))
                        cactus4.spawn()

                elif event.type == score_count:
                    score += 1
                if characters.stolknovenie() == True and player_jumping != True:
                    screen.fill((0, 0, 0))
                    main()




        if speed < -12.5:
            pygame.time.set_timer(player_jump, 0)
            player_jumping = False
        screen.fill(background)
        characters.all_sprites.draw(screen)
        characters.all_sprites.update()
        if not started:
            screen.blit(pygame.font.Font(None, 50).render('Нажмите Enter, чтобы начать',
                                                          True, pygame.Color('black')), (160, 180, 300, 300))
        score_to_blit = pygame.font.Font(None, 50).render(f'{score}', True, pygame.Color('black'))
        screen.blit(score_to_blit, (30, 50, 100, 100))
        pygame.display.flip()
        clock.tick(60)


if __name__ == '__main__':
    main()
