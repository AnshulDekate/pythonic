
s = "magic"
print(dir(s)) # get all attributes and magic methods of object

class Row(object) :
    def __init__(self, *args):
        self.sz = len(args)
        if (self.sz>1) : self.first = args[1]
        if (self.sz>2) : self.second = args[2]
        if (self.sz>3) : self.third = args[3]
        if (self.sz>4) : self.fourth = args[4]
        if (self.sz>5) : self.fifth = args[5]

    def __len__(self):
        return self.sz

def main():
    obj = Row("a", "b", "c")
    print("first ", obj.first)
    print("length ", len(obj))
    try: 
        print(obj.fifth)
    except AttributeError:
        print("got attribute error")


if __name__=="__main__":
    main()

