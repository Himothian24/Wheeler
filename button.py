import pygame

class Button():
    def __init__(self, x, y, width, height, text, color):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        size = 25 - (len(self.text) // 10)  
        self.font = pygame.font.Font(None, size)
        self.text_surf = self.font.render(self.text, True, (255, 255, 255)) 
        self.text_rect = self.text_surf.get_rect(center=self.rect.center)  
        self.color = color
        

    def draw(self):
        pygame.draw.rect(pygame.display.get_surface(), self.color, self.rect) 
        pygame.display.get_surface().blit(self.text_surf, self.text_rect) 

    def is_clicked(self):
        if self.rect.collidepoint(pygame.mouse.get_pos()):
            return True
        return False
    