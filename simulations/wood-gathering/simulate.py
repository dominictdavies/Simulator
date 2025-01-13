import pygame
from pygame.locals import *


# Main loop
def main():
    # Initialize Pygame
    pygame.init()

    # Screen dimensions
    width, height = 1920, 1080
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Wood Gathering")

    # Colors
    black = (0, 0, 0)
    white = (255, 255, 255)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        # Fill screen
        screen.fill(black)
        pygame.draw.circle(screen, white, (width // 2, height // 2), 10)

        # Update display
        pygame.display.update()


if __name__ == "__main__":
    main()
