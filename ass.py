stdata = {}
print()
print("\t\t\t\tWelcome to Student Management System")
print("")
def counsellor(stdata):        
    while(True):
        print("\t\t1.Add Student")
        print("\t\t2.Remove Student")
        print("\t\t3.View all Student")
        print("\t\t4.View Specific Student ")
        print("\t\t5.Exit")
        print("")
        choice = input("Enter a choice by Counsellor:")

        if choice == '1':

            while True:
                print()
                stid = input("Enter a Serial Number:")
                if stid.isdigit() and int(stid) not in stdata:
                    stid = int(stid)
                    break
                elif int(stid) in stdata:
                    print("* Serial Number already exists. Please enter a unique Serial Number. *")
                else:
                    print("* Invalid Serial Number. Please enter a valid number. *")

            fname = input("Enter a First Name:")
            lname = input("Enter a Last Name:")
            subjects={}
            while True:
                contact = input("Enter a Contact Number:")
                if contact.isdigit() and len(contact) == 10:
                    break
                else:
                    print("* Invalid Contact Number. Please enter a valid 10 digit number. *")
            while True:
                subname=input("Enter Subject Name (or 'done' to finish):")
                if subname.lower() == 'done':
                    break
                print()
                marks=input(f"Enter marks for {subname}:")
                fees=input(f"Enter fees for {subname}:")
                print()
                subjects[subname]={'marks':marks,'fees':fees}
                print()
            print()
            faculty=input("Enter a Faculty Name:").lower()

            stdata[stid] = {
                'fname': fname,
                'lname': lname,
                'contact': contact,
                'subject': subjects,
                'faculty': faculty
            }

                    

        elif choice == '2':
            print("")
            print("")
            rem=int(input("Enter Student ID which you want to Remove:"))
            if rem in stdata:
                con=input("Are you want to sure for Remove(Y/N):")
                if con == 'yes' or con == 'y' or con == 'YES' or con == 'Y':
                    del stdata[rem]
                    print()
                    print(" Student Removed succesfuly ")
            else:
                print("* Student does not exist *")

        elif choice == '3':
            print()
            print()
            print(stdata)

        elif choice == '4':
            print()
            print()
            search=int(input("Enter Student ID for View:"))
            print()
            if search in stdata:
                print("-----------------------------------------")
                print(f"Student Name is {stdata[search]['fname']} {stdata[search]['lname']}")
                print(f"Student Contact Number:{stdata[search]['contact']}")
                print()
                for i,j in stdata[search]['subject'].items():
                    print()
                    print(f"Student Subject Name:{i}")
                    print(f"Student Marks:{j['marks']}")
                    print(f"Student Fees:{j['fees']}")
                print()
                print(f"Faculty Name:{stdata[search]['faculty']}")
                print("-----------------------------------------")
            else:
                print("* Student not exist please make sure check student ID *")


        elif choice == '5':
            print()
            print("*_EXIT_*")
            break

        else:
            print()
            print("* please enter valid input *")
                    
def faculty(stdata):
            f_name=input("Enter Faculty Name:").lower()
            while True:

                print("")
                print("\t\t1.Add Marks to Student")
                print("\t\t2.View all Student")
                print("\t\t3.Exit")
                print("")
                fchoice=input("Enter a choice by Faculty:")

                if fchoice == '1':
                    print()
                    sid=int(input("Enter your Student ID:"))
                    print()
                    if f_name == stdata[sid]['faculty']:
                        for i in stdata[sid]['subject']:
                            stdata[sid]['subject'][i]['marks']=input(f'Enter {i} Subject Marks:')
                         
                    else:
                        print()
                        print("* Student does not exist *")
                
                elif fchoice == '2':
                    for stid,stu in stdata.items():
                        if stdata[stid]['faculty'] == f_name:
                            print()
                            print("------------------------------------------------------")
                            print(f"Student First Name = {stu['fname']}")
                            print(f"Student Last Name = {stu['lname']}")
                            print(f"Student Contact = {stu['contact']}")
                            for sub,mar in stu['subject'].items():
                                print()
                                print(f"Subject Name = {sub}")
                                print(f"{sub} Marks = {mar['marks']}")
                                print(f"{sub} Fees = {mar['fees']}")  

                            print()
                            print(f"Faculty Name= {stdata[stid]['faculty'] }")
                            print("------------------------------------------------------")


                
                elif fchoice == '3':
                    print()
                    print("*_Exit_*")
                    break

                else:
                    print("* please enter valid input *")

            

def student(stdata):
            sname=input("Enter Username ('Your Name'):").lower()
            sid=int(input("Enter Password ('Your id'):"))
            if sid in stdata:
                if sname in stdata[sid]['fname']:
                    print("-------------------------------------------------------")
                    print()
                    print(f"NAME={stdata[sid]['fname'].title()} {stdata[sid]['lname'].title()}")
                    print(f"Contact number={stdata[sid]['contact']}")
                    for i,j in stdata[sid]['subject'].items():
                        print()
                        print(f"Subject Name= {i}")
                        print(f"{i} Subject Marks= {j['marks']}")
                        print(f"{i} Subject fees= {j['fees']}")
                        print()
                    print()
                    print(f"Your Faculty Name = {stdata[sid]['faculty']}")
                    print()
                    print("-------------------------------------------------------")

                    
                else:
                    print('* sorry! incorect Username *')
            else:
                print("* incorect Password *")

def role():
    while(True):
            print("\t\tpress 1 for Counsellor")
            print("\t\tpress 2 for Faculty")
            print("\t\tpress 3 for Student")
            print("\t\tpress 4 for Exit")
            
            print("")
            rid=input("Enter a Role ID:")
            print("")
            if rid == '1':
                counsellor(stdata)
            elif rid == '2':
                faculty(stdata)
            elif rid == '3':
                student(stdata)
            elif rid == '4':
                print()
                print("*_EXIT_*")
                break
            else:
                print("* please enter valid Role ID *")
                print("")


role()