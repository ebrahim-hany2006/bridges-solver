import unittest
from models.island import Island
from models.candidateBridge import CandidateBridge
from models.solution import Solution
from validators.degree_validator import compute_degrees, check_degrees

class TestDegreeValidator(unittest.TestCase):

    def setUp(self):
        # 1. إعداد لغز P1 المذكور بالنص في DATA_MODEL.md Section 9
        self.islands = [
            Island("A", 0, 0, 2),
            Island("B", 0, 2, 2),
            Island("C", 2, 0, 2),
            Island("D", 2, 2, 2)
        ]
        
        # 2. Candidate Bridges المرتبة E1..E4
        self.candidate_bridges = [
            CandidateBridge("E1", "A", "B", "horizontal"),
            CandidateBridge("E2", "A", "C", "vertical"),
            CandidateBridge("E3", "B", "D", "vertical"),
            CandidateBridge("E4", "C", "D", "horizontal")
        ]

    def test_canonical_p1_valid_solution(self):
        # Solution: {"E1": 1, "E2": 1, "E3": 1, "E4": 1} أو [1, 1, 1, 1]
        solution = Solution({"E1": 1, "E2": 1, "E3": 1, "E4": 1})
        
        # حساب الدرجات
        degrees = compute_degrees(self.islands, self.candidate_bridges, solution)
        self.assertEqual(degrees["A"], 2)
        self.assertEqual(degrees["B"], 2)
        self.assertEqual(degrees["C"], 2)
        self.assertEqual(degrees["D"], 2)

        # فحص عدم وجود أي degree violations في الحل النهائي
        violations = check_degrees(self.islands, self.candidate_bridges, solution, mode="final")
        self.assertEqual(len(violations), 0)

    def test_partial_mode_exceeds(self):
        # تجربة إعطاء كباري زيادات لـ A فتعدي المطلوب
        solution = Solution({"E1": 2, "E2": 1}) # A عندها 3 من 2
        violations = check_degrees(self.islands, self.candidate_bridges, solution, mode="partial")
        
        self.assertEqual(len(violations), 1)
        self.assertEqual(violations[0]["island"], "A")
        self.assertEqual(violations[0]["actual"], 3)
        self.assertEqual(violations[0]["required"], 2)

if __name__ == "__main__":
    unittest.main()