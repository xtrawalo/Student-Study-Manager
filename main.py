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
    print("5. Assignments")
    print("6. Study Sessions")
    print("7. Daily Goals")
    print("8. Statistics")
    print("9. Save")
    print("10. Exit")
    #AVOIDING USER TO ENTER AN INVALID VALUE
    try:
        answer = int(input("Select a menu option (1-10) : "))
    except:
        print('Invalid Number')
        answer = int(input("Select a menu option (1-10) : "))
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
    try:
        choice = int(input("Enter your choice (0-3) : "))
    except:
        print('Invalid Number')
        choice = int(input("Enter your choice (0-3) : "))
    while answer not in [0,1,2,3]:
        print('Invalid Number')
        choice = int(input("Enter your choice (0-3) : "))
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
    #choosing a file to delete
    operation = int(input(f'Choose a subject to delete (0-{i}) : '))
    #deleting the file
    print(f'{Subjects[operation]} was deleted successfully !')
    del Subjects[operation]
    #Editing the Subjects File
    AccessMode = "w"
    MyFile = open(FileName, AccessMode) 
    for i in range(len(Subjects)):
        MyFile.write(Subjects[i])
    #Close the file
    MyFile.close()

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
    print(f'{Subjects[operation]} was edited successfully !')
    Subjects[operation] = NewSub
    #Editing the Subjects File
    AccessMode = "w"
    MyFile = open(FileName, AccessMode) 
    for i in range(len(Subjects)):
        MyFile.write(f'{Subjects[i]}\n')
    #Close the file
    MyFile.close()

#CALLING THE FUNCTION
answer = home()
#AVOIDING USER TO ENTER AN INVALID VALUE
while answer not in [1,2,3,4,5,6,7,8,9,10]:    
    print('Invalid Number')
    answer = int(input("Enter a Number between (1-10) to Continue : "))


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
