import unittest
from models.island import Island
from models.candidateBridge import CandidateBridge
from models.solution import Solution
from validators.connectivity_checker import find_connected_components, is_connected

class TestConnectivityChecker(unittest.TestCase):

    def setUp(self):
        # إعداد لغز P1 القياسي
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

    def test_p1_all_ones_connected(self):
        # [1, 1, 1, 1] -> مكون واحد {A, B, C, D}
        sol = Solution.from_chromosome([1, 1, 1, 1], self.candidate_bridges)
        comps = find_connected_components(self.islands, self.candidate_bridges, sol)
        self.assertEqual(len(comps), 1)
        self.assertTrue(is_connected(self.islands, self.candidate_bridges, sol))

    def test_two_components_split_horizontal(self):
        # [2, 0, 0, 2] -> مكونين: {A,B} و {C,D}
        sol = Solution.from_chromosome([2, 0, 0, 2], self.candidate_bridges)
        comps = find_connected_components(self.islands, self.candidate_bridges, sol)
        self.assertEqual(len(comps), 2)
        self.assertFalse(is_connected(self.islands, self.candidate_bridges, sol))

    def test_two_components_split_vertical(self):
        # [0, 2, 2, 0] -> مكونين: {A,C} و {B,D}
        sol = Solution.from_chromosome([0, 2, 2, 0], self.candidate_bridges)
        comps = find_connected_components(self.islands, self.candidate_bridges, sol)
        self.assertEqual(len(comps), 2)
        self.assertFalse(is_connected(self.islands, self.candidate_bridges, sol))

    def test_partial_split_three_and_one(self):
        # [1, 1, 0, 0] -> مكونين: {A, B, C} و {D}
        sol = Solution.from_chromosome([1, 1, 0, 0], self.candidate_bridges)
        comps = find_connected_components(self.islands, self.candidate_bridges, sol)
        self.assertEqual(len(comps), 2)
        self.assertFalse(is_connected(self.islands, self.candidate_bridges, sol))

    def test_all_zeros_four_components(self):
        # [0, 0, 0, 0] -> 4 مكونات (كل جزيرة لوحدها)
        sol = Solution.from_chromosome([0, 0, 0, 0], self.candidate_bridges)
        comps = find_connected_components(self.islands, self.candidate_bridges, sol)
        self.assertEqual(len(comps), 4)
        self.assertFalse(is_connected(self.islands, self.candidate_bridges, sol))

    def test_single_island_puzzle(self):
        single_island = [Island("A", 0, 0, 0)]
        sol = Solution({})
        comps = find_connected_components(single_island, [], sol)
        self.assertEqual(len(comps), 1)
        self.assertTrue(is_connected(single_island, [], sol))

if __name__ == "__main__":
    unittest.main()