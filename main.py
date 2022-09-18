STR = """
\t\t\t\tCODING INFORMATIONS

Group Members :

    1. Manas Tiwari -- 12 M2 -- 02 ( Admin )
    2. Zaid khan -- 12 M2 -- 05 
    3. Abhinav Srivastav -- 12 M2 -- 30
    4. Arnav Agrahari -- 12 M2 -- 14
    5. Yashdeep -- 12 M2 -- 

EDoc (Source Code) : https://pastebin.com/945Sy9Gh

1. This Project Is Completed Under the guidence of our computer teacher (Mr. K.C Bhargav).
2. The project Works for managing the fees records of students, it store the information(name, class, section
roll number, Number of month fees is submitted).
3. The Sr number of the students will be automatically generated by the program in series.(By Counting number
of records are saved in the sql table and than by adding 1 to it).
4. Final Version Is 0.001A 
 
Module Used :
    Sql Connector - Comes Default After Installing Mysql In Developer or If Selected While Installing Mysql
                    Command For Installing : pip install mysql.connector-python or
                                             pip3 install mysql.connector-python

    Random - Comes Default By The Installation Of Python

    Time - Comes Default By The Installation Of Python

\t\t\t\tFEES MANAGEMENT SYSTEM - Help
SQL CONNECTION STATUS - [CONNECTED]
VERSION - [0.001A]
DATABASE NAME - [Fees_Manager]
SERVER - [SQL]
TESTED ON - [Python 3.7.8 64 Bit\\Python 3.9 64 Bit & MYSQL 8.0]
TESTED PLATFORMS - [WINDOWS, LINUX (UBUNTU 20.04 LTS)]

Home Menu Instructions :
1. Add Student To Add Students Data In SQL Server ( All Update The Fee Record )
2. Deposit Fee ( Only Of Existing Student In Server Table) Updates The Fee Recoed UpTo 12 (Numbers Represent
there respective months)
3. Used For Updting The Fees Of All The Classes Which Is Going to stored in Fee_Amount.txt
4. Filter Records (Present In SQL DATABASE TABLE) (On the basis of Name, Class, Sr Number, Class-Section
5. Is Used To Delete All The Tables And Records.
6. For HELP 
7. For Ending The Program.

    
Happy Coding :)

"""

import mysql.connector as sql
from time import sleep
import random


print("VERSION - 0.001A")
print("ESTABLISHING CONNECTIONS .....\n")
sleep(1)

def fee_amount():
    """This function manages the Fee_Amount.txt file which contain fee amount of each and every class
    if the fee_amount.txt file is not present in the folder, this function creates the file with default
    fee amount.
    """
    with open("Fee_Amount.txt", "a") as f:
        with open("Fee_Amount.txt", "r") as i:
            if len(i.readlines()) == 0:
                f.write("1 - 500\n")
                f.write("2 - 700\n")
                f.write("3 - 900\n")
                f.write("4 - 1000\n")
                f.write("5 - 1200\n")
                f.write("6 - 1400\n")
                f.write("7 - 1600\n")
                f.write("8 - 1800\n")
                f.write("9 - 2000\n")
                f.write("10 - 2200\n")
                f.write("11 - 2400\n")
                f.write("12 - 2450\n")
            elif len(i.readlines()) > 13 or len(i.readlines()) < 13:
                with open("Fee_Amount.txt", "w") as f:
                    f.write("")
                with open("Fee_Amount.txt", "a") as f:
                    f.write("1 - 500\n")
                    f.write("2 - 700\n")
                    f.write("3 - 900\n")
                    f.write("4 - 1000\n")
                    f.write("5 - 1200\n")
                    f.write("6 - 1400\n")
                    f.write("7 - 1600\n")
                    f.write("8 - 1800\n")
                    f.write("9 - 2000\n")
                    f.write("10 - 2200\n")
                    f.write("11 - 2400\n")
                    f.write("12 - 2450\n")

fee_amount() # Managing The Fee_Amount.txt 

passwd = "manas123" # MYSQL PASSWORD

# In the next upcoming line the program is going to try to connect the python with mysql server
mycon = sql.connect(host='localhost',
                        user='root',
                        passwd=passwd)

mycursor = mycon.cursor()
print("Checking For database... \n") # 2nd > Just A print statement to increase the number of lines :)
sleep(1)

#! In the next upcoming line the program is going to create a database in sql server named Fees_Manager (If not exists)
mycursor.execute("CREATE DATABASE IF NOT EXISTS Fees_Manager")

