import unittest

Tc = unittest.TestCase

class Notes(dict):
    def addIncome(self, year, month, person, ammount, comment):
        self[(1, year, month, person)] = \
        self.getIncome(year, month, person) + [tuple([ammount, comment])]
    def getIncome(self, year, month, person):
        return self.get((1, year, month, person), [])
    def addMutualExpense(self, year, month, person, ammount, comment):
        self[(2, year, month, person)] = \
        self.getMutualExpense(year, month, person) + [tuple([ammount, comment])]
    def getMutualExpense(self, year, month, person):
        return self.get((2, year, month, person), [])

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
