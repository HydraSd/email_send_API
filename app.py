from flask import Flask, jsonify, request
from send_mail import *
app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route('/<name>/<email>/<contact>/<dis>', methods=['GET','POST'])
@cross_origin()
def sendMail(name, email, contact, dis):
    SendMessage(name, email, contact, dis)
    return jsonify({"name":name, "email": email, "contact":contact, "description":dis})


if __name__ == "__main__":
    app.run(debug=True)