import unittest
Tc = unittest.TestCase

from notes import *

class NoMixing(Tc):
    def test_logged(self):
        sut = Notes()
        sut.addMutualExpense(
            year = 2012,
            month = 5,
            person = "Fredrik",
            ammount = 6000.00,
            comment = "CSN")
        
        self.assertEqual(
            sut.getIncome(
                year = 2012,
                month = 5,
                person = "Fredrik"),
                [])

class MutualExpense(Tc):
    def test_logged(self):
        sut = Notes()
        sut.addMutualExpense(
            year = 2012,
            month = 5,
            person = "Fredrik",
            ammount = 6000.00,
            comment = "CSN")
        
        self.assertEqual(
            sut.getMutualExpense(
                year = 2012,
                month = 5,
                person = "Fredrik"),
            [(6000.00, "CSN")])

        self.assertEqual(
            sut.getMutualExpense(
                year = 2012,
                month = 6,
                person = "Fredrik"),
                [])
        
        self.assertEqual(
            sut.getMutualExpense(
                year = 2014,
                month = 5,
                person = "Fredrik"),
                [])
        
        self.assertEqual(
            sut.getMutualExpense(
                year = 2014,
                month = 6,
                person = "Fredrik"),
                [])

    
class IncomeEntry(Tc):
    def test_logged(self):
        sut = Notes()
        sut.addIncome(
            year = 2012,
            month = 5,
            person = "Fredrik",
            ammount = 6000.00,
            comment = "CSN")
        
        self.assertEqual(
            sut.getIncome(
                year = 2012,
                month = 5,
                person = "Fredrik"),
            [(6000.00, "CSN")])

        self.assertEqual(
            sut.getIncome(
                year = 2012,
                month = 6,
                person = "Fredrik"),
                [])
        
        self.assertEqual(
            sut.getIncome(
                year = 2014,
                month = 5,
                person = "Fredrik"),
                [])
        
        self.assertEqual(
            sut.getIncome(
                year = 2014,
                month = 6,
                person = "Fredrik"),
                [])
    
if __name__ == "__main__":
    unittest.main()
