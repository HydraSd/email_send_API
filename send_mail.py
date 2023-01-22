from email.message import EmailMessage
import smtplib
import ssl

def SendMessage(name, email, contact, dis):
    email_sender = "testdool983@gmail.com"
    email_password = "pqxiloodjgsmgcos"

    email_reciever = "doolwala.kimal@gmail.com"
    subject = "Message from website"
    body = f"Name : {name} \n Email : {email} \n Contact : {contact} \n Description : {dis}"

    em = EmailMessage()
    em['From'] = email_sender
    em['To'] = email_reciever
    em['subject'] = subject
    em.set_content(body)

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
        smtp.login(email_sender, email_password)
        smtp.sendmail(email_sender, email_reciever, em.as_string())
        print("..send")