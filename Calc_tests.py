# -*- coding: utf-8 -*-
"""
Created on Wed Nov 28 21:17:02 2018

@author: melan
"""

import unittest
from Calc_CA5 import add, divide, exponent, multiply, subtract, squareRoot, square, pythagorus, percentage, cube

class CalculatorTest(unittest.TestCase):

    def testAdd(self):
        self.assertEqual(4, add[2,2])
        self.assertEqual(5, add[3,2])
        self.assertEqual(200, add([150,50])
        self.assertEqual(10, add([1, 2, 3, 4])
        self.assertEqual(3, add([1, 2]))
    
    def testDivide(self):
        self.assertEqual(2, divide([16, 4, 2, 1]))
        self.assertEqual(5, divide([15, 10, 5, 1])

    def testExponent(self):
        self.assertEqual(2, exponent[2,1])
        self.assertEqual(4, exponent[2,2])

    
    def testMultiply(self):
        self.assertEqual(24, multiply([1, 2, 3, 4]))
        self.assertEqual(120 , multiply([2, 3, 4, 5]))
   
    def testSubtract(self):
        self.assertEqual(9, subtract([16, 4, 2, 1]))
        self.assertEqual(5, subtract[8,3])
        self.assertEqual(8, subtract[20,12])
        self.assertEqual(200, subtract[500,300])
     
        
    def testSquareRoot(self):
        self.assertEqual(4, squareRoot[16])
        self.assertEqual(3, squareRoot[9])
        self.assertEqual(8, squareRoot[8])
        self.assertEqual(5, squareRoot[25])
        self.assertEqual(12, squareRoot[144])
       
    def testSquare(self):
        self.assertSequenceEqual([1, 4, 9, 16], square([1, 2, 3, 4]))
        self.assertSequenceEqual([3, 6, 9, 12], square([9, 36, 81, 144]))
        elf.assertEqual(4, square[2])    
          
    def testPercentage(self):
        self.assertEqual(30, percentage[18, 60])
        self.assertEqual(20, percentage[10, 50])
        self.assertEqual('0 is not allowed', percentage[2,0])
      
    def testCube(self):
        self.assertEqual([1, 8, 27, 64], cube([1, 2, 3, 4]))
        self.assertEqual(216, cube[6])
            
    def testPythagoras(self):
        self.assertEqual(8.544, pythagoras[5,7])
        self.assertEqual('0 is not allowed', pythagoras[5,0])
        self.assertEqual(11.18, pythagoras[10,5])
        
if __name__ == '__main__':
    unittest.main()
  

       
            
