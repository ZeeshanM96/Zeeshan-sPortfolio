from flask import Flask, request, jsonify
from flask_mail import Mail, Message
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


app.config['MAIL_SERVER'] = 'smtp.outlook.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USERNAME'] = 'zeeshan.majeed96@outlook.com' 
app.config['MAIL_PASSWORD'] = 'Pakistan042' 
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False

mail = Mail(app)

@app.route('/send_email', methods=['POST'])
def send_email():
    name = request.form.get('name')
    email = request.form.get('email')
    message = request.form.get('message')

    # Create the message
    msg = Message("New Message from Your Portfolio Website",
                  sender=app.config['MAIL_USERNAME'],
                  recipients=['zeeshan.majeed96@outlook.com']) 
    msg.body = f"From: {name} ({email})\n\nMessage: {message}"
    mail.send(msg)

    return jsonify({"status": "success"})

if __name__ == '__main__':
    app.run(debug=True)
