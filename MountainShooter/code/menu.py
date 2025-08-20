#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame
from pygame import Surface, Rect
from pygame.font import Font

from code.const import WIN_WIDTH, C_ORANGE, MENU_OPTION, C_WHITE, C_YELLOW


class Menu:
    def __init__(self, window):
        self.window = window
        self.surf = pygame.image.load('./asset/MenuBg.png').convert_alpha() # Carregando a imagem
        self.rect = self.surf.get_rect(left=0, top=0) # Criando um Quadrado para receber a imagem

    def run(self, ):
        menu_option = 0
        pygame.mixer_music.load('./asset/Menu.mp3') # Carregamento de Sons
        pygame.mixer_music.play(-1) # Parametro para loop infinito
        while True:
            #DESENHAR AS IMAGENS
            self.window.blit(source=self.surf, dest=self.rect)  # Direcionar a imagem para aparecer na tela
            self.menu_text(50, "Mountain", C_ORANGE, ((WIN_WIDTH / 2), 70)) # Texto Titulo do game
            self.menu_text(50, "Shooter", C_ORANGE, ((WIN_WIDTH / 2), 120)) # Texto Titulo do game

            for i in range(len(MENU_OPTION)):
                if i == menu_option:
                    self.menu_text(20, MENU_OPTION[i], C_YELLOW, ((WIN_WIDTH / 2), 200 + 25 * i))
                else:
                    self.menu_text(20, MENU_OPTION[i], C_WHITE, ((WIN_WIDTH / 2), 200 + 25 * i))

            pygame.display.flip()  # Atualizando a tela para aparecer a imagem

            # Checagem de todos os eventos
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()  # fechar a janela
                    quit()  #finalizar o pygame
                #MOVIMENTOS DO MENU - TECLADO
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN:
                        if menu_option < len(MENU_OPTION) -1: #Evento de Tecla pra baixo resetar toda vez que chegar no fim
                            menu_option += 1
                        else:
                            menu_option = 0
                    if event.key == pygame.K_UP:
                        if menu_option > 0:
                            menu_option -= 1
                        else:
                            menu_option = len(MENU_OPTION) - 1
                    if event.key == pygame.K_RETURN:
                        return MENU_OPTION[menu_option]


    ## Importando um metodo para carregar uma font como se fosse imagem
    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
        text_surf: Surface = text_font.render(str(text), True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)
