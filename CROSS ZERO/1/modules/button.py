import pygame
import modules.data_base as m_bata
import modules.draw_place as m_draw

pygame.init()

class Button:
    def __init__(self, x, y, width, height, inactive_color, active_color, text='', font_size = 30):
        self.rect = pygame.Rect(x, y, width, height)
        self.inactive_color = inactive_color
        self.active_color = active_color
        self.text = text
        self.font = pygame.font.Font(None, font_size)
        self.rendered_text = self.font.render(text, True, (255, 255, 255))

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.rect)
        text_rect = self.rendered_text.get_rect(center=self.rect.center)
        surface.blit(self.rendered_text, text_rect)
    
    @property
    def color(self):
        if self.rect.collidepoint(pygame.mouse.get_pos()):
            return self.active_color
        return self.inactive_color
    
    def command(self):
        for i in range(len(m_bata.list_cell)):
            m_bata.list_cell[i] = 0
        m_draw.drow_place()
        m_bata.step= ["cross"]
        


