class Item:
    def __init__(self, name: str, max_stack: int, stack: int = 0):
        self.name = name
        self.max_stack = max_stack
        self.stack = stack
