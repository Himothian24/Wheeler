import math
import pygame

class Mass():
    def __init__(self, mass, pos, size, color):
        self.mass = mass
        self.pos = pos 
        self.inertia = [0, 0]
        self.size = size       
        self.color = color
    
    def draw(self):
        pygame.draw.circle(pygame.display.get_surface(), self.color, self.pos, self.size)
        self.pos[0] += self.inertia[0]
        self.pos[1] += self.inertia[1]
        
    def force(self, v):
        self.inertia[0] += v[0] / self.mass
        self.inertia[1] += v[1] / self.mass