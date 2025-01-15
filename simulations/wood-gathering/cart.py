from item import Item


class Cart:
    def __init__(
        self,
        position: list[float, float],
        inventory_size: int,
        inventory: list[Item] = [],
    ):
        self.position = position
        self.inventory_size = inventory_size
        self.inventory = inventory
