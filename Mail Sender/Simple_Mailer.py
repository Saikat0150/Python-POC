from flask import *
from flask_mail import *


app = Flask(__name__)
mail = Mail(app)


# Flask mail configuration
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 456
app.config['MAIL_USERNAME'] = 'saikat.sanil.0150@gmail.com'
app.config['MAIL_PASSWORD'] = 'jmoo gkfd zvma ssiu'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True


# instantiate the Mail class
mail = Mail(app)


# Configure the Message class object and send the mail for
@app.route('/')
def index():
    msg = Message('Subject', sender='saikat.sanil.0150@gmail.com', recipients=['saikat.sanil.0150@gmail.com'])
    msg.body = 'hi, this is the mail send by using the flask web application'
    mail.send(msg)
    return "Mail sent, Please check the mail id"


if __name__ == "__main__":
    app.run(debug=True, port=9090)

