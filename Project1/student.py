class School:

    passWord=0
    mailId=0
    rollNo=" "
    name=" "
    phoneNo=" "







class Student(School):
    

    def main(self):
        print("********WELCOME TO BHOOMI's SCHOOL***********\n")
        print("\t1]add student")    
        print("\t2]view student")    
        print("\t3]sort by marks of student")    
        print("\t4]sort by age of student\n")
        option=input("Enter the above given choice:") 
        print(option)
        if option=='1':
            print("You selected add student as a choice..")
            s.printStdentData()
            

        elif option=='2':
            print("you selected student view as a choice..",)
            s.ViewStdent()

       

    def getStudentData(self):
        self.name=input("\tEnter the name:")
        self.rollNo=int(input("\tEnter the roll no:"))
        self.mailId=input("\tEnter the mail id:")
        self.passWord=input("\tEnter the password:")
        self.phoneNo=input("\tEnter the phone number:")
        print("---------YOUR DETAILS ADDED SUSSCESSFULLY------\n")

    def printStdentData(self):
        print("Student name:",self.name)
        print("Student roll no.:",self.rollNo)
        print("Student email id:",self.mailId)
        print("Student password:",self.passWord)
        print("Student phone no.:",self.phoneNo)



    def getViewStudent(self):
        print("enter the 1st student data\n")
        self.name=input("\tEnter the name:")
        self.rollNo=int(input("\tEnter the roll no:"))
        self.mailId=input("\tEnter the mail id:")
        self.passWord=input("\tEnter the password:")
        self.phoneNo=input("\tEnter the phone number:")
        print("Enter 2nd student data\n")  
        self.name=input("\tEnter the name:")
        self.rollNo=int(input("\tEnter the roll no:"))
        self.mailId=input("\tEnter the mail id:")
        self.passWord=input("\tEnter the password:")
        self.phoneNo=input("\tEnter the phone number:")
        print("Enter 3rd student data\n")   
        self.name=input("\tEnter the name:")
        self.rollNo=int(input("\tEnter the roll no:"))
        self.mailId=input("\tEnter the mail id:")
        self.passWord=input("\tEnter the password:")
        self.phoneNo=input("\tEnter the phone number:")

    def printViewStdent(self):
        print("--------1st student details-----\n")
        print("Student name:",self.name)
        print("Student roll no.:",self.rollNo)
        print("Student email id:",self.mailId)
        print("Student password:",self.passWord)
        print("Student phone no.:",self.phoneNo)
        print("--------2nd student details-----\n")
        print("Student name:",self.name)
        print("Student roll no.:",self.rollNo)
        print("Student email id:",self.mailId)
        print("Student password:",self.passWord)
        print("Student phone no.:",self.phoneNo)
        print("--------3rd student details-----\n")
        print("Student name:",self.name)
        print("Student roll no.:",self.rollNo)
        print("Student email id:",self.mailId)
        print("Student password:",self.passWord)
        print("Student phone no.:",self.phoneNo)


s=School()
s.main()
s.getStudentData()
s.printStdentData()
s.getViewStudent()
s.printViewStdent()