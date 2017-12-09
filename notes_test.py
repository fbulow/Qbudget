import unittest

Tc = unittest.TestCase

def categoryKey(name):
    return name[3:]

def getCategory(fcn):
    key = categoryKey(fcn.__name__)
    def ret(self, year, month, person):
        return self.get((key, year, month, person),[])
    return ret
def setCategory(fcn):
    key = categoryKey(fcn.__name__)
    def ret(self, year, month, person, ammount, comment):
        self[(key, year, month, person)] = self.get(key, []) + [tuple([ammount, comment])]
    return ret


class Notes(dict):
    @setCategory
    def addIncome(self, year, month, person, ammount, comment):pass
    @getCategory
    def getIncome(self, year, month, person):pass
    @setCategory
    def addMutualExpense(self, year, month, person, ammount, comment):pass
    @getCategory
    def getMutualExpense(self, year, month, person):pass

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