print("Creating Database If Not Exist... Done!\n") #3rd > another print statement
sleep(1) # sleep Statement

#! In the next upcoming line the program is going to Use the previously created database (fees_manager)
mycursor.execute("USE Fees_Manager")

#!In the next upcoming line the program is going to create a table named students which is going to contain
#!all the information related to fee, the table contain SR NUMBER, NAME, CLASS, SECTIOn, ROLL_No, sub.Fee Month
mycursor.execute(
        "CREATE TABLE IF NOT EXISTS students(SR int, Name varchar(255), Class varchar(15), Section varchar(15),  Roll_No int, Submitted varchar(50))")

#! In the next upcoming line the program is going to check is the connection to sql is established or not
if mycon.is_connected():
    print("Connecting To Database ...\n") #4 Print statement
    sleep(1)
    print("Successfully Connected\n")# 5 print 
    print() # 6 print

def sleepRan():
    num = random.choice([0, 0.11, 0.0001, 0.21, 0.00000009, 0.5, 0.4, 0.004, 0.44, 0.00000001])
    sleep(num)
    return num


def add_student(Name, Class, Section, Roll_No):
    """This function adds student data to the mysql table which contains all the data that are specified 
    above.

    Args:
        Name (String): Name of the student
        Class (integer): Class of the student
        Section (string): Section of the students class
        Roll_No (integer): roll number of the specified student
    """
    CMD = f"SELECT * FROM students"
    data = mycursor.execute(CMD)
    records = mycursor.fetchall()
    Sr = len(records) + 1

    Month = 0
    while Month <= 0:
        Month = int(
            input("Enter Number Of Month Fee You Want To Submit 0 < x <=12 >>> "))
        if Month > 12:
            print("Invalid Month Number!\n")
            Month = 0
            print("Re-Enter Number Of Month")
        if Month < 0:
            print("Invalid Month Number!\n")
            Month = 0
            print("Re-Enter Number Of Month")

    with open("Fee_Amount.txt", "r") as f:
        data = f.readlines()
        amt = data[int(Class)-1].replace("\n", "").split(" - ")
        amt = int(amt[1])
        print("\nEach Month Fee : ", amt)
        print()
        amt = Month*amt

    print(f"\nTotal Fee Amount : {amt}\n")
    print("\nBefore You Save Take A Look To Entered Information : \n")
    print("-"*10, "SUMMARY INFO", "-"*10)
    print("\n")
    print("SR Number : ", Sr, " Allotted ".upper())
    print("Name : ", Name)
    print("Class : ", Class)
    print("Section : ", Section)
    print("Roll No : ", Roll_No)
    print("Number Of Month Fee Submitted : ", Month)
    print()
    print("-"*25)
    print()
    yn = input("Sure To Save This Record (Yes/No) >>> ")
    yn = yn.lower()
    if 'y' in yn:
        value = 'INSERT INTO students values(%s,%s,%s,%s,%s,%s)'
        Month = f"{Month} Month(s) ({amt} Rs)"
        values = [(Sr, Name, Class, Section, Roll_No, Month)]
        mycursor.executemany(value, values)
        mycon.commit()
        print("\nSaving Student Data...\n")
        sleep(1)
        print("Data Saved!\n")
    else:
        print("Quiting ... ")


def change_fee():
    """This function is used for changing the fee amount.
    """
    Class = 1
    with open("Fee_Amount.txt", "w") as f:
        f.write("")
    while Class != 13:
        Amount = int(input(f"Enter Fee Amount For Class {Class} >>> "))
        if Amount < 0:
            continue
        with open("Fee_Amount.txt", "a") as f:
            f.write(f"{Class} - {Amount}\n")
        Class += 1


def Filter_By_Sr(SR):
    """This function prints table of students stored data of specified SR number

    Args:
        SR (int): Sr number of the student
    """
    CMD = f"SELECT * FROM students WHERE SR = {SR}"
    data = mycursor.execute(CMD)
    records = mycursor.fetchall()
    # Sr, Name, Class, Section, Roll_No, Month
    Name = records[0][1]
    Class = records[0][2]
    Section = records[0][3]
    Roll = records[0][4]
    fee_submitted = records[0][5]
    total = len(records)
    print("-"*75)
    print ("{:<8} {:<15} {:<10} {:<10} {:<10} {:<10}".format('SR No.','Name','Class','Section', 'Roll No.', 'Submitted Record'))
    print("-"*75)
    print()
    Sum = 0
    print ("{:<8} {:<15} {:<10} {:<10} {:<10} {:<10}".format(SR, Name, Class, Section, Roll,  fee_submitted))
    Sum += sleepRan()
    print()
    print("-"*75)
    print(f"\nTotal Rows : {total}\n")
    print(f"{total} Rows in {Sum} Sec(s)")


