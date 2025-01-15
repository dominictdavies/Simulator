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
    players: list[Player] = [Player([width // 2, height // 2])]
    trees: list[Tree] = [
        Tree([width // 2, height // 3]),
        Tree([width // 3, height // 3 * 2]),
        Tree([width // 3 * 2, height // 3 * 2]),
    ]
    carts: list[Cart] = [Cart([width // 2, height // 2])]

    # Game loop
    while True:
        # Allow the application to be closed
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        # Update
        for player in players:
            player.ai()
        for tree in trees:
            tree.ai()
        for cart in carts:
            cart.ai()

        # Draw
        screen.fill((0, 0, 0))
        for player in players:
            player.draw(screen)
        for tree in trees:
            tree.draw(screen)
        for cart in carts:
            cart.draw(screen)
        pygame.display.update()


if __name__ == "__main__":
    main()
