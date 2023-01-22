from flask import Flask, jsonify, request
from email.message import EmailMessage
from flask_cors import CORS, cross_origin

import smtplib
import ssl
app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route('/<name>/<email>/<contact>/<dis>', methods=['GET'])
@cross_origin()
def sendMail(name, email, contact, dis):
    email_sender = "testdool983@gmail.com"
    email_password = "vfmcwrxnvvziuqzm"
    email_reciever = "doolwala.kimal@gmail.com"

    subject = name
    body = f"Name : {name} \n Email: {email} \n Contact : {contact} \n description : {dis}"
    
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

    return jsonify({"name":name, "email": email, "contact":contact, "description":dis})


if __name__ == "__main__":
    app.run(debug=True)