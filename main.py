import pygame
import sys
import characters
import start_screen
from random import randint, choice


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
    bird = characters.Bird(randint(2200, 2300), 200)
    ground_further = characters.Ground(ground.rect.size[0], 330)
    speed = 0
    score = 0
    i = 0
    speedgo = 5
    started = False
    player_jumping = False
    player_duck = False
    dont_move = False

    player_jump = pygame.USEREVENT + 1
    player_sprite_change = pygame.USEREVENT + 2
    ground_move = pygame.USEREVENT + 3
    score_count = pygame.USEREVENT + 4
    damage = pygame.USEREVENT + 5
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
                    elif event.key == pygame.K_DOWN:
                        player_duck = True
                        player.image = player.duck_sprites[0]
                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_DOWN:
                        player_duck = False
                        player.image = player.sprites[2]
                elif event.type == player_jump:
                    player.jump(speed)
                    if player_duck:
                        speed -= 1
                    else:
                        speed -= 0.5
                elif event.type == player_sprite_change and not dont_move:
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
                    if bird.image == bird.sprites[0]:
                        bird.image = bird.sprites[1]
                    else:
                        bird.image = bird.sprites[0]
                elif event.type == ground_move and not dont_move:
                    ground.move(speedgo)
                    ground_further.move(speedgo)
                    cactus.move(speedgo)
                    cactusm.move(speedgo)
                    cactus3.move(speedgo)
                    cactusm2.move(speedgo)
                    bird.move(speedgo)
                    if ground.rect.x + ground.rect.size[0] < 0:
                        ground.rect.x = ground_further.rect.size[0]
                        xs = [randint(800, 1000) + 20 * speedgo,
                              randint(1200, 1400) + 20 * speedgo,
                              randint(1600, 1800) + 20 * speedgo,
                              randint(2000, 2200) + 20 * speedgo,
                              randint(2400, 2600) + 20 * speedgo,
                              randint(2800, 3000) + 20 * speedgo]
                        cactusmx = choice(xs)
                        del xs[xs.index(cactusmx)]
                        cactusx = choice(xs)
                        del xs[xs.index(cactusx)]
                        cactus3x = choice(xs)
                        del xs[xs.index(cactus3x)]
                        cactusm2x = choice(xs)
                        del xs[xs.index(cactusm2x)]
                        birdx = choice(xs)
                        del xs[xs.index(birdx)]
                        cactus4x = choice(xs)
                        del xs[xs.index(cactus4x)]
                        spawns = sorted([(cactusmx, 'cactusm', cactusm),
                                         (cactusx, 'cactus', cactus),
                                         (cactus3x, 'cactus3', cactus3),
                                         (cactusm2x, 'cactusm2', cactusm2),
                                         (birdx, 'bird', bird),
                                         (cactus4x, 'cactus4', cactus4)], key=lambda x: x[0])
                        for e in spawns:
                            if e[2].rect.x + e[2].rect.size[0] < 0:
                                exec(f'{e[1]}.spawn({e[0]})')
                    elif ground_further.rect.x + ground_further.rect.size[0] < 0:
                        ground_further.rect.x = ground.rect.size[0]
                        xs = [randint(800, 1000) + 20 * speedgo,
                              randint(1200, 1400) + 20 * speedgo,
                              randint(1600, 1800) + 20 * speedgo,
                              randint(2000, 2200) + 20 * speedgo,
                              randint(2400, 2600) + 20 * speedgo,
                              randint(2800, 3000) + 20 * speedgo]
                        cactusmx = choice(xs)
                        del xs[xs.index(cactusmx)]
                        cactusx = choice(xs)
                        del xs[xs.index(cactusx)]
                        cactus3x = choice(xs)
                        del xs[xs.index(cactus3x)]
                        cactusm2x = choice(xs)
                        del xs[xs.index(cactusm2x)]
                        birdx = choice(xs)
                        del xs[xs.index(birdx)]
                        cactus4x = choice(xs)
                        del xs[xs.index(cactus4x)]
                        spawns = sorted([(cactusmx, 'cactusm', cactusm),
                                         (cactusx, 'cactus', cactus),
                                         (cactus3x, 'cactus3', cactus3),
                                         (cactusm2x, 'cactusm2', cactusm2),
                                         (birdx, 'bird', bird),
                                         (cactus4x, 'cactus4', cactus4)], key=lambda x: x[0])
                        for e in spawns:
                            if e[2].rect.x + e[2].rect.size[0] < 0:
                                exec(f'{e[1]}.spawn({e[0]})')
                elif event.type == score_count and not dont_move:
                    score += 1
                    if score % 100 == 0:
                        speedgo += 1
                if characters.stolknovenie() and not dont_move:
                    dont_move = True
                    player.image = player.sprites[4]
                    screen.fill(background)
                    characters.ground_sprites.draw(screen)
                    characters.ground_sprites.update()
                    characters.cactus_sprites.draw(screen)
                    characters.cactus_sprites.update(player)
                    characters.player_sprites.draw(screen)
                    characters.player_sprites.update()
                    characters.bird_sprites.draw(screen)
                    characters.bird_sprites.update(player)
                    score_to_blit = pygame.font.Font(None, 50).render(f'{score}', True, pygame.Color('black'))
                    screen.blit(score_to_blit, (30, 50, 100, 100))
                    pygame.time.set_timer(damage, 2000)
                elif event.type == damage:
                    pygame.time.set_timer(damage, 0)
                    ground.spawn()
                    ground_further.spawn()
                    cactus.kill()
                    cactusm.kill()
                    cactus3.kill()
                    cactus4.kill()
                    cactusm2.kill()
                    bird.kill()
                    cactus.spawn(randint(500, 1200))
                    cactusm.spawn(randint(1100, 1300))
                    cactus3.spawn(randint(1500, 1700))
                    cactus4.spawn(randint(500, 1200))
                    cactusm2.spawn(randint(1850, 2050))
                    bird.spawn(randint(2200, 2300))
                    player.spawn()
                    # !!! экран проигрыша СЮДА !!!
                    main()

        if not dont_move:
            if speed < -12.5 and player.rect.y >= 253:
                pygame.time.set_timer(player_jump, 0)
                player_jumping = False
            screen.fill(background)
            characters.ground_sprites.draw(screen)
            characters.ground_sprites.update()
            characters.cactus_sprites.draw(screen)
            characters.cactus_sprites.update(player)
            characters.player_sprites.draw(screen)
            characters.player_sprites.update()
            characters.bird_sprites.draw(screen)
            characters.bird_sprites.update(player)
            score_to_blit = pygame.font.Font(None, 50).render(f'{score}', True, pygame.Color('black'))
            screen.blit(score_to_blit, (30, 50, 100, 100))
        else:
            player.image = player.sprites[4]
        if not started:
            screen.blit(pygame.font.Font(None, 50).render('Нажмите Enter, чтобы начать',
                                                          True, pygame.Color('black')), (160, 180, 300, 300))
        pygame.display.flip()
        clock.tick(60)


if __name__ == '__main__':
    main()
