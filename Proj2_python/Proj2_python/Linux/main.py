#Zakiya AbuMurra
#Ibrahem Dehadi


import os
import matplotlib.pyplot as plt
import traceback

class Semister:
    def __init__(self,semnumber,courses):
        self.semnumber=semnumber
        self.courses=courses




path="inputs"
os.chdir(path)

def updatestudent(studentid,stud):
    file = open(studentid,"w")
    file.close()
    for i in stud:
        s=""
        s+=i.semnumber + " ; "
        l=list(i.courses.keys())
        for j in l :
            s+=j +" " + i.courses[j] +", "
        f= open(studentid,"a")
        s=s[:-2]
        f.write(s +"\n")
        f.close()


def readstudent(studentid):
    stud=[] #LIST
    file = open(studentid,"r") #OPEN ID FILE
    line =file.readline()
    print(studentid)

    while line:
        line = line.strip() #REMOVE SPACES
        line = line.replace("\n","") #TRANSLATE THE NEWLINE TO SPACE
        temp = line.split(";") #REMOVE ';' AND STORE THE RESULT IN TEMP LIST
        sem=temp[0] #sem  IS FIRST INDEX IN TEMP LIST
        sem=sem.strip()
        courgrad = temp[1]
        l=[]
        l=courgrad.split(",")
        dec={} #DICTIONARY
        for i in l :
            l1=[]
            l1=i.split(" ")
            dec[l1[1].strip()] = l1[2].strip()

        stud.append(Semister(sem,dec))
        line = file.readline()


    return stud
def addsem(studentid,sem):
    file=open(studentid,"a")
    file.write(sem+"\n")
    file.close()
    return

#READ COURSES FROM COURSES FILE
def readcourses(courses):

    file = open("C:/Users/Asus/Documents/Python/Linux/Courses.txt","r")

    line=" "
    while line:
        line =file.readline() #READ THE FIRST LINE
        #print(line)
        line=line.strip("\n") #REMOVE THE NEW LINE FROM THE END AND THE BEGINNING OF THE FILE
        line=line.strip(" ")  #REMOVE THE SPACE FROM END AND BEGINNGING OF THE FILE
        #print(line)
        courses.append(line)
    file.close()
    courses.pop()
    return courses
#this function check if the entered id is digit number or not
def checkisdigits(studentid):
    if studentid.isdigit() == False:
        return False
    return True

#THIS FUNCTION CHECK IF THE ID NUMBER IS UNIQUE OR NOT , ITS RETURN TRUE IF THERE IS AN ID ALREADY IN THE SYSTEM
def checkinthesystem(studentid):
    for f in os.listdir():
        if f.strip(".txt")==studentid:
           return True
    return False

#FUNCATION THAT CHECK IF THE ENTERED SEMESTER IS EXIST IN THE ID RECORD
def checkvalidationsem(studentid,yearsem):
    file=open(studentid,"r")
    line=" "
    while line:
        line=file.readline()
        sp=line.split(';')

        if sp[0].replace(" ","")==yearsem:
            return False
    return True


#TO GET THE TAKEN HOUR BU STUDENT AND REMAIN COURSES
def Taken_hour_and_remain_gcourses(stud, courses):
    dec={} #DICTIONARY
    stat={}
    reamningcourses=[]
    nontakenhour=0

    for i in courses:
        dec[i]=False   #AS A FLAG
    for i in stud:
        s = 0
        takenhours = 0
        l = list(i.courses.keys())
        for j in l : #loop in course dictionary and set a flag true for the courses are taken
            dec[j]=True
            s+=(int(j[5])*int(i.courses[j]))
            takenhours+=int(j[5]) #index 5 in encs313 for example represent the number of hour for this course
            l1=[]
            l1.append(s/takenhours)
            l1.append(takenhours)
        stat[i.semnumber]=l1

    l=list(dec.keys())
    for i in l:
        if dec[i]==False:
            reamningcourses.append(i)
    return stat,reamningcourses


