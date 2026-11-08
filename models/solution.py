class Solution:
    def __init__(self, bridge_counts: dict = None):
        # bridge_counts: {"E1": 1, "E2": 0, "E3": 2, ...}
        self.bridge_counts = bridge_counts if bridge_counts is not None else {}

    def get_count(self, bridge_id: str) -> int:
        return self.bridge_counts.get(bridge_id, 0)

    @classmethod
    def from_chromosome(cls, chromosome: list, candidate_bridges: list):
        """تحويل Chromosome [1, 1, 1, 1] لـ Solution object بناءً على الترتيب القياسي"""
        counts = {}
        for idx, bridge in enumerate(candidate_bridges):
            counts[bridge.id] = chromosome[idx]
        return cls(counts)

    def to_dict(self) -> dict:
        return {"bridge_counts": self.bridge_counts}