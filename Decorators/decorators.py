def custom_decorator(func):
    def wrapper(*args, **kwargs):
        print("action before")
        ret = func(*args, **kwargs)
        print("action after")
        return ret
    return wrapper

class CustomAdder():
    a = 4
    b = 5

    def __init__ (self, *args):
        self.values = []
        for val in args:
            self.values.append(val)

    @staticmethod
    def sAdd(*args):
        ans = 0
        for val in args:
            print(val, type(val))
            ans += val
        return ans
    
    @classmethod
    def cAdd(cls, *args):
        ans = cls.a + cls.b
        for val in args:
            ans += val
        return ans
    
    @property
    def sum(self):
        ans = self.a + self.b
        for val in self.values:
            ans += val
        return ans
    
    @custom_decorator
    def __repr__(self) -> str:
        print("action")
        ans = ""
        ans += str(self.a) + " "
        ans += str(self.b) + " "
        for val in self.values:
            ans += str(val) + " "
        return ans
    
if __name__=="__main__":
    print(CustomAdder.sAdd(2, 3, 5))
    print(CustomAdder.cAdd(2, 3, 5))
    obj = CustomAdder(2, 3, 5)
    print(obj.sum)
    print(obj)

    
    