#Add a new record file
def record():
    studentid = input("please enter the student id\n")
    if checkisdigits(studentid)==False: #CALL THE FUNCTION THAT CHECK IF THE ENTERD ID IS DIGIT OR NOT
        print("the student id must be digits only")
        return

    if checkinthesystem(studentid)==True: #CALL THE FUNCTION THAT CHECK IF THE ID IS UNIQUE OR NOT
        print("error...the student already in the system")
        return

    newrecord=studentid+".txt"
    os.path.join(path, newrecord) #ADD THE ENTERD ID NUMBER BY USER TO THE RECORD SYSTEM AS A TEXT FILE
    newrecord=open(newrecord,"w")
    newrecord.write("")
    newrecord.close()

#Add new semester with student course and grades
def newsem():
   studentid = input("please enter the student id :\n")#ENTER ID THAT  ALREADY EXISIT IN RECORD SYSTEM TO ADD NWE SEMESTER
   #CHECK IF THE ENTERED ID IS DIGIT NUMBER OR NOT
   if checkisdigits(studentid)==False:
       print("the student id must be digit only\n")
       return
   #CHECK IF THE ENTERED ID ID UNIQUE OR NOT BY CALLING FUNCTION THAT DO IT
   if checkinthesystem(studentid)==False:
       print("the user not in the system\n")
       return

   studentid+=".txt"
   sem=""
   while True:
       try: #USE EXCEPTIONS TO PRINT ERROE MESSAGE
           year = input("Please enter the year (it should in form x-x) . \n")
           if "-" in year:
               l = year.split('-') #SPLIT THR INPUT INTO LIST (l)
               l = list(map(int, l)) #CONVERT THE CONTENT OF LIST TO INTEGER TYPE TO CHECK IF THE NUMBERS BETWEEN A SPECIFIC INTERVAL
               if (l[0] >= 1900 and l[0] <= 2030 and l[1] >= 1900 and l[1] <= 2030 and l[1] == l[0] + 1) == False:  #CHECK THE CONTENT OF LIST l
                   e = TypeError("invalid year")
                   raise e
           else:
               e=TypeError("you miss the - symbol")
               raise e

           sem=input("Please enter the semester number ( '1' means the first semester , '2' means the second semseter , '3' means the Summer semester  ) :\n")
           if sem !="1" and sem !="2" and sem !="3":
               e=TypeError("wrong sem...the semister should be 1 or 2 or 3")
               raise e

           semester=""
           semyear=year+"/"+sem #2020-2021/1 FOR EXAMPLE
           semester+=semyear+" ;" #2020-2021/1 ; FOR EXAMPLE , AFTER ";" WE ADD LETER THE COURSE



           if checkvalidationsem(studentid,semyear)==False:
               e=TypeError("the semester you add is already in the record")
               raise e
           courses=[]
           courses = readcourses(courses)#CALL THE readcousres() function to print the coursese
           print(courses)
           while True:
               try:
                   corse=input("Please enter the course or -1 to exit\n")
                   corse=corse.upper()
                   if corse=="-1":
                       break
                   if (courses.count(corse)>0) ==False:
                       ex=TypeError("the course not found please add a valid one")
                       raise ex
                   grade=input("please enter the grade\n")
                   if (checkisdigits(grade)==False) or (int(grade) < 0 or int(grade)>100)==True:
                        ex=TypeError("the grade is not valid")
                        raise ex
                   semester+=" "+ corse +" " + grade+","


               except Exception as ex :
                   print(ex)
           if semester == semyear +" ;":
                e=TypeError("please enter courses to add to the record")
                raise e
           semester=semester[:-1]
           addsem(studentid,semester)
           break
       except Exception as e :
             print(e)
             continue





