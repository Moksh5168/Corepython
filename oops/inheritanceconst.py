class Parent:

    def __init__(self ,name):
        print("Parent constructor")



class Child(Parent):

    def __init__(self):
        super().__init__("rakesh")
        print("Child constructor")

c=Child()