class Gov:
    tax=10

class TRAI(Gov):
    def getTax1(self):
        print(self.tax)

class RBI(Gov):
    def getTax2(self):
        print(self.tax)


r= RBI()
r.getTax2()
t=TRAI()
t.getTax1()