import unittest
from models.island import Island
from models.candidateBridge import CandidateBridge
from models.solution import Solution
from validators.solution_validator import validate_solution

class TestSolutionValidator(unittest.TestCase):

    def setUp(self):
        # إعداد لغز P1 القياسي (3x3)
        self.islands = [
            Island("A", 0, 0, 2),
            Island("B", 0, 2, 2),
            Island("C", 2, 0, 2),
            Island("D", 2, 2, 2)
        ]
        
        self.candidate_bridges = [
            CandidateBridge("E1", "A", "B", "horizontal"),
            CandidateBridge("E2", "A", "C", "vertical"),
            CandidateBridge("E3", "B", "D", "vertical"),
            CandidateBridge("E4", "C", "D", "horizontal")
        ]

    def test_p1_valid_solution(self):
        # 1. P1 مع [1,1,1,1] -> valid = True
        sol = Solution.from_chromosome([1, 1, 1, 1], self.candidate_bridges)
        report = validate_solution(self.islands, self.candidate_bridges, sol)
        self.assertTrue(report["valid"])
        self.assertEqual(report["connected_components"], 1)
        self.assertEqual(len(report["degree_violations"]), 0)
        self.assertEqual(len(report["invalid_values"]), 0)

    def test_p1_degree_violation(self):
        # 2. P1 مع [1,0,1,1] -> خطأ في درجات A و C
        sol = Solution.from_chromosome([1, 0, 1, 1], self.candidate_bridges)
        report = validate_solution(self.islands, self.candidate_bridges, sol)
        self.assertFalse(report["valid"])
        self.assertTrue(len(report["degree_violations"]) > 0)
        self.assertEqual(report["connected_components"], 1)

    def test_p1_split_components_2_0_0_2(self):
        # 3. P1 مع [2,0,0,2] -> درجات سليمة لكن مكونين منفصلين
        sol = Solution.from_chromosome([2, 0, 0, 2], self.candidate_bridges)
        report = validate_solution(self.islands, self.candidate_bridges, sol)
        self.assertFalse(report["valid"])
        self.assertEqual(report["connected_components"], 2)
        self.assertEqual(len(report["degree_violations"]), 0)

    def test_p1_split_components_0_2_2_0(self):
        # 4. P1 مع [0,2,2,0] -> مكونين منفصلين
        sol = Solution.from_chromosome([0, 2, 2, 0], self.candidate_bridges)
        report = validate_solution(self.islands, self.candidate_bridges, sol)
        self.assertFalse(report["valid"])
        self.assertEqual(report["connected_components"], 2)

    def test_invalid_bridge_value(self):
        # 6. قيمة جسر خاطئة (= 3) أو ID غير موجود ("E9")
        bad_solution = Solution({"E1": 3, "E2": 1, "E3": 1, "E9": 1})
        report = validate_solution(self.islands, self.candidate_bridges, bad_solution)
        self.assertFalse(report["valid"])
        self.assertIn("E1", report["invalid_values"])
        self.assertIn("E9", report["invalid_values"])

if __name__ == "__main__":
    unittest.main()