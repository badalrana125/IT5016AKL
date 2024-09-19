class Whitecliffe():
    def __init__(self,studentid, lname,program):
        self.studentid = studentid
        self.lname = lname
        self.program = program
        self.membershipid = 400001
    def member(self):
        self.membershipid+=1
        return self.membershipid

    def display(self):
        print(f"Student ID : {self.studentid} \n Last Name : {self.lname} \n Student Program : {self.program} \n Membership ID : {self.membershipid}")

info = Whitecliffe(20240593,"Rana","Bachelor")
info.member()
info.display()

class Member():
    def __init__(self,lname):
        self.lname = lname 
        self.id = id
        self.registeredstudents = 400
        self.withdrwanstudents = 600
        self.active = True
    def id(self):
        self.id+=1
        return self.id
    def withdraw(self):
        if self.active:
            self.registeredstudents-=1
            self.withdrwanstudents+=1
            print(f"Registered students ={self.registeredstudents} ")
            print(f"Withdrwan students = {self.withdrwanstudents} ")
        else:
            print("Invalid choices")
    def program(self,stream):
        if stream == "Diploma":
            print("Student Program is Diploma.")
        else:
            print("Student program is Bachelor")

    def display(self):
        print(f"LAST NAME: {self.lname}")
        print(f"Member ship ID: {self.id}")
        print(f"Registered students: {self.registeredstudents}")
        print(f"Withdrwan students:{self.withdrwanstudents}")
info = Member("Rana")
info.id(400)
info.withdraw()
info.display()
