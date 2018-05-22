# Tests

import unittest
import algo

class methodTest(unittest.TestCase):

    def test_extEu(self):
        self.assertEqual(algo.ExtendedEuclid(1324,439),(1,-188,567))
        self.assertEqual(algo.ExtendedEuclid(20,30),(10,-1,1))
        self.assertEqual(algo.ExtendedEuclid(5,7),(1,3,-2))

    def test_Congruence(self):
        self.assertEqual(algo.Linear_Congruence_Solver(4,26,22),[1,12])
        self.assertEqual(algo.Linear_Congruence_Solver(14,30,100),[95,45])
        self.assertEqual(algo.Linear_Congruence_Solver(256,179,337),[81])
        self.assertEqual(algo.Linear_Congruence_Solver(1215,560,2755),[200,751,1302,1853,2404])
        self.assertEqual(algo.Linear_Congruence_Solver(1296,1105,2413),[1630])

    def test_Inverse(self):
        self.assertEqual(algo.MultInverse(9,33),None)
        self.assertEqual(algo.MultInverse(5,7),3)
        self.assertEqual(algo.MultInverse(3,7),5)
        self.assertEqual(algo.MultInverse(2,11),6)

    def test_SystemSolver1(self):
        A = [2,3,2]
        M = [3,5,7]
        self.assertEqual(algo.Linear_Congruence_System_Solver(A,M),23)

    def test_SystemSolver2(self):
        A = [2,3]
        M = [5,13]
        self.assertEqual(algo.Linear_Congruence_System_Solver(A,M),42)
        
if __name__ == '__main__':
    unittest.main()
