# main.py (Main game file)
import pygame
import mass
import button 

# Initialize Pygame
pygame.init()

# Set up display
width, height = 1000, 800
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Rocket Simulator")

# Game variables
earth_radius = 40
earth_center_x = width / 4
earth_center_y = height / 2
earth_mass = 59720009000000000000

moon_size = 20
initial_distance = 250
moon_mass = 1000000
moon_x = earth_center_x
moon_y = earth_center_y - initial_distance

# Create Mass objects
earth = mass.Mass(earth_mass, [earth_center_x, earth_center_y], earth_radius, "blue")
moon = mass.Mass(moon_mass, [moon_x, moon_y], moon_size, "gray")
play = button.Button(300, 450, 100, 50, "Play", (0,0,255))
add = button.Button(300, 550, 100, 50, "+", (0,0,255))
sub = button.Button(300, 650, 100, 50, "-", (0,0,255))
# Apply initial force to the moon
moon.force([2900000, 0])
playing = 0
# Game loop
running = True
clock = pygame.time.Clock()

while running:
    # Clear screen
    screen.fill("black")
    play.draw()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update and draw objects
        if event.type == pygame.MOUSEBUTTONDOWN:
            
            if play.is_clicked():
                playing += 1
    if playing % 2 == 1:
        add.draw()
        sub.draw()
        earth.draw()
        earth.gravity(moon)
        moon.draw()
        if add.is_clicked():
            moon.change_mass(1000000)
    # Boundary check for moon
    if moon.pos[1] - moon.size < 0:
        moon.pos[1] = 0 + moon.size

    # Update display
    pygame.display.flip()

    # Control frame rate
    clock.tick(60)

# Quit Pygame
pygame.quit()