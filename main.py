#Importing csv to read it
import csv
#CREATING FUNCTIONs SO WE CAN RECALL IT LATER WHEN RETURN
def home():
    #INFORMING USER WHAT HE SHOULD DO 
    print("===================================")
    print("       STUDENT STUDY MANAGER       ")
    print("===================================")
    print("1. Dashboard")
    print("2. Subjects")
    print("3. Homeworks")
    print("4. Exams")
    print("5. Exit")
    #AVOIDING USER TO ENTER A stringers
    while True:
        try:
            answer = int(input("Select a menu option (1-5) : "))
            break
        except:
            print('Invalid Number')
    #AVOIDING USER TO ENTER AN number over 5 or less than 1
    while answer not in [1,2,3,4,5]:
        try:
            answer = int(input("Enter your choice (1-5) : "))
        except:
            print('Invalid Number')
    return answer

def Subjects():
    #INFORMING USER WHAT HE SHOULD DO 
    print("===================================")
    print("             Subjects              ")
    print("===================================")
    print("0. Return")
    print("1. Add Subject")
    print("2. Delete Subject")
    print("3. Edit Subject")
    #AVOIDING USER TO ENTER AN INVALID VALUE
    while True:
        try:
            choice = int(input("Enter your choice (0-3) : "))
            break
        except:
            print('Invalid Number')
    #AVOIDING USER TO ENTER AN number over 3 or less than 0
    while choice not in [0,1,2,3]:
        try:
            choice = int(input("Enter your choice (0-3) : "))
        except:
            print('Invalid Number')
    return choice

def AddSub():
    #OPENING THE SUBJECTS FILE
    FileName = "Subjects.csv"
    AccessMode = "a"
    MyFile = open(FileName, AccessMode)
    #ADD A NEW SUBJECT
    NewSubject = input("Enter a New Subject : ")
    MyFile.write(f"{NewSubject}\n")
    #CLOSING THE FILE
    MyFile.close()

    #OPENING THE HOMEWORK FILE
    FileName = "Homework.csv"
    AccessMode = "a"
    MyFile = open(FileName, AccessMode)
    #ADD IT TO HOMEWORK
    Exercice = "Not Set"
    Deadline = "Not Set"
    Status = "Not Set"
    MyFile.write(f"{NewSubject},{Exercice},{Deadline},{Status}\n")
    #CLOSING THE FILE
    MyFile.close()
    return

def DeleteSub():
    #OPENING THE SUBJECTS FILE
    FileName = "Subjects.csv"
    AccessMode = "r"
    with open(FileName, AccessMode) as MyFile:
        #converting data to a list
        Rows = csv.reader(MyFile)
        Subjects = []
        for subject in Rows:
            Subjects.append(subject[0])        
        for i in range(len(Subjects)):
            print(f"{i}. {Subjects[i]}")
    #choosing a Subject to delete
    operation = int(input(f'Choose a subject to delete (0-{i}) : '))
    #deleting the subject
    print(f'{Subjects[operation]} was deleted successfully !')
    del Subjects[operation]
    #Editing the Subjects File
    AccessMode = "w"
    MyFile = open(FileName, AccessMode) 
    for i in range(len(Subjects)):
        MyFile.write(f"{Subjects[i]}\n")
    #Close the file
    MyFile.close()
        
    #OPENING THE HOMEWORK FILE
    FileName = "Homework.csv"
    AccessMode = "r"
    with open(FileName, AccessMode) as MyFile:
        #converting data to a list
        Rows = csv.reader(MyFile)
        Homework = []
        for subject in Rows:
            Homework.append(subject)
    #deleting everything related to that subject
    del Homework[operation]
    #Editing the Homework File
    AccessMode = "w"
    MyFile = open(FileName, AccessMode) 
    for i in range(len(Homework)):
        MyFile.write(f"{Homework[i][0]},{Homework[i][1]},{Homework[i][2]},{Homework[i][3]}\n")
    #Close the file
    MyFile.close()
    return

def EditSub():
    #OPENING THE SUBJECTS FILE
    FileName = "Subjects.csv"
    AccessMode = "r"
    with open(FileName, AccessMode) as MyFile:
        #converting data to a list
        Rows = csv.reader(MyFile)
        Subjects = []
        for subject in Rows:
            Subjects.append(subject[0])        
        for i in range(len(Subjects)):
            print(f"{i}. {Subjects[i]}")
    #choosing a subject to edit
    operation = int(input(f'Choose a subject to edit (0-{i}) : '))
    NewSub = input("Enter the new Subject name : ")
    #editing the subject
    Subjects[operation] = NewSub
    #Editing the Subjects File
    AccessMode = "w"
    MyFile = open(FileName, AccessMode) 
    for i in range(len(Subjects)):
        MyFile.write(f'{Subjects[i]}\n')
    #Close the file
    MyFile.close()
    #OPENING THE Homework FILE
    FileName = "Homework.csv"
    AccessMode = 'r'
    with open(FileName, AccessMode) as MyFile:
        #converting data to a list
        Rows = csv.reader(MyFile)
        Homework = []
        for homework in Rows:
            Homework.append(homework) 
    #editing the subject name
        Homework[operation][0] = NewSub
    #saving the subject name in homework
    AccessMode = "w"
    MyFile = open(FileName, AccessMode) 
    for i in range(len(Homework)):
        MyFile.write(f"{Homework[i][0]},{Homework[i][1]},{Homework[i][2]},{Homework[i][3]}\n")
    #Close the file
    MyFile.close()
    return

