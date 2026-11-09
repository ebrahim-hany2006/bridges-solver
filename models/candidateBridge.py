class CandidateBridge:
    def __init__(self, bridge_id: str, from_island_id: str, to_island_id: str, orientation: str):
        self.id = str(bridge_id)
        self.from_island_id = str(from_island_id)
        self.to_island_id = str(to_island_id)
        self.orientation = str(orientation)  # "horizontal" أو "vertical"

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "from": self.from_island_id,
            "to": self.to_island_id,
            "orientation": self.orientation
        }

    def __repr__(self):
        return f"CandidateBridge({self.id}: {self.from_island_id}->{self.to_island_id}, {self.orientation})"


