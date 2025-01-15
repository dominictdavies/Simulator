import pygame
from pygame.locals import *
from entities import Player, Tree, Cart


def main():
    # PyGame initialisation
    pygame.init()

    # Display configuration
    width, height = 1920, 1080
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Wood Gathering")

    # Entity sets
    players: list[Player] = []
    trees: list[Tree] = []
    carts: list[Cart] = []

    # Game loop
    while True:
        # Allow the application to be closed
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        # Update
        players.append(Player([width / 2, height / 2]))
        for player in players:
            player.ai()

        # Draw
        screen.fill((0, 0, 0))
        for player in players:
            player.draw(screen)
        pygame.display.update()


if __name__ == "__main__":
    main()
