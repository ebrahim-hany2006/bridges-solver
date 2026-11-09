# from models.island import Island
# from models.candidateBridge import CandidateBridge
# from models.solution import Solution
# from validators.degree_validator import compute_degrees, check_degrees
# from validators.connectivity_checker import find_connected_components, is_connected

# # إعداد لغز P1 القياسي
# puzzle_islands = [
#     Island("A", 0, 0, 2),
#     Island("B", 0, 2, 2),
#     Island("C", 2, 0, 2),
#     Island("D", 2, 2, 2)
# ]

# candidate_bridges = [
#     CandidateBridge("E1", "A", "B", "horizontal"),
#     CandidateBridge("E2", "A", "C", "vertical"),
#     CandidateBridge("E3", "B", "D", "vertical"),
#     CandidateBridge("E4", "C", "D", "horizontal")
# ]

# print("==================================================")
# print("       HASHIWOKAKERO SOLVER - CONNECTIVITY DEMO   ")
# print("==================================================")

# # 1. السيناريو الأول: حل صحيح ومتصل بالكامل (P1 Canonical Solution)
# # Chromosome [1, 1, 1, 1] -> كل الجزر متصلة في مكوّن واحد
# sol_valid = Solution.from_chromosome([1, 1, 1, 1], candidate_bridges)
# print("\n[Scenario 1] Fully Connected Solution [1, 1, 1, 1]:")
# print("  - Computed Degrees:", compute_degrees(puzzle_islands, candidate_bridges, sol_valid))
# print("  - Connected Components:", find_connected_components(puzzle_islands, candidate_bridges, sol_valid))
# print("  - Is Fully Connected?:", is_connected(puzzle_islands, candidate_bridges, sol_valid))


# # 2. السيناريو الثاني: حل مقسوم لمكونين منفصلين (Split Graph)
# # Chromosome [2, 0, 0, 2] -> الجزر مقسومة لمجموعتين {A,B} و {C,D}
# sol_split = Solution.from_chromosome([2, 0, 0, 2], candidate_bridges)
# print("\n[Scenario 2] Split Solution [2, 0, 0, 2] (Should have 2 components):")
# print("  - Connected Components:", find_connected_components(puzzle_islands, candidate_bridges, sol_split))
# print("  - Is Fully Connected?:", is_connected(puzzle_islands, candidate_bridges, sol_split))


# # 3. السيناريو الثالث: كل الجزر منعزلة (All Zeros)
# # Chromosome [0, 0, 0, 0] -> 4 مكونات منفصلة
# sol_zeros = Solution.from_chromosome([0, 0, 0, 0], candidate_bridges)
# print("\n[Scenario 3] Disconnected Solution [0, 0, 0, 0] (All components separate):")
# print("  - Connected Components:", find_connected_components(puzzle_islands, candidate_bridges, sol_zeros))
# print("  - Is Fully Connected?:", is_connected(puzzle_islands, candidate_bridges, sol_zeros))
# print("\n==================================================")








from models.island import Island
from models.candidateBridge import CandidateBridge
from models.solution import Solution
from validators.solution_validator import validate_solution

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

print("==================================================")
print("     SOLUTION VALIDATOR (FINAL JUDGE) DEMO        ")
print("==================================================")

# اختبار الحل الصحيح P1 [1,1,1,1]
sol_valid = Solution.from_chromosome([1, 1, 1, 1], candidate_bridges)
print("\n[Test 1] Valid Solution [1,1,1,1]:")
print(validate_solution(puzzle_islands, candidate_bridges, sol_valid))

# اختبار حل بخطأ في الدرجات [1,0,1,1]
sol_bad_deg = Solution.from_chromosome([1, 0, 1, 1], candidate_bridges)
print("\n[Test 2] Bad Degree Solution [1,0,1,1]:")
print(validate_solution(puzzle_islands, candidate_bridges, sol_bad_deg))

# اختبار حل مقسوم لمكونين [2,0,0,2]
sol_split = Solution.from_chromosome([2, 0, 0, 2], candidate_bridges)
print("\n[Test 3] Split Network Solution [2,0,0,2]:")
print(validate_solution(puzzle_islands, candidate_bridges, sol_split))

# اختبار قيم خاطئة أو IDs غير موجودة
sol_invalid_vals = Solution({"E1": 3, "E2": 1, "E9": 1})
print("\n[Test 4] Invalid Values & Unknown IDs:")
print(validate_solution(puzzle_islands, candidate_bridges, sol_invalid_vals))
print("==================================================")