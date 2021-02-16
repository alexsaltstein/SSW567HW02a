# -*- coding: utf-8 -*-
"""
Updated Jan 21, 2018
The primary goal of this file is to demonstrate a simple unittest implementation

@author: jrr
@author: rk
"""

import unittest

from Triangle import classifyTriangle

# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework

class TestTriangles(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin

    def testRightTriangleA(self): 
        self.assertEqual(classifyTriangle(3,4,5),'Right','3,4,5 is a Right triangle')

    def testRightTriangleB(self): 
        self.assertEqual(classifyTriangle(5,3,4),'Right','5,3,4 is a Right triangle')
        
    def testEquilateralTriangles(self): 
        self.assertEqual(classifyTriangle(1,1,1),'Equilateral','1,1,1 should be equilateral')
    
    def testIsoscelesTriangles(self): 
        self.assertEqual(classifyTriangle(3,2,2),'Isoceles','3,2,2 should be isoceles')
    
    def testInvalidInput(self): 
        self.assertEqual(classifyTriangle('a',1,'bad'),'InvalidInput','a,1,bad should be InvalidInput')

    def testLowInteger(self): 
        self.assertEqual(classifyTriangle(-1,-50,1),'InvalidInput','-1,-50,1 should be InvalidInput')

    def testScaleneTriangles(self): 
        self.assertEqual(classifyTriangle(7,9,10),'Scalene','7,9,10 should be Scalene')

    def testBigNumbers(self): 
        self.assertNotEqual(classifyTriangle(2000,1000,201),'Scalene','2000,1000,201 should not be Scalene')

    def testNotATriangle(self): 
        self.assertEqual(classifyTriangle(1,9,10),'NotATriangle','1,9,10 should be NotATriangle')

    def testBigEquilateralTriangles(self): 
        self.assertEqual(classifyTriangle(199,199,199),'Equilateral','199,199,199 should be Equilateral')

if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()

