import pygame
import sqlite3

def main(score):
    screen = pygame.display.set_mode((800, 600))
    background = pygame.Color('grey')
    screen.fill(background)
    font = pygame.font.Font(None, 32)
    input_box = pygame.Rect(300, 300, 140, 32)
    color_inactive = pygame.Color('black')
    color_active = pygame.Color('black')
    new_game = font.render('ВВЕДИТЕ ВАШЕ ИМЯ', True, pygame.Color('black'))
    screen.blit(new_game, (272, 250, 500, 500))

    logo = pygame.font.Font(None, 100).render('ВЫ   ПРОИГРАЛИ!!!', True, pygame.Color('black'))
    screen.blit(logo, (60, 75, 300, 200))
    score = str(score)
    f = 'Ваш счёт ' + score
    scores = font.render(f, True, pygame.Color('black'))
    screen.blit(scores, (327, 360, 500, 500))
    color = color_inactive
    active = False
    text = ''
    done = False

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                if input_box.collidepoint(event.pos):
                    active = not active
                else:
                    active = False
                color = color_active if active else color_inactive
            if event.type == pygame.KEYDOWN:
                if active:
                    if event.key == pygame.K_RETURN:
                        con = sqlite3.connect('data/leaderboard.sqlite')
                        cur = con.cursor()
                        players = cur.execute("""SELECT * FROM scores""").fetchall()
                        con.close()
                        
                        # тут надо сделать адекватные замены, но на пальцах вроде бы работает
                        
                        for player in players:
                            if text == player[1] and score > player[2]:
                                player[1] = text
                                player[2] = score
                            elif text == player[1] and score > player[2]:
                                pass
                            elif score > player[2]:
                                player[1] = text
                                player[2] = score
                        for player in players:
                            for player1 in players:
                                if player1[0] > player[0] and player1[2] < player[2]:
                                    x = player[0]
                                    player[0] = player1[0]
                                    player1[0] = x
                                elif player1[0] < player[0] and player1[2] > player[2]:
                                    x = player[0]
                                    player[0] = player1[0]
                                    player1[0] = x
                                
                                
                        text = ''
                        done = True
                    elif event.key == pygame.K_BACKSPACE:
                        text = text[:-1]
                    else:
                        text += event.unicode

        txt_surface = font.render(text, True, color)
        width = max(200, txt_surface.get_width()+10)
        input_box.w = width
        screen.blit(txt_surface, (input_box.x+5, input_box.y+5))
        pygame.draw.rect(screen, color, input_box, 2)

        pygame.display.flip()


if __name__ == '__main__':
    pygame.init()
    main()
    pygame.quit()
