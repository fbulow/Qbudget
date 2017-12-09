def _categoryKey(name):
    return name[3:]

def getCategory(fcn):
    key = _categoryKey(fcn.__name__)
    def ret(self, time, person):
        return self.get((key, time, person),[])
    return ret
def setCategory(fcn):
    key = _categoryKey(fcn.__name__)
    def ret(self, time, person, ammount, comment):
        self[(key, time, person)] = self.get(key, []) + [tuple([ammount, comment])]
    return ret


class Notes(dict):
    @setCategory
    def addIncome(self, time, person, ammount, comment):pass
    @getCategory
    def getIncome(self, time, person):pass
    
    @setCategory
    def addMutualExpense(self, time, person, ammount, comment):pass
    @getCategory
    def getMutualExpense(self, time, person):pass

