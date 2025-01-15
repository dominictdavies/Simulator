import pygame
import random


class Entity:
    def __init__(
        self,
        position: list[float] = None,
        velocity: list[float] = None,
        colour: tuple[int, int, int] = (255, 255, 255),
        radius: float = 5.0,
    ):
        self.position = position if position is not None else [0.0, 0.0]
        self.velocity = velocity if velocity is not None else [0.0, 0.0]
        self.colour = colour
        self.radius = radius

    def ai(self):
        pass

    def draw(self, screen):
        pygame.draw.circle(screen, self.colour, self.position, self.radius)


class Item(Entity):
    def __init__(
        self,
        position: list[float] = None,
        velocity: list[float] = None,
        colour: tuple[int, int, int] = (128, 128, 128),
        radius: float = 5.0,
        name: str = "",
        stack: int = 0,
    ):
        super().__init__(position, velocity, colour, radius)
        self.name = name
        self.stack = stack


class Player(Entity):
    def __init__(
        self,
        position: list[float] = None,
        velocity: list[float] = None,
        colour: tuple[int, int, int] = (255, 255, 255),
        radius: float = 5.0,
        inventory: list[Item] = [],
    ):
        super().__init__(position, velocity, colour, radius)
        self.inventory = inventory

    def ai(self):
        self.velocity = (random.randint(-5, 5), random.randint(-5, 5))
        self.position[0] += self.velocity[0]
        self.position[1] += self.velocity[1]


class Tree(Entity):
    def __init__(
        self,
        position: list[float] = None,
        velocity: list[float] = None,
        colour: tuple[int, int, int] = (0, 255, 0),
        radius: float = 7.5,
        life: int = 10,
        wood: int = 10,
    ):
        super().__init__(position, velocity, colour, radius)
        self.life = life
        self.wood = wood


class Cart(Entity):
    def __init__(
        self,
        position: list[float] = None,
        velocity: list[float] = None,
        colour: tuple[int, int, int] = (255, 165, 0),
        radius: float = 5.0,
        inventory: list[Item] = [],
    ):
        super().__init__(position, velocity, colour, radius)
        self.inventory = inventory
