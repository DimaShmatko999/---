import pygame 
import modules.draw_place as m_draw
import modules.screen as m_screen

pygame.init()

def draw_crosses(lt,ld,rt,rd):
    pygame.draw.line(m_screen.screen, (0, 0, 255), (lt), (rd), 7)
    pygame.draw.line(m_screen.screen, (0, 0, 255), (ld), (rt), 7)