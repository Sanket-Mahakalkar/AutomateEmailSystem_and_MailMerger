# AutomateEmailSystem_and_MailMerger

In this Automate Email System we can send mail to 1000s of people at a time. The details of people to whom we need to send the mail is stored in a csv file.
CSV or Comma Separated Values is a very common data format used to store data as a segment of text separated by commas. It can be assume like a spreadsheet.
Here I have used a "myfile.txt" to store the data which contains coloumn like Name,Email_Id,College,Hobby.
This system contain 2 program files : 
readCSV.py which read the csv file and emails.py send the mail to recipients.
I have imported emails.py file in readCSV.py so we only need to run the readCSV.py file.

This system sends a personalised mail content. Like in body if we have to use the name, college etc of that particular person then we can add it to his/her mail body.
For that i have make use of regular expression in python. In regex we can replaced the matched charachter with the one we want.
just like real life application Mail Merger do.

This system also check the duplicacy. If we have two files like here I have used "myfile2.txt" it may happen that the same name may appear in both the files.
So this system also check for the duplicate names and give us a pop up message whether to send the mail again to that person or not.
It can also work if the same file contain duplicate information.
