import os.path
import csv
import re
import emails


def readFile(row):

    flag='true'
    names,email_id,hobby,college=row

    #If duplicacy is found then we decide whether to send the mail again or not
    if email_id in Email_Id:
        print("The given mail has already sent to "+names+". Do you want to send the mail again ?")
        val=input("Enter yes/no : ")
        if val=='yes':
            flag='true';
        else:
            flag='false'

#we store the coloumn of a csv file in their respective list
    if(flag=='true'):
        name.append(names)
        Email_Id.append(email_id)
        Hobby.append(hobby)
        colleges.append(college)

name=[]
Email_Id=[]
Hobby=[]
colleges=[]

#we read the details of people from this file and mail them to their respective Email Id
with open("myfile.txt") as file:
    csv_f=csv.reader(file)
    for row in csv_f:
        readFile(row)


duplicateFile="myfile2.txt"
#This check whether second file contains the person to whom we have already sent a mail
if not duplicateFile=="":
    with open(duplicateFile) as file:

        csv_f=csv.reader(file)
        for row in csv_f:
            readFile(row)

body="Hi NAME,\nHow are you? Its being a long while we aren't in touch.\nYou are studing in COLLEGE college. Am i right?\nHow is your HOBBY practice going on ?"
subject="Automate Email System - Project"


attachment_path="example.pdf"
for i in range(len(name)):
    body_temp=body
    body_temp=re.sub(r"NAME",name[i],body_temp)
    body_temp=re.sub(r"COLLEGE",colleges[i],body_temp)
    body_temp=re.sub(r"HOBBY",Hobby[i],body_temp)

    message=emails.generateEmail('example@gmail.com',Email_Id[i],subject,body_temp,attachment_path)
    emails.send_email(message)

print("Email has been sent to all successfully")