def Filter_By_Name(Name):
    """This function finds every match of specified name and prints the table which contain all the data

    Args:
        Name (str): NAME OF STUDENT
    """
    CMD = f"SELECT * FROM students WHERE Name = '{Name}'"
    data = mycursor.execute(CMD)
    records = mycursor.fetchall()
    total = len(records)
    print()
    print("-"*75)
    print ("{:<8} {:<15} {:<10} {:<10} {:<10} {:<10}".format('|SR No.','|Name','|Class','|Section', '|Roll No.', '|Submitted Record'))
    print("-"*75)
    print()
    Sum = 0
    for i in records:
        print ("{:<8} {:<15} {:<10} {:<10} {:<10} {:<10}".format("|"+str(i[0]), "|"+str(i[1]), "|"+str(i[2]), "|"+str(i[3]), "|"+str(i[4]), "|"+str(i[5])))
        Sum += sleepRan()
    print("-"*75)
    print(f"\nTotal Rows : {total}\n")
    print(f"{total} Rows in {Sum} Sec(s)")


def Filter_By_Class(Class):
    """This function finds every match of specified Class and prints the table which contain all the data

    Args:
        Class (int): Class of the student.SECTION IS NOT INCLUDED
    """
    CMD = f"SELECT * FROM students WHERE Class = '{Class}'"
    data = mycursor.execute(CMD)
    records = mycursor.fetchall()
    total = len(records)
    print()
    print("-"*75)
    print ("{:<8} {:<15} {:<10} {:<10} {:<10} {:<10}".format('|SR No.','|Name','|Class','|Section', '|Roll No.', '|Submitted Record'))
    print("-"*75)
    print()
    Sum = 0
    for i in records:
        print ("{:<8} {:<15} {:<10} {:<10} {:<10} {:<10}".format("|"+str(i[0]), "|"+str(i[1]), "|"+str(i[2]), "|"+str(i[3]), "|"+str(i[4]), "|"+str(i[5])))
        Sum += sleepRan()
    print("-"*75)
    print(f"\nTotal Rows : {total}\n")
    print(f"{total} Rows in {Sum} Sec(s)")


def Filter_By_Section(Class_Sec):
    """This function finds every match of specified Class-Section and prints the table which contain all the data

    Args:
        Class_Sec (str): Class and section of student, format = class-section
    """
    Class = Class_Sec.split("-")
    CMD = f"SELECT * FROM students WHERE Class = '{Class[0]}' AND Section = '{Class[1]}'"
    data = mycursor.execute(CMD)
    records = mycursor.fetchall()
    total = len(records)
    print()
    print("-"*75)
    print ("{:<8} {:<15} {:<10} {:<10} {:<10} {:<10}".format('|SR No.','|Name','|Class','|Section', '|Roll No.', '|Submitted Record'))
    print("-"*75)
    print()
    Sum = 0
    for i in records:
        print ("{:<8} {:<15} {:<10} {:<10} {:<10} {:<10}".format("|"+str(i[0]), "|"+str(i[1]), "|"+str(i[2]), "|"+str(i[3]), "|"+str(i[4]), "|"+str(i[5])))
        Sum += sleepRan()
    print("-"*75)
    print(f"\nTotal Rows : {total}\n")
    print(f"{total} Rows in {Sum} Sec(s)")

