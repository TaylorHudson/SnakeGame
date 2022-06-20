import pygame as pg
import random
import sys
import loads

pg.init()
pg.display.init()


# Configurações de tela
LARGURA = 500
ALTURA = 500
tela = pg.display.set_mode((LARGURA, ALTURA))
areaTela = tela.get_rect()
pg.display.set_caption("Snake Game")

# Imagens
back_ground = loads.back

btnJogar = loads.botao_jogar
areaBtnJogar = btnJogar.get_rect( x=160, y=390 )

txtGameOver = loads.txt_over

# fps
relogio = pg.time.Clock()

## Personagens do Jogo
# Snake
CIMA = 0
BAIXO = 2
DIREITA = 1
ESQUERDA = 3
PARADO = 4
corpo_snake = [[200,200], [200,210], [200,220]]
snake_skin = pg.surface.Surface((10, 10))
snake_skin.fill((255,255,255))
direcao_snake = BAIXO

# Apple
apple_skin = pg.surface.Surface((10, 10))
apple_skin.fill((255,0,0))
x, y = ((random.randint(0, 490)) // 10 * 10), ((random.randint(0, 490)) // 10 * 10)
apple_pos = (x, y)

# Main
loop = True
while loop:
    tela.fill((0,0,0))

    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()

    if areaBtnJogar.collidepoint(pg.mouse.get_pos()):
        if pg.mouse.get_pressed()[0]:

            jogando = True
            while jogando:
                tela.fill((0,0,0))
                relogio.tick(15)

                for event in pg.event.get():
                    if event.type == pg.QUIT:
                        pg.quit()
                        sys.exit()
                    else:    
                        if pg.key.get_pressed()[pg.K_UP] or pg.key.get_pressed()[pg.K_w]:
                            direcao_snake = CIMA
                        elif pg.key.get_pressed()[pg.K_DOWN] or pg.key.get_pressed()[pg.K_s]:
                            direcao_snake = BAIXO
                        elif pg.key.get_pressed()[pg.K_LEFT] or pg.key.get_pressed()[pg.K_a]:
                            direcao_snake = ESQUERDA
                        if pg.key.get_pressed()[pg.K_RIGHT] or pg.key.get_pressed()[pg.K_d]:
                            direcao_snake = DIREITA
                        if pg.key.get_pressed()[pg.K_c]:
                            direcao_snake = BAIXO
    
                if direcao_snake == CIMA:
                    corpo_snake[0] = corpo_snake[0][0], corpo_snake[0][1] - 10
                if direcao_snake == BAIXO:
                    corpo_snake[0] = corpo_snake[0][0], corpo_snake[0][1] + 10
                if direcao_snake == DIREITA:
                    corpo_snake[0] = corpo_snake[0][0] + 10, corpo_snake[0][1]
                if direcao_snake == ESQUERDA:
                    corpo_snake[0] = corpo_snake[0][0] - 10, corpo_snake[0][1]

                if corpo_snake[0][0] <= 0 or corpo_snake[0][0] >= LARGURA \
                   or corpo_snake[0][1] <= 0 or corpo_snake[0][1] >= ALTURA:

                    btnJogar2 = loads.botao_jogar
                    areaBtnJogar2 = btnJogar2.get_rect( x=160, y=390 )

                    over_loop = True
                    while over_loop:
                        tela.fill((0,0,0))

                        for event in pg.event.get():
                            if event.type == pg.QUIT:
                                pg.quit()
                                sys.exit()

                        tela.blit(txtGameOver, (35,10))

                        pg.display.update()
                        pg.display.flip()

                if corpo_snake[0][0] == apple_pos[0] and corpo_snake[0][1] == apple_pos[1]:
                    x, y = ((random.randint(0, 490)) // 10 * 10), ((random.randint(0, 490)) // 10 * 10)
                    apple_pos = (x, y)
                    corpo_snake.append((0, 0))

                for i in range(len(corpo_snake)-1, 0, -1):
                    corpo_snake[i] = (corpo_snake[i-1][0], corpo_snake[i-1][1])

                for posicao in corpo_snake:
                    tela.blit(snake_skin, posicao)
                
                tela.blit(apple_skin, (apple_pos))

                pg.display.update()
                pg.display.flip()

    tela.blit(back_ground, (0,0))
    tela.blit(btnJogar, (areaBtnJogar.x, areaBtnJogar.y))

    pg.display.update()
    pg.display.flip()
    