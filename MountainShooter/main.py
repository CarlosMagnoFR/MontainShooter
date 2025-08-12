import pygame

print('Setup Start')
pygame.init()
window = pygame.display.set_mode(size=(800, 600))  # Abrir a janela do menu inicial
print('Setup End')

print('Loop Start')
while True:
    # Checagem de todos os eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()  # fechar a janela
            quit()  #finalizar o pygame
