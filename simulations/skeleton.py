import pygame
from pygame.locals import *
from random import randint


# Main loop
def main():
    # Initialize Pygame
    pygame.init()

    # Screen dimensions
    width, height = 1920, 1080
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Skeleton")

    # Colors
    black = (0, 0, 0)
    white = (255, 255, 255)

    # Circle
    velocity = (0, 0)
    position = (width // 2, height // 2)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        # Fill screen
        screen.fill(black)

        # Circle rule
        velocity = (randint(-5, 5), randint(-5, 5))
        position = tuple(a + b for a, b in zip(position, velocity))
        pygame.draw.circle(screen, white, position, 10)

        # Update display
        pygame.display.update()


if __name__ == "__main__":
    main()
