import pygame as pg
import os

pg.init()

caminho_imagens = os.path.join(os.getcwd(),"Snake/imagem")

back = pg.image.load(os.path.join(caminho_imagens,"snake_back.png"))
botao_jogar = pg.image.load(os.path.join(caminho_imagens,"btnJogar.png"))
txt_over = pg.image.load(os.path.join(caminho_imagens,"game_over.png"))