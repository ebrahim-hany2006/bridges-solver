class Bridge:
    def __init__(self, island1, island2, count):
        self.island1 = island1
        self.island2 = island2
        self.count = count

    def __repr__(self):
        return (
            f"Bridge({self.island1.id}, "
            f"{self.island2.id}, {self.count})"
        )