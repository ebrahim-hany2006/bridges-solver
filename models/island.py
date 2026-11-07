class Island:
    def __init__(self, island_id, x, y, degree):
        self.id = island_id
        self.x = x
        self.y = y
        self.degree = degree

    def __repr__(self):
        return f"Island({self.id}, degree={self.degree})"