#update courese and grades
def update():
    studentid = input("please enter the student id :\n")
    if checkisdigits(studentid) == False:
        print("the student id must be digit only\n")
        return
    if checkinthesystem(studentid) == False: #CALL THE FUNCTION THAT CHECK IF THE ENTERED ID ID ALREADY EXISIT OR NOT
        print("the user not in the system\n")
        return
    studentid += ".txt"
    courses= [] #LIST OF COURSES
    courses=readcourses(courses)


    stud=[]
    stud =readstudent(studentid)

    course = input("please enter the course you want to update\n")
    grad=input("please enter the new grade\n")
    course = course.upper() #CONVERT THE INPUT TO UPPER CASE THAT SUITABLE WITH THE FILE OF COURSES

    try:
        if (courses.count(course) > 0) == False:
            e = TypeError("the course not found please add a valid one")
            raise e
        for i in stud :
            if course in i.courses:
                i.courses[course]=grad
        for i in stud:
            print(i.semnumber, i.courses)
        updatestudent(studentid,stud)
    except Exception as e:
        print(e)

        return
#Student statistics
def studentstat():
    studentid = input("please enter the student id :\n")
    if checkisdigits(studentid) == False:
        print("the student id must be digit only\n")
        return
    if checkinthesystem(studentid) == False:
        print("the user not in the system\n")
        return
    studentid += ".txt"
    if (os.path.getsize(studentid) == 0 ):
        print("The student does not have any courses . Please add courses to this student and try again ! .\n")
        return 
    courses = []
    courses = readcourses(courses)
    stud = []
    stud = readstudent(studentid)
    stat,remainingcourses = Taken_hour_and_remain_gcourses(stud, courses)
    for i in stat:
        print("semester : " + i + " ---->  average : %.2f,taken hour : %d "%(stat[i][0],stat[i][1]))
    print(f"remaining courses --->{remainingcourses}")
    allhours=0
    s=0

    for i in stat :
       s+=stat[i][0]*stat[i][1]
       allhours+=stat[i][1]
    print("over all avg ---> %.2f\ntaken hours --->%d"%(s/allhours,allhours))

def allstudentstat():
    avg = {}
    takenhour = {}
    coursemap = {}
    for file in os.listdir():
        if os.path.getsize(file) == 0:
            continue
        stud = []
        course = []
        stud = readstudent(file)
        for i in stud:
            temp = list(i.courses.keys())
            if file in coursemap:
                coursemap[file] = coursemap[file] + temp
            else:
                coursemap[file] = temp


        course = readcourses(course)
        stat, remain = Taken_hour_and_remain_gcourses(stud, course)

        s = 0
        t = 0

        for i in stat:
            s += stat[i][0] * stat[i][1]
            t += stat[i][1]

        takenhour[file] = t
        avg[file] = s / t
    return  avg,takenhour,coursemap
#To find all information about student and call the functions that calculate the average for each and all student .
def globalstat():

    avg, takenhour, corsemap = allstudentstat()
    print(f"avg for all students ---> {avg}"
          f"taken hour for all students ---> {takenhour}\n"
          f"taken courses for all student : \n")
    for i in corsemap:
        print("student------taken courses\n"
              f"{i}\t\t{corsemap[i]}")
    l = list(avg.values())
    l1 = list(takenhour.values())
    formatter = "{0:.3f}"
    print(f"average for all students ---> {formatter.format(sum(l) / len(l))}\n"
          f"average for taken hours ---> {formatter.format(sum(l1) / len(l1))}")
    plt.hist(l)
    plt.show()
