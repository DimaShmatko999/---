import pygame
import modules.data_base as m_data
import modules.win_line as m_line
import modules.screen as m_screen

def victory(value):
    if m_data.list_cell[0] == value and m_data.list_cell[1] == value and m_data.list_cell[2] == value:
        m_line.draw_line(0,65,360,65)
        m_data.step[0] = ''
        return True
    elif m_data.list_cell[3] == value and m_data.list_cell[4] == value and m_data.list_cell[5] == value:
        m_line.draw_line(0,180,360,180)
        m_data.step[0] = ''
        return True
    elif m_data.list_cell[6] == value and m_data.list_cell[7] == value and m_data.list_cell[8] == value:
        m_line.draw_line(0,295,360,295)
        m_data.step[0] = ''
        return True
    elif m_data.list_cell[0] == value and m_data.list_cell[4] == value and m_data.list_cell[8] ==value:
        m_line.draw_line(0,0,360,360)
        m_data.step[0] = ''
        return True
    elif m_data.list_cell[2] == value and m_data.list_cell[4] == value and m_data.list_cell[6] ==value:
        m_line.draw_line(0,360,360,0)
        m_data.step[0] = ''
        return True
    elif m_data.list_cell[0] == value and m_data.list_cell[3] == value and m_data.list_cell[6] ==value:
        m_line.draw_line(65,0,65,360)
        m_data.step[0] = ''
        return True
    elif m_data.list_cell[1] == value and m_data.list_cell[4] == value and m_data.list_cell[7] ==value:
        m_line.draw_line(180,0,180,360)
        m_data.step[0] = ''
        return True
    elif m_data.list_cell[2] == value and m_data.list_cell[5] == value and m_data.list_cell[8] ==value:
        m_line.draw_line(295,0,295,360)
        m_data.step[0] = ''
        return True
    return False

def check_draw():
    for i in m_data.list_cell:
        if i == 0:
            return False
    font = pygame.font.Font(None, 36)
    tie_surface = font.render("DRAW", True, (255, 255, 0))
    tie_rect = tie_surface.get_rect()
    tie_rect.center = (180,400)
    m_screen.screen.blit(tie_surface, tie_rect)        
    return True

def check_who_win():
    if m_data.step[0] == '':
        if m_data.step[1] == 'zerro':
            font = pygame.font.Font(None, 36)
            tie_surface = font.render("WIN ZERRO", True, (255, 255, 0))
            tie_rect = tie_surface.get_rect()
            tie_rect.center = (180,400)
            m_screen.screen.blit(tie_surface, tie_rect)

        elif m_data.step[1] == 'cross':
            font = pygame.font.Font(None, 36)
            tie_surface = font.render("WIN CROSSES", True, (255, 255, 0))
            tie_rect = tie_surface.get_rect()
            tie_rect.center = (180,400)
            m_screen.screen.blit(tie_surface, tie_rect)  




