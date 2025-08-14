#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame
from pygame import Surface, Rect
from pygame.font import Font

from code.const import WIN_WIDTH, COLOR_ORANGE, MENU_OPTION, COLOR_WHITE


class Menu:
    def __init__(self, window):
        self.window = window
        self.surf = pygame.image.load('./asset/MenuBg.png') # Carregando a imagem
        self.rect = self.surf.get_rect(left=0, top=0) # Criando um Quadrado para receber a imagem

    def run(self, ):
        pygame.mixer_music.load('./asset/Menu.wav') # Carregamento de Sons
        pygame.mixer_music.play(-1) # Parametro para loop infinito
        while True:
            self.window.blit(source=self.surf, dest=self.rect)  # Direcionar a imagem para aparecer na tela
            self.menu_text(50, "Mountain", COLOR_ORANGE , ((WIN_WIDTH / 2), 70)) # Texto Titulo do game
            self.menu_text(50, "Shooter", COLOR_ORANGE , ((WIN_WIDTH / 2), 120)) # Texto Titulo do game

            for i in range(len(MENU_OPTION)):
                self.menu_text(20, MENU_OPTION[i], COLOR_WHITE ,  ((WIN_WIDTH / 2), 200 + 25 * i))

            pygame.display.flip()  # Atualizando a tela para aparecer a imagem

            # Checagem de todos os eventos
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()  # fechar a janela
                    quit()  #finalizar o pygame

    ## Importando um metodo para carregar uma font como se fosse imagem
    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
        text_surf: Surface = text_font.render(str(text), True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)
