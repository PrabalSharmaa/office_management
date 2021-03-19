print(r'''
                               __          __  _                            _______
                               \ \        / / | |                          |__   __|
                                \ \  /\  / /__| | ___ ___  _ __ ___   ___     | | ___
                                 \ \/  \/ / _ \ |/ __/ _ \| '_ ` _ \ / _ \    | |/ _ \
                                  \  /\  /  __/ | (_| (_) | | | | | |  __/    | | (_) |
                                   \/  \/ \___|_|\___\___/|_| |_| |_|\___|    |_|\___/


''')
print(r'''
   ____   __  __ _            __  __                                                   _      _____           _
  / __ \ / _|/ _(_)          |  \/  |                                                 | |    / ____|         | |
 | |  | | |_| |_ _  ___ ___  | \  / | __ _ _ __   __ _  __ _  ___ _ __ ___   ___ _ __ | |_  | (___  _   _ ___| |_ ___ _ __ ___
 | |  | |  _|  _| |/ __/ _ \ | |\/| |/ _` | '_ \ / _` |/ _` |/ _ \ '_ ` _ \ / _ \ '_ \| __|  \___ \| | | / __| __/ _ \ '_ ` _ \
 | |__| | | | | | | (_|  __/ | |  | | (_| | | | | (_| | (_| |  __/ | | | | |  __/ | | | |_   ____) | |_| \__ \ ||  __/ | | | | |
  \____/|_| |_| |_|\___\___| |_|  |_|\__,_|_| |_|\__,_|\__, |\___|_| |_| |_|\___|_| |_|\__| |_____/ \__, |___/\__\___|_| |_| |_|
                                                        __/ |                                        __/ |
                                                       |___/                                        |___/

						    -Prabal Sharma
''')

#import mysql data
def Employee():
    empid=input("\nEnter id: ")
    emppass=input("Enter password: ")
    e=open('emplog.txt')
    for line in e:
        line=line.rstrip()
        if(line==empid+' '+emppass):
            print('\n***Welcome',empid+'***')
            print("""
                1. Your Details
                2. Your Attendance
                3. Projects and Deadline
                4. Back
            """)
            ch=input("\n***Enter Task No***")
            while True:
                if(ch=='1'):
                    Empdetails(empid)
                elif(ch=='2'):
                    Attendance(empid)
                elif(ch=='3'):
                    Project(empid)
                elif(ch=='4'):
                    main()
                else:
                    print("\n***Wrong Choice***")
                break
            i=input('\nPress *q* to main menu: ')
            if(i=='q'):
                main()
            return

    print('\n***Sorry Wrong ID or Password***')
    main()

    #checking from Sql data
    #if else loop-for authentication
    #Attendance(),Project(),Empdetails()

def Attendance(u):
    att=open('empatt.txt')
    for t in att:
        t=t.rstrip()
        p=list(t.split(' '))
        if(p[0]==u):
            print('\nAttendance of this month:',p[1],'Days')
            break
    #show attendance

def Project(s):
    pr=open('prodet.txt')
    for z in pr:
        z=z.rstrip()
        y=list(z.split(' '))
        if(y[0]==s):
            print('\nYour Current Project:',y[1],'Deadline:',y[2])
            break
    #show project details

def Empdetails(r):
    det=open('empdet.txt')
    for q in det:
        q=q.rstrip()
        w=list(q.split(' '))
        if(w[0]==r):
            print('\nPost:',w[1])
            print('Gender:',w[2])
            print('Email: ',w[3])
            print('Salary: Rs.',w[4])
            break
    #show Employee Empdetails

def Admin():
    admid=input("\nEnter id: ")
    admpass=input("Enter password: ")
    det=open('admlog.txt')
    for line in det:
        line=line.rstrip()
        if(line==admid+' '+admpass):
            print('\n***Welcome',admid+'***')
            print("""
                1. All Employees Details
                2. Employees' Attendance
                3. Back
            """)
            ch=input("\n***Enter Task No***")
            while True:
                if(ch=='1'):
                    Allempdetails()
                elif(ch=='2'):
                    Allempatt()
                elif(ch=='3'):
                    main()
                else:
                    print("\n***Wrong Choice***")
                break
            return
#        else:
    print('***Sorry Wrong ID or Password***')
    main()
    #checking from Sql data
    #if else loop-for authentication
    #ProjectEDIT(),EmpdetailsEDIT()

def Allempdetails():
    ale=open('empdet.txt')
    for tu in ale:
        tu=tu.rstrip()
        po=list(tu.split(' '))
        print('\nName: ',po[0])
        print('Post:',po[1])
        print('Gender:',po[2])
        print('Email: ',po[3])
        print('Salary: Rs.',po[4])
    i=input('\nPress *q* to main menu: ')
    if(i=='q'):
        main()
    return

def Allempatt():
    ale=open('empatt.txt')
    for tu in ale:
        tu=tu.rstrip()
        po=list(tu.split(' '))
        print('\nName: ',po[0])
        print('Attendance: ',po[1])
    i=input('\nPress *q* to main menu: ')
    if(i=='q'):
        main()
    return

def main():
    print("""
    1. Employee Login
    2. Admin Login
    """)
    choice=input("***Enter Task No***")
    while True:
        if(choice=='1'):
            Employee()
        elif(choice=='2'):
            Admin()
        else:
            print("***Wrong Choice***")

main()
