from password import mainfx


class University:
    def __init__(self,n):
        self.uni_name=n
    def showdet(self):
        print(self.uni_name)

class Course(University):
    def __init__(self,n,uni):
        University.__init__(self,uni)
        self.course_name=n
    def showdet(self):
        print(self.course_name)

class Branch(University):
    def __init__(self,n,uni):
        University.__init__(self,uni)
        self.branch_name=n
    def showdet(self):
        print(self.branch_name)

class Student(Course,Branch):
    def __init__(self,n,course,branch,univ):
        Course.__init__(self,course,univ)
        Branch.__init__(self,branch,univ)
        self.stud_name=n
    def showdet(self):
        print(f"Student nmae:{self.stud_name}\nUniversity Name:{self.uni_name}\nBranch Name:{self.branch_name}\nCourse Name:{self.course_name}")

class Prof(Branch):
    def __init__(self,n,branch,univ):
        Branch.__init__(self,branch,univ)
        self.prof_name=n
    def showdet(self):
        print(f"Professor Name:{self.prof_name}\nUniversity Name:{self.uni_name}\nBranch Name:{self.branch_name}")





shubam=Student('shubam','python','cs','dtu')



aaryaman=Student('aaryaman','python','cs','dtu')

A=Student('A','python','cs','dtu')

B=Prof('B','cs','dtuy')
def addstud():
 
    n=input("Enter name of the Student:")
    u=input("Enter you univwersity:")
    b=input("Enter your branch:")
    c=input("Enter you course:")



    data=(f"\n{n}=Student('{n}','{c}','{b}','{u}')")
    write_data_between_classes_and_functions(data)

def addprof():


    
    n=input("Enter name of the Professor:")
    u=input("Enter you univwersity:")
    b=input("Enter your branch:")

    data=(f"\n{n}=Prof('{n}','{b}','{u}')")
    write_data_between_classes_and_functions(data)

    

  

def searchstud(n):
    try:
        globals()[n].showdet()
    except:
        print("Student dosent exist in the data")

def searchprof(n):
    try:
        globals()[n].showdet()
    except:
        print("Professor dosent exist in the data")

def write_data_between_classes_and_functions(data):
    with open(__file__, "r") as f:
        lines = f.readlines()

    with open(__file__, "w") as f:
        for line in lines:
            if line.strip().startswith("def addstud():") :
                f.write(data)
                f.write("\n")
            f.write(line)


print("WELCOME TO DATA COLLECTION AND REGISTRATION CENTER")







pin=input("Enter the password:")
pas=mainfx()
if pin==pas:
    print("Type=student,professoror 0 for ending the program")

    while True:
    
        ans=input("You are a student or a professor?")
        if ans=="student":
            choice=input("You want to add or search the student's data:")
            if choice=="add":
                addstud()
            elif choice=="search":
                st=input("Enter student's name")
                searchstud(st)
            else:
                print("Enter correct choice!")
        elif ans=="professor":
            choice=input("You want to add or search the professor's data:")
            if choice=="add":
                addprof()
            elif choice=="search":
                pf=input("Enter Prof name:")
                searchprof(pf)
            else:
                print("Enter correct choice!") 
        elif ans=="0":
            break
        else:
            print("Wrong option")

else:
    print("WRONG PASSWORD")


    






    





