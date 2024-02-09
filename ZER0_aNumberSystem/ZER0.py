'''
Introducing a ZER0 number system for fun, it combines the Hindu-Arabic numeral system (0-9) and Roman System.
We use placeholder technique from Hindu-Arabic numeral system with Roman system,
using 4 chars, to represent each power of 10. 

Roman system is like using 3 symbols to represent 10 numbers repeateadly but doesn't use any placeholders 
And because it doesn't use any placeholders, it would require infinite number of symbols to represent infinite numbers.

With ZER0 number system we can represent infinite numbers with just 4 symbols while adopting the Roman system.

Z - 1
E - 5
R - 10
0 - placeholder

Reference:
    1e3	1e2	 1e1  1
1	M	C	 X	  I
2	MM	CC	 XX	  II
3	MMM	CCC	 XXX  III
4		CD	 XL	  IV
5		D	 L	  V
6		DC	 LX	  VI
7		DCC	 LXX  VII
8		DCCC LXXX VIII
9		CM	 XC	  IX
'''

class ZER0:
    m = {
        "Z": 1,
        "E": 5,
        "R": 10,
        "0": 0
    }

    to = {
        0  : "0000",
        1  : "000Z",
        2  : "00ZZ",
        3  : "0ZZZ",
        4  : "00ZE",
        5  : "000E",
        6  : "00EZ",
        7  : "0EZZ",
        8  : "EZZZ",
        9  : "00ZR",
        10 : "000R"
    }

    val = ""
    # check if initialized with valid string literal
    def __init__(self, s):
        self.val = s

    def __int__(self):
        p = 1
        i = 1
        prev = "0"
        curr = 0
        ans = 0
        for c in reversed(self.val):
            if self.m[c] >= self.m[prev]:
                curr += self.m[c]
            else :
                curr -= self.m[c]
            prev = c
            if i%4==0:
                ans += p*curr
                prev = "0"
                curr = 0
                p *= 10
            i += 1

        ans += p*curr
        return ans
    
    def __repr__(self):
        return self.val
    
    @classmethod
    def to_ZER0(cls, a: int) -> str:
        ansList = []
        while a :
            ansList.append(cls.to[a%10])
            a //= 10
            
        return "".join(reversed(ansList))

if __name__ == "__main__":
    obj = ZER0("00ZE00R0")
    print(obj)
    print(int(obj))

    obj = ZER0("00EZ00ZR")
    print(obj)
    print(int(obj))

    i = 45
    print(i)
    print(ZER0.to_ZER0(i))
