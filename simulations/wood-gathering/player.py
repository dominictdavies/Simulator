from item import Item


class Player:
    def __init__(
        self,
        position: tuple[float, float],
        move_speed: float,
        chop_speed: float,
        inventory_size: int,
        inventory: list[Item] = [],
    ):
        self.position = position
        self.move_speed = move_speed
        self.chop_speed = chop_speed
        self.inventory_size = inventory_size
        self.inventory = inventory
