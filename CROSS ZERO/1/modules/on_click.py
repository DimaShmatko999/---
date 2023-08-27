import pygame
import modules.who_turn as m_turn

pygame.init()

def click_cell(x, y):
    if y > 15 and y < 115:
        if x > 15 and x < 115:
            m_turn.who_turn(115, 115, 0)
            print(x,y)
        elif x > 130 and x < 230:
            m_turn.who_turn(230, 115, 1)
        elif x > 230 and x < 330:
            m_turn.who_turn(345, 115, 2)
    elif y > 130 and y < 230:
        if x > 15 and x < 115:
            m_turn.who_turn(115,230, 3)
        elif x > 130 and x < 230:
            m_turn.who_turn(230, 230, 4)
        elif x > 230 and x < 330:
            m_turn.who_turn(345, 230, 5) 
    elif y > 230 and y < 330:
        if x > 15 and x < 115:
            m_turn.who_turn(115,345, 6)
        elif x > 130 and x < 230:
            m_turn.who_turn(230,345, 7)
        elif x > 230 and x < 330:
            m_turn.who_turn(345,345, 8)