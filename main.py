from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import os
from flask_cors import CORS
import pyrebase
from random import choices
import string
# from flask_mail import Mail, Message
# app = Flask(__name__, static_folder="./dist", static_url_path='/')
app = Flask(__name__)
CORS(app, origins=["https://smgtherapy.netlify.app"])

# Set the SQLAlchemy configuration using the DATABASE_URL environment variable
database_url = os.getenv("DATABASE_URL")
app.config['SQLALCHEMY_DATABASE_URI'] = database_url

# "postgresql://postgres:oHtTmFO0HRJ5l3EKfuRn@containers-us-west-133.railway.app:5870/railway"
config = {
    "apiKey": "AIzaSyDkCfsf_cqssNgpVjXzhANxmf6iPq-XcmY",
    "authDomain": "smgtherapy-10277.firebaseapp.com",
    "projectId": "smgtherapy-10277",
    "storageBucket": "smgtherapy-10277.appspot.com",
    "messagingSenderId": "409460478726",
    "appId": "1:409460478726:web:efa68b8ebc4e5a89db4487",
    "databaseURL": ""
}
firebase = pyrebase.initialize_app(config)
auth = firebase.auth()

# Create the SQLAlchemy database object
db = SQLAlchemy(app)

class Feedback(db.Model):
    __tablename__ = 'smg'
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(200))
    last_name = db.Column(db.String(200))
    email = db.Column(db.String(200))
    massage_type = db.Column(db.String(200))
    time_date = db.Column(db.String(20))
        
    def __init__(self, first_name, last_name, email, massage_type, time_date):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.massage_type = massage_type
        self.time_date = time_date
        
class TimeSetter(db.Model):
    __tablename__ = 'time_dates'
    id = db.Column(db.Integer, primary_key=True)
    time_date = db.Column(db.String(20))

    def __init__(self, time_date):
        self.time_date = time_date

        
@app.route('/Home') 
def index():
    # return app.send_static_file('index.html')
    return "Hey"


@app.route('/api/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        data = request.get_json()
        
        firstname = data.get('firstName')
        lastname = data.get('lastName')
        email = data.get('email')
        massagetype = data.get('massageType')
        time_date = data.get('time_date')
        
        # Create a new Feedback instance using the correct column names
        new_entry = Feedback(first_name=firstname, last_name=lastname, email=email, massage_type=massagetype, time_date=time_date)
        db.session.add(new_entry)
        db.session.commit()  

        # Check if the new record exists in the 'time_dates' table
        matching_record = TimeSetter.query.filter_by(time_date=time_date).first()
        if matching_record:
            # Delete the matching record from the 'time_dates' table
            db.session.delete(matching_record)
            db.session.commit()
            return jsonify({"message": "Saved entry and deleted matching record from 'time_dates'!"})
        else:
            return jsonify({"message": "Saved entry but no matching record found in 'time_dates'."})

    
@app.route('/DisplayAppointment', methods=['GET', 'POST'])
def Appointments():
    
    if request.method == 'POST':
        data = request.get_json()
                
        time = data.get('time')
        date = data.get('date')
        
        
        time_date = f"{date} Time {time}"
        
        # Create a new TimeSetter instance with the modified time_date
        new_entry = TimeSetter(time_date=time_date)
        db.session.add(new_entry)
        db.session.commit()
    
        return jsonify({"message": "HI"})
        
    if request.method == 'GET':

        appointments = TimeSetter.query.all()

        appointment_list = []

        for appointment in appointments:
            appointment_avl = {
                "id": appointment.id,
                "time_date": appointment.time_date
            }

            appointment_list.append(appointment_avl)

        return jsonify(appointment_list)



@app.route('/clients', methods=['GET'])
def clients():

    clients = Feedback.query.all()

    client_list = []

    for client in clients:
        client_info = {
            "first_name": client.first_name,
            "last_name": client.last_name,
            "email": client.email,
            "massage_type": client.massage_type,
            "time_date": client.time_date
        }

        client_list.append(client_info)

    return jsonify(client_list)

@app.route('/login', methods=['POST'])
def login():
    data = request.json
    email = data['email']
    password = data['password']
    try:
        user = auth.sign_in_with_email_and_password(email, password)
        # Successfully authenticated
        return jsonify({"message": "Login successful", "uid": user['localId']})
    except Exception as e:
        # Authentication failed
        return jsonify({"error": str(e)}), 401
    
if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))
