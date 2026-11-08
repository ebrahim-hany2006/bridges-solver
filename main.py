from models.island import Island
from models.candidateBridge import CandidateBridge
from models.solution import Solution
from validators.degree_validator import check_degrees, compute_degrees

# إعداد لغز P1 القياسي
puzzle_islands = [
    Island("A", 0, 0, 2),
    Island("B", 0, 2, 2),
    Island("C", 2, 0, 2),
    Island("D", 2, 2, 2)
]

candidate_bridges = [
    CandidateBridge("E1", "A", "B", "horizontal"),
    CandidateBridge("E2", "A", "C", "vertical"),
    CandidateBridge("E3", "B", "D", "vertical"),
    CandidateBridge("E4", "C", "D", "horizontal")
]

# حل P1: Chromosome [1, 1, 1, 1]
solution = Solution.from_chromosome([1, 1, 1, 1], candidate_bridges)

print("Computed Degrees:", compute_degrees(puzzle_islands, candidate_bridges, solution))
print("Final Violations:", check_degrees(puzzle_islands, candidate_bridges, solution, mode="final"))