#Importing csv to read it
import csv
#CREATING HOME FUNCTION SO WE CAN RECALL IT LATER WHEN RETURN
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
        answer = int(input("Enter a Number between (1-10) to Continue : "))
    except:
        print('Invalid Number')
        answer = int(input("Enter a Number between (1-10) to Continue : "))
    return answer
#CALLING THE FUNCTION
home()
answer = home()
#AVOIDING USER TO ENTER AN INVALID VALUE
while answer not in [1,2,3,4,5,6,7,8,9,10]:    
    print('Invalid Number')
    answer = int(input("Enter a Number between (1-10) to Continue : "))
#ENTERING THE CHOSEN MENU
if answer == 1:
    print('Dashboard')
elif answer == 2:
    #INFORMING USER WHAT HE SHOULD DO 
    print("===================================")
    print("             Subjects              ")
    print("===================================")
    print("1. Add Subject")
    print("2. Delete Subject")
    print("3. Edit Subject")
    #AVOIDING USER TO ENTER AN INVALID VALUE
    try:
        choice = int(input("Enter a Number between (1-3) to Continue : "))
    except:
        print('Invalid Number')
        choice = int(input("Enter a Number between (1-3) to Continue : "))
    while answer not in [1,2,3]:
        print('Invalid Number')
        choice = int(input("Enter a Number between (1-10) to Continue : "))
    #ENTERING THE CHOSEN OPERATION
    if choice == 1:
        #OPENING THE SUBJECTS FILE
        FileName = "Subjects.txt"
        AccessMode = "a"
        MyFile = open(FileName, AccessMode)
        #ADD A NEW SUBJECT
        NewSubject = input("Enter a New Subject : ")
        MyFile.write(f"{NewSubject}\n")
        #CLOSING THE FILE
        MyFile.close()
    elif choice == 2:
        #OPENING THE SUBJECTS FILE
        FileName = "Subjects.csv"
        AccessMode = "r"
        with open(FileName, AccessMode) as MyFile:
            #converting data to a list
            Subjects = list(csv.reader(MyFile))
            print(Subjects)
        for subject in subjects