def Homework():
    #INFORMING USER WHAT HE SHOULD DO 
    print("===================================")
    print("             Homework              ")
    print("===================================")
    print("0. Return")
    print("1. Add Homework")
    print("2. Delete Homework")
    print("3. Edit Homework")
    print("4. View Homework")
    #AVOIDING USER TO ENTER AN INVALID VALUE
    while True:
        try:
            choice = int(input("Enter your choice (0-4) : "))
            break
        except:
            print('Invalid Number')
    #AVOIDING USER TO ENTER AN number over 4 or less than 0
    while choice not in [0,1,2,3,4]:
        try:
            choice = int(input("Enter your choice (0-4) : "))
        except:
            print('Invalid Number')
    return choice

def AddHome():
    #opening homework
    FileName = "Homework.csv"
    AccessMode = "a"
    MyFile = open(FileName, AccessMode)
    #ADDing The HOMEWORK
    Subject = input("Enter ur subject:")
    Exercice = input('Enter ur exercice:')
    Deadline = input('Enter ur deadline:')
    Status = "Not Finished"
    MyFile.write(f"{Subject},{Exercice},{Deadline},{Status}\n")
    #CLOSING THE FILE
    MyFile.close()
    return

def DeleteHome():
    FileName = "Homework.csv"
    AccessMode = "r"
    with open(FileName, AccessMode) as MyFile:
    #converting data to a list
        Rows = csv.reader(MyFile)
        Homework = []
        for subject in Rows:
            Homework.append(subject)
        for i, homework in enumerate(Homework):
            print(i, homework)
        operation = int(input(f"choose a homework to delete (0-{i}) : "))
        del Homework[operation]
    #Opening Homework file
    FileName = "Homework.csv"
    AccessMode = "w"
    MyFile = open(FileName, AccessMode)
    #Saving changes
    for i in range(len(Homework)):
        MyFile.write(f"{Homework[i][0]},{Homework[i][1]},{Homework[i][2]},{Homework[i][3]}\n")
    #Close the file
    MyFile.close()
    return

def EditHome():
    FileName = "Homework.csv"
    AccessMode = 'r'
    with open(FileName, AccessMode) as MyFile:
        #converting data to a list
        Rows = list(csv.reader(MyFile))
        Homework = []
        for homework in Rows:
            Homework.append(homework)        
        for i in range(len(Homework)):
            print(f"{i}. {Homework[i][0]}")
        operation = int(input(f'Choose a Homework to edit (0-{i}) : '))
        NewEx = input('Enter new Exercice (0 to keep old one): ')
        if NewEx != "0":
            Homework[operation][1] = NewEx
        Newdate = input('Enter new Deadline (0 to keep old one) : ')
        if Newdate != "0":
            Homework[operation][2] = Newdate
        NewStat = input('Enter new Status (0 to keep old one) : ')
        if NewStat != "0":
            Homework[operation][3] = NewStat
    AccessMode = "w"
    MyFile = open(FileName, AccessMode)
    for i in range(len(Homework)):
        MyFile.write(f"{Homework[i][0]},{Homework[i][1]},{Homework[i][2]},{Homework[i][3]}\n")
    #Close the file
    MyFile.close()
    return

def ViewHome():
    FileName = "Homework.csv"
    AccessMode = 'r'
    with open(FileName, AccessMode) as MyFile:
        #converting data to a list
        Rows = list(csv.reader(MyFile))
        Homework = []
        for homework in Rows:
            Homework.append(homework)  
        for i in range(len(Homework)):
            print(f"Subject: {Homework[i][0]} \nExercise: {Homework[i][1]} \nDue: {Homework[i][2]} \nStatus :{Homework[i][3]}\n")
    return

#CALLING THE FUNCTION
answer = home()

#ENTERING THE DASHBOARD MENU
if answer == 1:
    print('Dashboard')

#ENTERING THE SUBJECTS MENU
elif answer == 2:
    choice = Subjects()
    if choice == 0:
        home()
    elif choice == 1:
        AddSub()
    elif choice == 2:
        DeleteSub()
    elif choice == 3:
        EditSub()

#ENTERING THE HOMEWORKS MENU
elif answer == 3:
    choice = Homework()
    if choice == 0:
        home()
    elif choice == 1:   
        AddHome()
    elif choice == 2:
        DeleteHome()
    elif choice == 3:
        EditHome()
    elif choice == 4:
        ViewHome()

#ENTERING THE EXAMS MENU
