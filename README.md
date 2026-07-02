<h1 align="center">Student Study Manager in Python</h1>
<p align="center">
<img src="asset.jpg">
</p>

## Table of content

- [How it works](#how-it-works)
  - [Dashboard](#dashboard)
  - [Subjects](#subjects)
  - [Homework](#homework)
  - [Exams](#exams)
  - [WorkFlow](#workflow)
- [Built With](#built-with)
- [Installation](#installation)
- [Author](#author)

## How it works
 
First, I import everything I'll need: csv to read files, date to get the current date, and os to create files if they don't already exist.
```python
import csv
from datetime import date
import os
for f in ("Subjects.csv", "Homework.csv", "Exams.csv"):
    if not os.path.exists(f):
        open(f, "w").close()
```
Then I create a function for each operation to keep the program clean.
 
`def home()`: Displays all the menus the user can choose from
```python
def home():
    print("===================================")
    print("       STUDENT STUDY MANAGER       ")
    print("===================================")
    print("1. Dashboard")
    print("2. Subjects")
    print("3. Homeworks")
    print("4. Exams")
    print("5. Exit")
    #PREVENTING USER TO ENTER A TEXT
    while True:
        try:
            answer = int(input("Select a menu option (1-5) : "))
            break
        except:
            print('Invalid Number')
    #PREVENTING USER TO ENTER A NUMBER OVER 5 OR LESS THAN 1
    while answer not in [1,2,3,4,5]:
        try:
            answer = int(input("Enter your choice (1-5) : "))
        except:
            print('Invalid Number')
    return answer
```
### Dashboard
`def Dashboard()`: Dashboard menu showing the current date, total subjects, total exams, and homework status
```python
def Dashboard():
    print("===================================")
    print("             Dashboard             ")
    print("===================================")
    today = date.today()
    print(f"Today : {today.strftime("%d/%m/%Y")} ")
    FileName = 'Subjects.csv'
    AccessMode = 'r'
    with open(FileName, AccessMode) as MyFile:
        Rows = csv.reader(MyFile)
        Subjects = []
        for subject in Rows:
            Subjects.append(",".join(subject))
        if not Subjects:
            print(f"Subjects          : 0")
        else:
            print(f"Subjects          : {len(Subjects)}")
    FileName = 'Homework.csv'
    AccessMode = 'r'
    with open(FileName, AccessMode) as MyFile:
        Rows = csv.reader(MyFile)
        Homeworks = []
        Pending = 0
        Finished = 0
        for homework in Rows:
            Homeworks.append((homework[3]))
        for homework in Homeworks:
            if homework == 'Pending':
                Pending += 1
            elif homework == 'Finished':
                Finished += 1
        print(f"Pending Homework  : {Pending}")
        print(f"Finished Homework : {Finished}")
    FileName = 'Exams.csv'
    AccessMode = 'r'
    with open(FileName, AccessMode) as MyFile:
        Rows = csv.reader(MyFile)
        Exams = []
        for exam in Rows:
            Exams.append(exam[0])
        if not Exams:
            print(f"Exams             : 0")
        else:
            print(f"Exams             : {len(Exams)}")
    return
```
### Subjects
`def Subjects()`: Subjects menu; the user can choose to add, delete, or edit a subject
```python
def Subjects():
    #INFORMING USER WHAT HE SHOULD DO 
    print("===================================")
    print("             Subjects              ")
    print("===================================")
    print("0. Return")
    print("1. Add Subject")
    print("2. Delete Subject")
    print("3. Edit Subject")
    #PREVENTING USER TO ENTER A TEXT
    while True:
        try:
            choice = int(input("Enter your choice (0-3) : "))
            break
        except:
            print('Invalid Number')
    #PREVENTING USER TO ENTER A NUMBER OVER 3 OR LESS THAN 0
    while choice not in [0,1,2,3]:
        try:
            choice = int(input("Enter your choice (0-3) : "))
        except:
            print('Invalid Number')
    return choice
```
`def AddSub()`: Adds a subject to Subjects.csv and Homework.csv
```python
def AddSub():
    #OPENING THE SUBJECTS FILE
    FileName = "Subjects.csv"
    AccessMode = "a"
    MyFile = open(FileName, AccessMode)
    #ADD A NEW SUBJECT
    NewSubject = input("Enter a New Subject : ")
    while "," in NewSubject:
        NewSubject = input("Enter a New Subject (without a comma \",\") : ")
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
    Status = "Pending"
    MyFile.write(f"{NewSubject},{Exercice},{Deadline},{Status}\n")
    #CLOSING THE FILE
    MyFile.close()
    return
```
`def DeleteSub()`: Deletes a subject from Subjects.csv and Homework.csv
```python
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
        if not Subjects:
            print("No subjects yet.")
        else:       
            for i in range(len(Subjects)):
                print(f"{i}. {Subjects[i]}")
            #choosing a Subject to delete
            while True:
                try:
                    operation = int(input(f'Choose a subject to delete (0-{i}) : '))
                    break
                except:
                    print('Invalid Number')
            #PREVENTING USER TO ENTER A NUMBER OVER 5 OR LESS THAN 1
            while operation < 0 or operation > i :
                try:
                    operation = int(input(f'Choose a subject to delete (0-{i}) : '))
                except:
                    print('Invalid Number')
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
        if not Homework:
            print("No subjects yet.")
        else: 
            #deleting everything related to that subject
            del Homework[operation]
    #Editing the Homework File
    AccessMode = "w"
    MyFile = open(FileName, AccessMode)
    if not Homework:
        pass
    else:  
        for i in range(len(Homework)):
            MyFile.write(f"{Homework[i][0]},{Homework[i][1]},{Homework[i][2]},{Homework[i][3]}\n")
    #Close the file
    MyFile.close()
    return
```
`def EditSub()`: Edits a subject's name in Subjects.csv and Homework.csv
```python
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
        if not Subjects:
            print("No subjects yet.")
        else:     
            for i in range(len(Subjects)):
                print(f"{i}. {Subjects[i]}")
            #choosing a subject to edit
            while True:
                try:
                    operation = int(input(f'Choose a subject to edit (0-{i}) : '))
                    break
                except:
                    print('Invalid Number')
            #PREVENTING USER TO ENTER A NUMBER OVER i OR LESS THAN 0
            while operation < 0 or operation > i :
                try:
                    operation = int(input(f'Choose a subject to edit (0-{i}) : '))
                except:
                    print('Invalid Number')
            NewSub = input("Enter the new Subject name : ")
            while "," in NewSub:
                NewSub = input("Enter a New Subject (without a comma \",\") : ")
            #editing the subject
            Subjects[operation] = NewSub
    #Editing the Subjects File
    AccessMode = "w"
    MyFile = open(FileName, AccessMode) 
    if not Subjects:
        pass
    else: 
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
        if not Homework:
            pass
        else: 
            Homework[operation][0] = NewSub
    #saving the subject name in homework
    AccessMode = "w"
    MyFile = open(FileName, AccessMode) 
    if not Homework:
        pass
    else: 
        for i in range(len(Homework)):
            MyFile.write(f"{Homework[i][0]},{Homework[i][1]},{Homework[i][2]},{Homework[i][3]}\n")
    #Close the file
    MyFile.close()
    return
```
### Homework
`def Homework()`: Homework menu; the user can choose to add, delete, edit, or view homework
```python
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
```
`def AddHome()`: Adds a homework entry to Homework.csv
```python
def AddHome():
    #opening homework
    FileName = "Homework.csv"
    AccessMode = "a"
    MyFile = open(FileName, AccessMode)
    #ADDing The HOMEWORK
    Subject = input("Enter ur subject:")
    while "," in Subject:
        Subject = input("Enter ur subject (without a comma \",\") : ")
    Exercice = input('Enter ur exercise:')
    while "," in Exercice:
        Exercice = input("Enter ur exercise (without a comma \",\") : ")
    Deadline = input('Enter ur deadline:')
    while "," in Deadline:
        Deadline = input("Enter ur deadline (without a comma \",\") : ")
    Status = "Not Finished"
    MyFile.write(f"{Subject},{Exercice},{Deadline},{Status}\n")
    #CLOSING THE FILE
    MyFile.close()
    return
```
`def DeleteHome()`: Deletes a homework entry from Homework.csv
```python
def DeleteHome():
    FileName = "Homework.csv"
    AccessMode = "r"
    with open(FileName, AccessMode) as MyFile:
    #converting data to a list
        Rows = csv.reader(MyFile)
        Homework = []
        for subject in Rows:
            Homework.append(subject)
        if not Homework:
            print("No Homework yet.")
        else:   
            for i, homework in enumerate(Homework):
                print(i, homework)
            while True:
                try:
                    operation = int(input(f"choose a homework to delete (0-{i}) : "))
                    break
                except:
                    print('Invalid Number')
            #PREVENTING USER TO ENTER A NUMBER OVER i OR LESS THAN 0
            while operation < 0 or operation > i :
                try:
                    operation = int(input(f"choose a homework to delete (0-{i}) : "))
                except:
                    print('Invalid Number')
            del Homework[operation]
    #Opening Homework file
    FileName = "Homework.csv"
    AccessMode = "w"
    MyFile = open(FileName, AccessMode)
    #Saving changes
    if not Homework:
        pass
    else:   
        for i in range(len(Homework)):
            MyFile.write(f"{Homework[i][0]},{Homework[i][1]},{Homework[i][2]},{Homework[i][3]}\n")
    #Close the file
    MyFile.close()
    return
```
`def EditHome()`: Edits a homework entry in Homework.csv
```python
def EditHome():
    FileName = "Homework.csv"
    AccessMode = 'r'
    with open(FileName, AccessMode) as MyFile:
        #converting data to a list
        Rows = list(csv.reader(MyFile))
        Homework = []
        for homework in Rows:
            Homework.append(homework) 
        if not Homework:
            print("No Homework yet.")
        else:          
            for i in range(len(Homework)):
                print(f"{i}. {Homework[i][0]}")
            while True:
                try:
                    operation = int(input(f'Choose a Homework to edit (0-{i}) : '))
                    break
                except:
                    print('Invalid Number')
            #PREVENTING USER TO ENTER A NUMBER OVER i OR LESS THAN 0
            while operation < 0 or operation > i :
                try:
                    operation = int(input(f'Choose a Homework to edit (0-{i}) : '))
                except:
                    print('Invalid Number')
            NewEx = input('Enter new Exercice (0 to keep old one): ')
            while "," in NewEx:
                NewEx = input("Enter new Exercice (0 to keep old one) (without a comma \",\") : ")
            if NewEx != "0":
                Homework[operation][1] = NewEx
            Newdate = input('Enter new Deadline (0 to keep old one) : ')
            while "," in Newdate:
                Newdate = input("Enter new Deadline (0 to keep old one) (without a comma \",\") : ")
            if Newdate != "0":
                Homework[operation][2] = Newdate
            NewStat = input('Enter new Status (0 to keep old one) : ')
            while "," in NewStat:
                NewStat = input("Enter new Status (0 to keep old one) (without a comma \",\") : ")
            if NewStat != "0":
                Homework[operation][3] = NewStat
    AccessMode = "w"
    MyFile = open(FileName, AccessMode)
    if not Homework:
        pass
    else:   
        for i in range(len(Homework)):
            MyFile.write(f"{Homework[i][0]},{Homework[i][1]},{Homework[i][2]},{Homework[i][3]}\n")
    #Close the file
    MyFile.close()
    return
```
`def ViewHome()`: Views current homework with deadlines and status
```python
def ViewHome():
    FileName = "Homework.csv"
    AccessMode = 'r'
    with open(FileName, AccessMode) as MyFile:
        #converting data to a list
        Rows = list(csv.reader(MyFile))
        Homework = []
        for homework in Rows:
            Homework.append(homework) 
        if not Homework:
            print("No Homework yet.")
        else:    
            for i in range(len(Homework)):
                print(f"Subject: {Homework[i][0]} \nExercise: {Homework[i][1]} \nDue: {Homework[i][2]} \nStatus :{Homework[i][3]}\n")
    return
```
### Exams
`def Exams()`: Exams menu; the user can choose to add, delete, edit, or view exams
```python
def Exams():
    #INFORMING USER WHAT HE SHOULD DO 
    print("===================================")
    print("             Exams              ")
    print("===================================")
    print("0. Return")
    print("1. Add Exam")
    print("2. Delete Exam")
    print("3. Edit Exam")
    print("4. View Exam")
    #PREVENTING USER TO ENTER A Text
    while True:
        try:
            choice = int(input("Enter your choice (0-4) : "))
            break
        except:
            print('Invalid Number')
    #PREVENTING USER TO ENTER A NUMBER OVER THAN 4 OR LESS THAN 0
    while choice not in [0,1,2,3,4]:
        try:
            choice = int(input("Enter your choice (0-4) : "))
        except:
            print('Invalid Number')
    return choice
```
`def AddExam()`: Adds an exam to Exams.csv
```python
def AddExam():
    #opening Exams File
    FileName = "Exams.csv"
    AccessMode = "a"
    MyFile = open(FileName, AccessMode)
    #ADDing The Exam
    Subject = input("Enter the exam subject : ")
    while "," in Subject:
        Subject = input("Enter the exam subject (without a comma \",\") : ")
    Date = input("Enter the date of the exam : ")
    while "," in Date:
        Date = input("Enter the date of the exam (without a comma \",\") : ")
    MyFile.write(f"{Subject},{Date}\n")
    #CLOSING THE FILE
    MyFile.close()
    return
```
`def DeleteExam()`: Deletes an exam from Exams.csv
```python
def DeleteExam():
    FileName = "Exams.csv"
    AccessMode = "r"
    with open(FileName, AccessMode) as MyFile:
    #converting data to a list
        Rows = csv.reader(MyFile)
        Exams = []
        for exam in Rows:
            Exams.append(exam)
        if not Exams:
            print("No subjects yet.")
        else:   
            for i, exam in enumerate(Exams):
                print(i, exam)
            while True:
                try:
                    operation = int(input(f"choose an exam to delete (0-{i}) : "))
                    break
                except:
                    print('Invalid Number')
            #PREVENTING USER TO ENTER A NUMBER OVER i OR LESS THAN 0
            while operation < 0 or operation > i :
                try:
                    operation = int(input(f"choose an exam to delete (0-{i}) : "))
                except:
                    print('Invalid Number')
            del Exams[operation]
    #Opening Exams file
    FileName = "Exams.csv"
    AccessMode = "w"
    MyFile = open(FileName, AccessMode)
    #Saving changes
    if not Exams:
        pass
    else:   
        for i in range(len(Exams)):
            MyFile.write(f"{Exams[i][0]},{Exams[i][1]}\n")
    #Close the file
    MyFile.close()
    return
```
`def EditExam()`: Edits exam data in Exams.csv
```python
def EditExam():
    FileName = "Exams.csv"
    AccessMode = 'r'
    with open(FileName, AccessMode) as MyFile:
        #converting data to a list
        Rows = list(csv.reader(MyFile))
        Exams = []
        for exam in Rows:
            Exams.append(exam)   
        if not Exams:
            print("No exams yet.")
        else:        
            for i in range(len(Exams)):
                print(f"{i}. {Exams[i][0]}")
            while True:
                try:
                    operation = int(input(f'Choose an exam to edit (0-{i}) : '))
                    break
                except:
                    print('Invalid Number')
            #PREVENTING USER TO ENTER A NUMBER OVER i OR LESS THAN 0
            while operation < 0 or operation > i :
                try:
                    operation = int(input(f'Choose an exam to edit (0-{i}) : '))
                except:
                    print('Invalid Number')
            NewExam = input('Enter new date (0 to keep old one): ')
            while "," in NewExam:
                NewExam = input("Enter new date (0 to keep old one) (without a comma \",\") : ")
            if NewExam != "0":
                Exams[operation][1] = NewExam
    AccessMode = "w"
    MyFile = open(FileName, AccessMode)
    if not Exams:
        pass
    else:   
        for i in range(len(Exams)):
            MyFile.write(f"{Exams[i][0]},{Exams[i][1]}\n")
    #Close the file
    MyFile.close()
    return
```
`def ViewExam()`: Views current exams with dates
```python
def ViewExam():
    FileName = "Exams.csv"
    AccessMode = 'r'
    with open(FileName, AccessMode) as MyFile:
        #converting data to a list
        Rows = list(csv.reader(MyFile))
        Exams = []
        for exam in Rows:
            Exams.append(exam)  
        if not Exams:
            print("No Exams yet.")
        else:   
            for i in range(len(Exams)):
                print(f"Subject: {Exams[i][0]} \nDate: {Exams[i][1]}\n")
    return
```
### WorkFlow
The program starts here:
```python
while True:
    #CALLING THE FUNCTION
    answer = home()
 
    #ENTERING THE DASHBOARD MENU
    if answer == 1:
        Dashboard()
 
    #ENTERING THE SUBJECTS MENU
    elif answer == 2:
        choice = Subjects()
        if choice == 0:
            continue
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
            continue
        elif choice == 1:   
            AddHome()
        elif choice == 2:
            DeleteHome()
        elif choice == 3:
            EditHome()
        elif choice == 4:
            ViewHome()
 
    #ENTERING THE EXAMS MENU
    elif answer == 4:
        choice = Exams()
        if choice == 0:
            continue
        elif choice == 1:   
            AddExam()
        elif choice == 2:
            DeleteExam()
        elif choice == 3:
            EditExam()
        elif choice == 4:
            ViewExam()
 
    elif answer == 5:
        break    
```
## Built With

- Python
- csv Module
- datetime Module 

## Installation

## Author

Me : [xtrawalo](https://github.com/xtrawalo)
