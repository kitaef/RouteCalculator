import unittest

from utils import build_graph, calculate_optimal_route

class TestTSP(unittest.TestCase):
    def setUp(self):
        self.points = [(0,0), (7,7), (3,3), (5,5), (1,1),
                       (2,2), (9,9), (4,4), (6,6), (8,8)]

    def test_optimal_route(self):
        graph = build_graph(self.points)
        optimal_route = calculate_optimal_route(graph)
        expected_route = [{'lat': 0, 'lng': 0},
                          {'lat': 1, 'lng': 1},
                          {'lat': 2, 'lng': 2},
                          {'lat': 3, 'lng': 3},
                          {'lat': 4, 'lng': 4},
                          {'lat': 5, 'lng': 5},
                          {'lat': 6, 'lng': 6},
                          {'lat': 7, 'lng': 7},
                          {'lat': 8, 'lng': 8},
                          {'lat': 9, 'lng': 9},
                          {'lat': 0, 'lng': 0}]
        self.assertEqual(optimal_route, expected_route)

if __name__ == '__main__':
    unittest.main()