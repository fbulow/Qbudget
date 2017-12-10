def _categoryKey(name):
    return name[3:]

def getCategory(fcn):
    keyName = _categoryKey(fcn.__name__)
    def ret(self, time, person):
        key = (keyName, time, person)
        return self.get(key,[])
    return ret
def setCategory(fcn):
    keyName = _categoryKey(fcn.__name__)
    def ret(self, time, person, ammount, comment):
        key = (keyName, time, person)
        self[key] = self.get(key, []) + [tuple([ammount, comment])]
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

