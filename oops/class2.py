#inheritance
 #a--->b
#single inheritance
#mul
     #----> a ---->b,c     x.y ---->p
#mul lev
  #a ---> b--->c
#hybrid
# a--->10 ---->    ----->
#hyrical
##
#                                               a
#                                         b          c
  #                                  p       q    r       s


class Vehicle:
    no_wheels=0
    makeYear =0
    color= ""
    fuelType =""
    name=""

    def test(self):
        print("test....")

class Car(Vehicle):
    def getCarData(self):
        self.name=input("Enter name")
        self.no_wheels=int(input("Entre no of wheels"))
        self.makeYear=int(input("Enter make year"))
        self.fuelType=input("Enter fuel Type")
        self.color=input("Enter color")
    def printCarData(self):
        print("Name",self.name)
        print("No of whhels"self.no_wheels)
        print("Make year",self.makeYear)
        print("Fule type",self.fuelType)
        print("color",self.color)


class CarType(Car):
    type=""


c1=Car()
c1.getCarData()
c1.printCarData()
ctype= CarType()