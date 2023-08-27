import pygame
import modules.draw_place as m_draw
import modules.screen as m_screen
import modules.on_click as m_click
import modules.button as m_button
import modules.data_base as m_data
import modules.who_victory as m_win


pygame.init()

m_screen.screen.fill((255,255,255))
m_draw.drow_place()
pygame.display.update()
pygame.display.set_caption('CROSS ZERO')

xB = 0
yB = 450

button = m_button.Button(xB, yB, 360, 60, (0,0,255), (65,105,225), "RESET")

game = True
win = True
draw = True

while game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            game = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            m_click.click_cell(x, y)
            if button.rect.collidepoint(x, y):
                button.command()
                win = True
    if m_data.step[0] == '' and win == True:
        m_win.check_who_win()
        win = False 
    if m_data.step[0] !='':
        m_win.check_draw()
    button.draw(m_screen.screen)    
    pygame.display.update()