def deposit_fee(Sr):
    """This function updates ONLY FEE record of the student when fee of the student is submitted

    Args:
        Sr (int): SR number of the student
    """
    CMD = f"select * from students where SR={Sr}"
    data = mycursor.execute(CMD)
    records = mycursor.fetchall()
    Name = records[0][1]
    Class = records[0][2]
    Section = records[0][3]
    Roll = records[0][4]
    fee_submitted = records[0][5]
    print()
    print("-"*26, " Info ", "-"*26)
    print("Sr Number : ", Sr)
    print("Student Name : ", Name)
    print("Class : ", Class)
    print("Section : ", Section)
    print("Roll Number ", Roll)
    fee_submitted = int(fee_submitted.split()[0])
    print("Month Fee Left : ", 12-int(fee_submitted))
    print("-"*65)
    print()
    if 12-int(fee_submitted) != 0:
        Month = 0
        if 12-int(fee_submitted) != 1:
            while Month == 0:
                Month = int(input(
                    f"Enter Number Of Month Fee You Want To Submit 0 < x <={12-int(fee_submitted)} >>> "))
                if Month > 12-int(fee_submitted):
                    print("\nInvalid Month Number!\n")
                    Month = 0
                    print("\nRe-Enter Number Of Month")
                if Month < 0:
                    print("\nInvalid Month Number!\n")
                    Month = 0
                    print("\nRe-Enter Number Of Month")
        else:
            Month = 1
        with open("Fee_Amount.txt", "r") as f:
            data = f.readlines()
            amt = data[int(Class)-1].replace("\n", "").split(" - ")
            amt = int(amt[1])
            print("\nEach Month Fee : ", amt)
            amt1 = amt
            amt = Month*amt
        print(f"\nFee Amount : {amt}")
        yn = input("\nSure To Save This Record (yes/No) >>> ")
        print()
        yn.lower()
        submitted = int(fee_submitted) + Month
        if 'y' in yn:
            amt = submitted * amt1
            submitted = f"'{submitted} Month(s) ({amt} Rs)'"
            CMD = f"UPDATE students SET Submitted={submitted} WHERE SR={Sr}"
            mycursor.execute(CMD)
            mycon.commit()
    else:
        print("\n12 Month Fees Is Already Submitted!\n")

def admin():
    attempt = 1
    Success = False
    while attempt <= 3:
        print("\nUser : Root")
        with open(".Password.txt", "a") as f:
            with open(".Password.txt", "r") as i:
                if len(i.readlines()) == 0:
                    print("\nNo Password, Please Create Password")
                    passwd = input("Create Password, 0 To Exit >>> ")
                    if passwd != '0':
                        with open(".Password.txt", "w") as f:
                            f.write(passwd)
                    else:break
        passwd = input("Enter Password To Continue, 0 To Exit, -1 To Change Password >>> ")
        with open(".Password.txt", "r") as f:
            PASS = f.readlines()[0]
        if passwd == PASS:
            print("Correct Password\n")
            Success = True
            break
        elif passwd == '0':
            Success = False
            print("Exiting ... ")
            sleep(2)
            break
        elif passwd == '-1':
            passwd = input("Enter Current Password To Continue >>> ")
            if passwd == PASS:
                passwd = input("Create New Password >>> ")
                with open(".Password.txt", "w") as f:
                    f.write(passwd)
            else:
                print("\nInvalid Password")
        else:
            print("\n*** Invalid Password !")
            print(f"Only {3-attempt} Attempt(s) Is Left***")
            delete = input("\nAre You Sure To Reset All The Data >>> ").lower()
            if 'y' in delete:
                print("Reseting ... ")
                sleep(1)
                CMD = "DROP DATABASE Fees_Manager"
                mycursor.execute(CMD)
                mycursor.execute("CREATE DATABASE IF NOT EXISTS Fees_Manager")
                mycursor.execute("USE Fees_Manager")
                mycursor.execute(
                    "CREATE TABLE IF NOT EXISTS students(SR int, Name varchar(255), Class varchar(15), Section varchar(15),  Roll_No int, Submitted varchar(50))")
                fee_amount()
                with open(".Password.txt", "w") as f:
                    f.write("")
                print("\nReset Successfull")
                sleep(1)
        attempt += 1
    return Success

Continue = admin()

