from collections import namedtuple

Key = namedtuple("Key", "label, time, person")

def upFirstLetter(words):
    return words[:1].upper()+words[1:]

def defLabel(fcn):
    def ret(notes, label):
        assert(label == upFirstLetter(label))
        return fcn(notes, label)
    return ret

@defLabel            
def defAdd(notes, label):
    def adder(self, time, person, ammount, comment):
        key = Key(label, time, person)
        self[key] = self.get(key, []) + [tuple([ammount, comment])]
    setattr(notes,
             "add"+label,
             adder)
    
@defLabel            
def defGet(notes, label):
    def getter(self, time, person):
        return self.get(Key(label, time, person), [])
    setattr(notes,
             "get"+label,
             getter)
    
@defLabel            
def defCategory(notes, label):
    defGet(notes, label)
    defAdd(notes, label)

class Notes(dict):
    def __init__(self):
        defCategory(Notes, "Income")
        defCategory(Notes, "MutualExpense")

    def totalIncome(self, time):
        return sum(
            sum(x[0] for x in v) for k, v  in self.items() if k.time==time)
            
    def owes(self, time, person):
        return 1.0;
