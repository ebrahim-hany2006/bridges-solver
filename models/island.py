class Island:
    def __init__(self, island_id: str, row: int, col: int, required_bridges: int):
        self.id = str(island_id)
        self.row = int(row)
        self.col = int(col)
        self.required_bridges = int(required_bridges)

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "row": self.row,
            "col": self.col,
            "required_bridges": self.required_bridges
        }

    def __repr__(self):
        return f"Island({self.id}, row={self.row}, col={self.col}, req={self.required_bridges})"