#Search function 
def search():
    avg,takenhour,coursemap = allstudentstat()
    while True:
        s1=set()
        choice=input("please chose the criteria you want to search\n"
          "1-average\n"
          "2-taken hour\n"
          "3-courses\n"
          "4-back to menu\n")
        if choice=="1":

            avg3=input("please enter the average you search for\n")
            if avg3.isdigit()==False:
                print("the avg should be only degits")
                continue

            c=input("chose what you want to search : \n"
                  "1-less\n"
                  "2-grater\n"
                  "3-equal\n")
            if (c=="1" or c=="2" or c=="3")==False:
                print("error...chose a valid input")
                break
            if c =="1":
                for i in avg:
                    if avg[i] < int(avg3):
                        s1.add(i)

            if c== "2":
                for i in avg :
                    if avg[i] > int(avg3):
                        s1.add(i)
            if c=="3" :
                for i in avg :
                    if avg[i]==int(avg3):
                        s1.add(i)
            print(f"the students is : {s1}")
            continue




        if choice=="2":
            takenh = input("please enter the taken hours\n")
            if takenh.isdigit()==False:
                print("the taken hours should be only digits")
                continue
            for i in takenhour:
                if takenhour[i] == int(takenh):
                    s1.add(i)
            print(f"the students is : {s1}")
            continue

        if choice=="3":
            cour=input("please enter the course you search for : \n")
            cour=cour.upper()
            for i in coursemap:
                if cour in coursemap[i]:
                    s1.add(i)
            print(f"the students is : {s1}")
            continue
            
        if choice=="4" :
            break
        else :
            print("error in choice")
            continue

    return
#HERE, THE MENU AND CALLING THE NEED FUNCTION
while True :
    login=input("\twelcome to our student recording system\n--------------------------------------------\n\tplease "
                "chose Admin or "
                "user\n "
          "\t\t1-Admin"
          "\n\t\t2-User"
          "\n\t\t3-End the program\n--------------------------------------------\n")
    if login =="1":
        while True:
            print("\t\twelcome to Admin page\n--------------------------------------------\n\tplease chose frome the "
                  "menu\n"
                  "\t\t1-Add new record to the system\n"
                  "\t\t2-Add new semester to the student record\n"
                  "\t\t3-update student record\n"
                  "\t\t4-Student statistics\n"
                  "\t\t5-Global statistics\n"
                  "\t\t6-Searching\n"
                  "\t\t7-return to login\n--------------------------------------------")
            choice = input()
            if choice=="1":
                record()
            elif choice =="2":
                newsem()
            elif choice =="3":
                update()
            elif choice=="4":
                studentstat()
            elif choice =="5":
                globalstat()
            elif choice=="6":
                search()
            elif choice=="7":
                break
            else :
                print("error choice please chose again\n")



    elif login == "2":
        print("\t\twelcome to user page\n--------------------------------------------\n")
        id=input("\t\tplease enter your number\n")
        if checkisdigits(id) ==False:
            print("the id should be digits only!!")
            continue

        if checkinthesystem(id) ==False:
            print("the user does not in the system!!")
            continue
        id = id+".txt"

        while True:
            print("\n_____________________________________________________________\n")
            c=input("\t\tplease chosse from the menu\n"
                         "\t\t1-my statistics .\n"
                         "\t\t2-global statistics . \n"
                         "\t\t3-back to menu . \n"
                    "____________________________________________________________\n")
            if c == "1":
                stud = readstudent(id)
                courses = []
                courses = readcourses(courses)
                stat,remain = Taken_hour_and_remain_gcourses(stud, courses)
                t=0
                s=0
                for i in stat :
                    s+= stat[i][0]*stat[i][1]
                    t+=stat[i][1]

                avg = s/t
                f= "{0:.2f}"
                print(f"your statistics is : \n"
                      f"1- overall avg ---> {f.format(avg)}\n"
                      f"2-all taken hours ---> {t}\n"
                      f"3-\tsemester------ taken hours ------avg  \n")
                for i in stat :
                    print(f"\t{i}------{stat[i][1]}----------{stat[i][0]}")
                print(f"\tRemaining courses : \n\t{remain}")
                continue
            if c =="2":
                globalstat()
                continue
            if c =="3":
                break
            else :
                print("error in choice please chose again")
                continue
    elif login=="3":
        break
    else :
        print("error in choice please chose a valid one")

print("bye bye(:(:")
