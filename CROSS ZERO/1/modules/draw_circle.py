import pygame
import modules.draw_place as m_draw
import modules.screen as m_screen

pygame.init()

def draw_circle(x,y):
    pygame.draw.circle(m_screen.screen, (250, 0, 0), (x, y), 50)