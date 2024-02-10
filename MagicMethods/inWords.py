
s = "magic"
print(dir(s)) # get all attributes and magic methods of object

class Row(object) :
    def __init__(self, *args):
        self.sz = len(args)
        if (self.sz>0) : self.first = args[0]
        if (self.sz>1) : self.second = args[1]
        if (self.sz>2) : self.third = args[2]
        if (self.sz>3) : self.fourth = args[3]
        if (self.sz>4) : self.fifth = args[4]

    def __len__(self):
        return self.sz

if __name__=="__main__":
    obj = Row("a", "b", "c")
    print("first ", obj.first)
    print("length ", len(obj))
    try: 
        print(obj.fifth)
    except AttributeError:
        print("got attribute error")

