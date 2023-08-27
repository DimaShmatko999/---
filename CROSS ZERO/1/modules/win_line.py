import pygame
import modules.screen as m_screen

def draw_line(x,y,x1,y1):
    pygame.draw.line(m_screen.screen,(255,255,255),(x,y),(x1,y1),12)