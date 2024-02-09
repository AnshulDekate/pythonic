a = ["a", "b", "c"]
print(dir(a))

class customList:  
    values = []  
    def __init__(self, data):
        self.values = data

    def __repr__(self) -> str:
        ret = ""
        for val in self.values :
            ret += " " + val
        ret = ret.strip()
        return ret
    
    # += opertor, appends the whole string instead of appending each char in string
    def __iadd__(self, s) : 
        self.values.append(s)
        return self     
    
     # *= operator, appends the whole string to each element instead of duplicating the list
    def __imul__(self, s) :
        for idx, _ in enumerate(self.values):
            self.values[idx] += s
        return self
    
if __name__=="__main__":
    obj = customList(["a", "b", "c"])
    print(obj)
    obj += "d"
    print(obj)
    obj *= "e"
    print(obj)