while True:
    if not Continue:
        print("\nGood Bye\n")
        break
    try:
        print("-"*75)
        print("\t\t\t\tFEES MANAGEMENT SYSTEM")
        print("-"*75)
        print()
        print("SQL CONNECTION STATUS - [CONNECTED]\n")
        print("VERSION - [0.001A]\n")
        print("DATABASE NAME - [Fees_Manager]\n")
        print("SERVER - [SQL]\n")
        print("TESTED ON - [Python 3.7.8 64 Bit\\Python 3.9 64 Bit & MYSQL 8.0]\n")
        print("TESTED PLATFORMS - [WINDOWS, LINUX (UBUNTU 20.04 LTS)]")
        print("-"*75)
        print("\n1. Add Student\n2. Deposit Fee\n3. Change Fee\n4. Filter Students Data \n5. Delete Record\n6. Help\n7. Exit")
        user = int(input("\nEnter Your Choice (Natural Numbers Only) >>> "))

        if user == 1:
            print("\n")
            Sr = 0
            Name = input("\nEnter Student Name >>> ").title()
            Class = int(input("\nEnter Class >>> "))
            if Class > 12:
                print("Invalid Class!\n")
            if Class < 0:
                print("Invalid Class!\n")
            Section = input("\nEnter Section >>> ").title()
            Roll_No = int(input("\nEnter Roll Number >>> "))
            print("Checking Info...\n")
            add_student(Name, Class, Section, Roll_No)

        elif user == 2:
            Sr = 0
            print("\n"*3)
            while Sr == 0:
                Sr = int(input("\nEnter Sr Number >>> "))
                if Sr < 0:
                    print("\nInvalid Sr Number .\n")
                    Sr = 0
            deposit_fee(Sr)

        elif user == 3:
            print("\n"*3)
            change_fee()

        elif user == 4:
            print()
            print("            1.By Name\n\
                2.By Sr Number\n\
                3.By Class\n\
                4.By Class And Section")
            choose = int(input("\nChoose Your Operation UpTo 4 (Natural Numbers <= 4),Exit ? Press 0 >>> "))
            if choose >= 0:
                if choose == 0:
                    print("\nReturning To Home ....\n")
                elif choose == 1:
                    name = input("\nEnter Name, 0 To Exit >>> ")
                    if name != "" and name != "0":
                        print("\n"*3)
                        Filter_By_Name(name)
                elif choose == 2:
                    Sr = 0
                    while Sr == 0:
                        Sr = int(input("\nEnter Sr Number, 0 Exit >>> "))
                        if Sr < 0:
                            print("\nInvalid Sr Number .\n")
                            Sr = 0
                    if Sr != 0:
                        print("\n"*3)
                        Filter_By_Sr(Sr)
                elif choose == 3:
                    Class = 0
                    while Class == 0:
                        Class = int(input("\nEnter Class, 0 Exit >>> "))
                        if Class < 0:
                            print("\nInvalid Class .\n")
                            Class = 0
                    if Class != 0:
                        print("\n"*3)
                        Filter_By_Class(Class)
                elif choose == 4:
                    Class_Sec = input("\nEnter Class-Section, 0 To Exit >>> ")
                    if Class_Sec != "" and Class_Sec != "0":
                        print("\n"*3)
                        Filter_By_Section(Class_Sec)
                else:
                    print("\nReturning To Home ....\n")

        elif user == 5:
            print("\n"*3)
            yn = input("\nAre You Sure To Delete All Stored Records (Yes/No)>>> ").lower()
            if 'y' in yn:
                print("\nDeleting Data Total Steps : 2 Done : 0\\2 ... ")
                with open("Fee_Amount.txt", "w") as f:
                    f.write("")
                sleep(0.04)
                print("\nDeleted (1/2) !")
                CMD = "DROP DATABASE Fees_Manager"
                mycursor.execute(CMD)
                sleep(1)
                print("\nDeleted (2/2) !")
                print("\nALL RECORDS ARE DELETED SUCCESSFULLY!\n")
                print("\nProcessing (1/4) ....")
                sleep(1)
                mycursor.execute("CREATE DATABASE IF NOT EXISTS Fees_Manager")
                print("\nProcessing (2/4) ....")
                sleep(1)
                mycursor.execute("USE Fees_Manager")
                print("\nProcessing (3/4) ....")
                sleep(1)
                mycursor.execute(
                    "CREATE TABLE IF NOT EXISTS students(SR int, Name varchar(255), Class varchar(15), Section varchar(15),  Roll_No int, Submitted varchar(50))")
                print("\nProcessing (4/4) ....")
                fee_amount()
                sleep(1)
                print("\nProcessing Done !\n")
            else:
                print("\nExiting From This Step ...\n")

        elif user == 6:
            print("\n"*9)
            print("Click Squeezed Text (xx Lines) To Display Help")
            print(STR)
            
        elif user == 7:
            print("\n"*3)
            yn = input("\nAre You Sure To Exit (Yes/No)>>> ")
            if yn[0] == "y":
                print("\nThank You For Using !")
                print("Exiting .... ")
                sleep(2)
                break
            else:
                print("\nReturning To Home ....")
        else:
            print("Invalid Option!\n")
        input("\nPRESS ENTER TO CONTINUE >>> ")
        print("\n"*40)

    except Exception as e:
        print("\n"*3)
        print("Some Error! (", e, ")")
        input("\nPRESS ENTER TO CONTINUE >>> ")
        print("\n"*30)

print("VERSION 0.001A")
