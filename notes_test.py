import unittest

Tc = unittest.TestCase

class Notes(dict):
    def addIncome(self, year, month, person, ammount, comment):
        self[(year, month, person)] = \
        self.getIncome(year, month, person) + [tuple([ammount, comment])]
    def getIncome(self, year, month, person):
        return self.get((year, month, person), [])

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
