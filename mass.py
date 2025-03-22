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
    
    def gravity(self, gravity):
        y_velocity = 0
        y_velocity += gravity
        self.pos[1] += y_velocity

        if self.pos[1] + self.size > 800:
            self.pos[1] = 800 - self.size
            y_velocity = 0