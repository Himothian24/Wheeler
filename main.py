import pygame
import mass
import math

#F = G * (m1 * m2) / r^2

pygame.init()
clock = pygame.time.Clock()
f = True
screen = pygame.display.set_mode((1000,800))
pygame.display.set_caption("Rocket Simulator")

object =  mass.Mass(50, [200, 400], 50, (255,0,0))

object2 =  mass.Mass(50, [800, 400], 50, (0,255,0))

object2.force([0, -20])
if object2.pos[1] < 300:
    object2.gravity(10)

while True:
    clock.tick(100)
    screen.fill("black")

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    
    object.draw()
    object.gravity(.98)
    object2.draw()
        
    pygame.display.update()

