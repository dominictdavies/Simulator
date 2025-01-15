from item import Item
import random
import pygame


class Player:
    def __init__(
        self,
        position: list[float, float] = (0, 0),
        velocity: list[float, float] = (0, 0),
        move_speed: float = 1.0,
        chop_speed: float = 1.0,
        inventory_size: int = 10,
        inventory: list[Item] = []
    ):
        self.position = position
        self.velocity = velocity
        self.move_speed = move_speed
        self.chop_speed = chop_speed
        self.inventory_size = inventory_size
        self.inventory = inventory

    def ai(self):
        self.velocity = (random.randint(-25, 25), random.randint(-25, 25))
        self.position[0] += self.velocity[0]
        self.position[1] += self.velocity[1]

    def draw(self, screen):
        white = (255, 255, 255)
        pygame.draw.circle(screen, white, self.position, 10)
