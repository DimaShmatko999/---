import pygame
import modules.screen as m_scrren

pygame.init()

size_block = 100
margin = 15
heigth = size_block * 3 + margin * 4
width = size_block * 3 + margin * 4 + 150
size_window =(heigth, width)

def drow_place():
    m_scrren.screen = pygame.display.set_mode(size_window)
    for row in range(3):
        for col in range(3):
            x = col * size_block + (col + 1) * margin 
            y = row * size_block + (row + 1) * margin
            pygame.draw.rect(m_scrren.screen, (0,255,0),(x,y,size_block , size_block))
    pygame.display.update()
         