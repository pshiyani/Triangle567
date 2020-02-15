"""
Updated Jan 21, 2018
The primary goal of this file is to demonstrate a simple unittest implementation
@author: jrr
@author: rk
"""
import unittest
from Triangle_corrected import Classify_triangle

class TestTriangles(unittest.TestCase):
    

    def test_incorrect_inputs(self):
        """check that function will raises the exception properly or not when the input is not in correct format"""
        self.assertEqual(Classify_triangle( 1, 1, 'piyu'), 'InvalidInput')
        self.assertEqual(Classify_triangle('A', 'B', 'C'), 'InvalidInput')
        self.assertEqual(Classify_triangle('a', 'b', 'c'), 'InvalidInput')

    def test_not_triangle(self):
        """In this test function will tell us this is a right triangle or not"""
        self.assertEqual(Classify_triangle(0, 0, 0), 'InvalidInput')
        self.assertEqual(Classify_triangle(10.10, 10.10, -10.10), 'InvalidInput')
        self.assertNotEqual(Classify_triangle(3, 4, 5), 'NotATriangle')
        self.assertIn(Classify_triangle(1000, 1000, 2000), 'InvalidInput')
        self.assertEqual(Classify_triangle(-1, -3, -2), 'InvalidInput')
        self.assertEqual(Classify_triangle(1, 1, 3), 'NotATriangle')

    def test_equilateral(self):
        """In this test function will tell us if the triangle is equilateral or not"""
        self.assertEqual(Classify_triangle(1, 1, 1), 'Equilateral')
        self.assertEqual(Classify_triangle(11.1, 11.1, 11.1), 'Equilateral')
        self.assertNotEqual(Classify_triangle(10.11, 10.11, 10.111), 'Equilateral')
    
    def test_right_scalene(self):
        """In this test function will tell us if the triangle is right scalene or not"""
        self.assertEqual(Classify_triangle(3, 5, 4), 'Right Scalene')
        self.assertEqual(Classify_triangle(3, 4, 5), 'Right Scalene')

    def test_scalene(self):
        """In this test function will tell us if the triangle is scalene or not"""
        self.assertEqual(Classify_triangle(3, 4, 6), 'Scalene')
        self.assertNotEqual(Classify_triangle(3 * (2 ^ 64), 4 * (2 ^ 64), 5 * (2 ^ 64)),
                            'Scalene')
        self.assertEqual(Classify_triangle(10, 20, 12), 'Scalene')
        
        
    def test_right_isosceles(self):
        """In this test function will tell us if the triangle is right isosceles or not"""
        self.assertEqual(Classify_triangle(1, 1, 2 ** 0.5), 'Right Isosceles')
        self.assertNotEqual(Classify_triangle(3, 5, 5), 'Right Isosceles')
        self.assertEqual(Classify_triangle(3, 3, 4.242640687119285146), 'Right Isosceles')

    def test_isosceles(self):
        """In this test function will tell us if the triangle is isosceles or not"""
        self.assertEqual(Classify_triangle(5, 5, 6), 'Isosceles')
        self.assertEqual(Classify_triangle(123456789, 123456789, 987654321), 'InvalidInput')
        self.assertEqual(Classify_triangle(20, 20, 20), 'Equilateral')
        self.assertEqual(Classify_triangle(10, 10, 8), 'Isosceles')
        self.assertEqual(Classify_triangle(4, 4, 4.000000000000001), 'Isosceles')

if __name__ == '__main__':
    unittest.main(exit=False, verbosity=2)