import pygame
import math

# Initialize Pygame
pygame.init()

# Set up display
width, height = 600, 600
window = pygame.display.set_mode((width, height))
pygame.display.set_caption('Windmill Animation')

# Define colors
WHITE = (255, 255, 245)
BLACK = (100, 3, 7)
BLUE = (0, 50, 125)

# Clock for controlling the frame rate
clock = pygame.time.Clock()

# Windmill center and blade dimensions
center_x, center_y = width // 2, height // 2
blade_length = 150
blade_width = 10

# Angle of rotation
angle = 0

# Function to draw windmill blades
def draw_blades(surface, x, y, length, width, angle):
    for i in range(4):  # Draw four blades, 90 degrees apart
        blade_angle = angle + i * 90
        rad_angle = math.radians(blade_angle)

        # Calculate blade end position
        end_x = x + length * math.cos(rad_angle)
        end_y = y - length * math.sin(rad_angle)

        # Draw the blade
        pygame.draw.line(surface, BLUE, (x, y), (end_x, end_y), width)

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the screen with white
    window.fill(WHITE)

    # Draw the windmill base
    pygame.draw.rect(window, BLACK, (center_x - 10, center_y, 20, 200))

    # Draw the rotating blades
    draw_blades(window, center_x, center_y, blade_length, blade_width, angle)

    # Update the angle for rotation
    angle -= 2  # Speed of rotation

    # Update the display
    pygame.display.update()

    # Control the frame rate
    clock.tick(20)

# Quit Pygame
pygame.quit()