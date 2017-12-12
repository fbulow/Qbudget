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
        key = tuple([label, time, person])
        self[key] = self.get(key, []) + [tuple([ammount, comment])]
    setattr(notes,
             "add"+label,
             adder)
    
@defLabel            
def defGet(notes, label):
    def getter(self, time, person):
        key = tuple([label, time, person])
        return self.get(key, [])
    setattr(notes,
             "get"+label,
             getter)
    
@defLabel            
def defCategory(notes, label):
    defGet(notes, label)
    defAdd(notes, label)

class Notes(dict):
    pass

defCategory(Notes, "Income")
defCategory(Notes, "MutualExpense")
