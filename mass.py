# mass.py (Separate file for the Mass class)
import pygame
import math

class Mass:
    def __init__(self, mass, pos, size, color):
        self.mass = mass
        self.pos = list(pos)  # Ensure pos is a list for mutability
        self.inertia = [0, 0]
        self.size = size
        self.color = color

    def draw(self):
        pygame.draw.circle(pygame.display.get_surface(), self.color, (int(self.pos[0]), int(self.pos[1])), self.size)
        self.pos[0] += self.inertia[0]
        self.pos[1] += self.inertia[1]

    def force(self, v):
        self.inertia[0] += v[0] / self.mass
        self.inertia[1] += v[1] / self.mass

    def change_mass(self, change):
        self.mass += change
        print(self.mass)
        
    def gravity(self, m2):
        dx = self.pos[0] - m2.pos[0]
        dy = self.pos[1] - m2.pos[1]
        r = math.sqrt(dx * dx + dy * dy) * 1000

        if r == 0:
            print("Rocket got cooked")
            return

        G = 0.0000000000667430
        F = G * (self.mass * m2.mass) / (r * r)
        angle = math.atan2(dy, dx)

        self.inertia[0] -= F * math.cos(angle) / self.mass
        self.inertia[1] -= F * math.sin(angle) / self.mass
        m2.inertia[0] += F * math.cos(angle) / m2.mass
        m2.inertia[1] += F * math.sin(angle) / m2.mass
    
    