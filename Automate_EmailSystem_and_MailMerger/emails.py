#!usr/bin/env python3
import email.message
import mimetypes
import os.path
import smtplib
import getpass

def generateEmail(sender,recipient,subject,body,attachment_path):
    #Basic Email formatting
    message=email.message.EmailMessage()
    message['From']=sender
    message['To']=recipient
    message['Subject']=subject
    message.set_content(body)


    #Process the attachment if any and add it to mail

    if not attachment_path=="":
        attachment_filename=os.path.basename(attachment_path)
        mime_type, _ = mimetypes.guess_type(attachment_path)
        mime_type, mime_subtype=mime_type.split('/',1)

        with open(attachment_path,'rb') as ap:
            message.add_attachment(ap.read(),
                                   maintype=mime_type,
                                   subtype=mime_subtype,
                                   filename=attachment_filename)

    return message

#Let's put the Email password into a variable so it's not visible on the screen.
mail_pass=getpass.getpass('Password? ')

#we need to create a mail server and  we can authenticate to the email server using the SMTP object's login method.
def send_email(message):
    mail_server = smtplib.SMTP_SSL('smtp.gmail.com',465)
    mail_server.login('mahakalkar111sanket@gmail.com', mail_pass)
    mail_server.send_message(message)
    mail_server.quit()
