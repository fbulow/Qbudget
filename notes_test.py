import unittest
Tc = unittest.TestCase

from notes import *

def Month(*arg):
    return tuple(arg)
        
class TestTransaction(Tc):
    def test_multipleItems(self):
        time = Month(2012,5)
        
        sut=Notes()
        sut.addIncome(
            time = time,
            person = "Fredrik",
            ammount = 6000.00,
            comment = "CSNA")
        
        sut.addIncome(
            time = time,
            person = "Fredrik",
            ammount = 3000.00,
            comment = "CSNB")
        
        sut.addIncome(
            time = time,
            person = "Fredrik",
            ammount = 3000.00,
            comment = "CSNC")
        
        ret = sut.getIncome(
            time = time,
            person = "Fredrik")
        
        self.assertEqual(ret,
                         [(6000.00, "CSNA"),
                          (3000.00, "CSNB"),
                          (3000.00, "CSNC")])

class NoMixing(Tc):
    def test_logged(self):
        sut = Notes()
        sut.addMutualExpense(
            time = Month(2012,5),
            person = "Fredrik",
            ammount = 6000.00,
            comment = "CSN")
        
        self.assertEqual(
            sut.getIncome(
                time = Month(2012,5),
                person = "Fredrik"),
                [])

class MutualExpense(Tc):
    def test_logged(self):
        sut = Notes()
        sut.addMutualExpense(
            time = Month(2012, 5),
            person = "Fredrik",
            ammount = 6000.00,
            comment = "CSN")
        
        self.assertEqual(
            sut.getMutualExpense(
                time = Month(2012, 5),
                person = "Fredrik"),
            [(6000.00, "CSN")])

        self.assertEqual(
            sut.getMutualExpense(
                time = Month(2012, 6),
                person = "Fredrik"),
                [])
        
        self.assertEqual(
            sut.getMutualExpense(
                time = Month(2014, 5),
                person = "Fredrik"),
                [])
        
        self.assertEqual(
            sut.getMutualExpense(
                time = Month(2014, 6),
                person = "Fredrik"),
                [])

    
class IncomeEntry(Tc):
    def test_logged(self):
        sut = Notes()
        sut.addIncome(
            time = Month(2012, 5),
            person = "Fredrik",
            ammount = 6000.00,
            comment = "CSN")
        
        self.assertEqual(
            sut.getIncome(
                time = Month(2012, 5),
                person = "Fredrik"),
            [(6000.00, "CSN")])

        self.assertEqual(
            sut.getIncome(
                time = Month(2012, 6),
                person = "Fredrik"),
                [])
        
        self.assertEqual(
            sut.getIncome(
                time = Month(2014, 5),
                person = "Fredrik"),
                [])
        
        self.assertEqual(
            sut.getIncome(
                time = Month(2014, 6),
                person = "Fredrik"),
                [])
    
if __name__ == "__main__":
    unittest.main()
