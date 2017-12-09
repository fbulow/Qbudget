def _categoryKey(name):
    return name[3:]

def getCategory(fcn):
    key = _categoryKey(fcn.__name__)
    def ret(self, year, month, person):
        return self.get((key, year, month, person),[])
    return ret
def setCategory(fcn):
    key = _categoryKey(fcn.__name__)
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

