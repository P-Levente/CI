import unittest,math

sz1=int(input("sz1"))
sz2=int(input("sz2"))
def abs_max(a:int,b:int) -> int:
    if(abs(a)>abs(b)): return (a)
    elif(abs(b)>abs(a)): return abs(b)
print(abs_max(sz1,sz2))

class Testek(unittest.TestCase):
    def test_nagyobb_nulla(self):
        nagyobb=int(abs_max(sz1,sz2))
        self.assertGreater(nagyobb,0)
class Testek2(unittest.TestCase):
    def test_nagyobb_nulla(self):
        nagyobb=int(abs_max(sz1,sz2))
        self.assertGreater(nagyobb,1000000)


unittest.main()