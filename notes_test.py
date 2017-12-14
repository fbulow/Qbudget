import unittest
Tc = unittest.TestCase

from notes import *

def Month(*arg):
    return tuple(arg)




def addMultipleIncome(notes, time):
    notes.addIncome(
        time = time,
        person = "Fredrik",
        ammount = 6000.00,
        comment = "CSNA")
    
    notes.addIncome(
        time = time,
        person = "Fredrik",
        ammount = 3000.00,
        comment = "CSNB")

    notes.addIncome(
        time = time,
        person = "Fredrik",
        ammount = 3000.00,
        comment = "CSNC")
    
class TestTransaction(Tc):
    def test_bowing(self):
        sut=Notes()
        time = Month(2012,5)
        sut.addIncome(
            time = time,
            person = "Fredrik",
            ammount = 10.00,
            comment = "Expense comment")

        sut.addIncome(
            time = time,
            person = "Helen",
            ammount = 1.00,
            comment = "Expense comment")

        sut.addMutualExpense(
            time = time,
            person = "Fredrik",
            ammount = 10.00,
            comment = "Expense comment")

        sut.addMutualExpense(
            time = time,
            person = "Helen",
            ammount = 1.00,
            comment = "Expense comment")

        self.assertEqual(
            sut.owes(time, "Helen"),
            0.0)
        
        self.assertEqual(
            sut.owes(time, "Fredrik"),
            0.0)
        
    def test_totalIncome(self):
        time = Month(2012,5)
        sut = Notes()

        sut.addIncome(time, "Fredrik",  1000.00, "A")
        sut.addIncome(time, "Helen",    2000.00, "B")
        sut.addIncome(time, "Freddrik",   20.00, "C")

        self.assertEqual( sut.totalIncome(time), 3020.00)
        
        
    def test_helen_and_fredrik_NoMix(self):
        time = Month(2012,5)
        sut=Notes()
        
        sut.addMutualExpense(
            time = time,
            person = "Fredrik",
            ammount = 1.00,
            comment = "Expense comment")

        sut.addMutualExpense(
            time = time,
            person = "Helen",
            ammount = 2.00,
            comment = "Expense comment")

        self.assertEqual(sut.getMutualExpense(
            time = time,
            person = "Fredrik"),
        [(1.00, "Expense comment")])
        self.assertEqual(sut.getMutualExpense(
            time = time,
            person = "Helen"),
        [(2.00, "Expense comment")])
        

    def test_multipleItems_NoMix(self):
        time = Month(2012,5)
        sut=Notes()
        
        addMultipleIncome(sut, time)
        sut.addMutualExpense(
            time = time,
            person = "Fredrik",
            ammount = 1.00,
            comment = "Expense comment")
        
        self.assertEqual(sut.getMutualExpense(
            time = time,
            person = "Fredrik"),
        [(1.00, "Expense comment")])
        
        self.assertEqual(sut.getIncome(
            time = time,
            person = "Fredrik"),
                         [(6000.00, "CSNA"),
                          (3000.00, "CSNB"),
                          (3000.00, "CSNC")])
        
    def test_multipleItems(self):
        time = Month(2012,5)
        sut=Notes()
        
        addMultipleIncome(sut, time)
        
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
