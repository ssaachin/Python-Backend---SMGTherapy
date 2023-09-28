# from flask import Flask, request, jsonify
# from flask_sqlalchemy import SQLAlchemy
# from flask_pymongo import PyMongo
# import os
# from flask_cors import CORS
# import pyrebase
# # from flask_mail import Mail, Message

# # app = Flask(__name__, static_folder="./dist", static_url_path='/')
# app = Flask(__name__)

# CORS(app, origins=["https://smgtherapy.netlify.app"])
# # Set the SQLAlchemy configuration using the DATABASE_URL environment variable
# database_url = os.getenv("DATABASE_URL")
# app.config['SQLALCHEMY_DATABASE_URI'] = database_url
# # "postgresql://postgres:oHtTmFO0HRJ5l3EKfuRn@containers-us-west-133.railway.app:5870/railway"

# MONGO_URL = os.environ.get("MONGO_URL")
# MONGO_HOST = os.environ.get("MONGOHOST") 
# MONGO_PASSWORD = os.environ.get("MONGOPASSWORD")
# MONGO_PORT = os.environ.get("MONGOPORT")
# MONGO_USER = os.environ.get("MONGOUSER")
# MONGO_COLLECTION = "test"

# app.config["MONGO_URI"] = "mongodb://"+ MONGO_USER +":"+ MONGO_PASSWORD +"@"+ MONGO_HOST +":"+ MONGO_PORT +"/"+ MONGO_COLLECTION
# mongo = PyMongo(app)

# config = {
#     "apiKey": "AIzaSyDkCfsf_cqssNgpVjXzhANxmf6iPq-XcmY",
#     "authDomain": "smgtherapy-10277.firebaseapp.com",
#     "projectId": "smgtherapy-10277",
#     "storageBucket": "smgtherapy-10277.appspot.com",
#     "messagingSenderId": "409460478726",
#     "appId": "1:409460478726:web:efa68b8ebc4e5a89db4487",
#     "databaseURL": ""
# }

# firebase = pyrebase.initialize_app(config)
# auth = firebase.auth()

# # Create the SQLAlchemy database object
# db = SQLAlchemy(app)

# class Feedback(db.Model):
#     __tablename__ = 'smg_customer'
#     id = db.Column(db.Integer, primary_key=True)
#     first_name = db.Column(db.String(200), unique=True)
#     last_name = db.Column(db.String(200))
#     email = db.Column(db.String(200))
#     massage_type = db.Column(db.String(200))
#     time = db.Column(db.String(20))
#     date = db.Column(db.String(20))

#     def __init__(self, first_name, last_name, email, massage_type, time, date):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.email = email
#         self.massage_type = massage_type
#         self.time = time
#         self.date = date



# @app.route('/Home') 
# def index():
#     # return app.send_static_file('index.html')
#     return "Heycvc"


# @app.route('/api/submit', methods=['POST'])
# def submit():
#     if request.method == 'POST':
#         data = request.get_json()
        
#         firstname = data.get('firstName')
#         lastname = data.get('lastName')
#         email = data.get('email')
#         massagetype = data.get('massageType')
#         time = data.get('time')
#         date = data.get('date')

#         # Create a new Feedback instance using the correct column names
#         new_entry = Feedback(first_name=firstname, last_name=lastname, email=email, massage_type=massagetype, time=time, date=date)

#         db.session.add(new_entry)
#         db.session.commit()  

#         return jsonify({"message": "Saved entry!"})
    
# @app.route('/clients', methods=['GET'])
# def clients():
    
#     clients = Feedback.query.all()
    
#     client_list = []
    
#     for client in clients:
#         client_info = {
#             "first_name": client.first_name,
#             "last_name": client.last_name,
#             "email": client.email,
#             "massage_type": client.massage_type,
#             "time": client.time,
#             "date": client.date
#         }
        
#         client_list.append(client_info)
        
#     return jsonify(client_list)


# @app.route('/appointment', methods=['POST'])
# def create_appointment():
#     try:
#         data = request.get_json()
#         date = data.get('date')
#         time = data.get('time')
        
#         # You can insert the date and time into your "SMG" collection here
#         # Assuming your MongoDB database is correctly configured in the app
#         mongo.db.SMG.insert_one({
#             "date": date,
#             "time": time
#         })

#         return jsonify({'message': 'Appointment created in MongoDB'})
#     except Exception as e:
#         return jsonify({'error': str(e)}), 500  # Handle any errors that may occur

# @app.route('/login', methods=['POST'])
# def login():
#     data = request.json
#     email = data['email']
#     password = data['password']

#     try:
#         user = auth.sign_in_with_email_and_password(email, password)
#         # Successfully authenticated
#         return jsonify({"message": "Login successful", "uid": user['localId']})
#     except Exception as e:
#         # Authentication failed
#         return jsonify({"error": str(e)}), 401  

# if __name__ == '__main__':
#     app.run(debug=True, port=os.getenv("PORT", default=5000))


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

    
@app.route('/DisplayAppointment', methods=['GET', 'POST', 'DELETE'])
def Appointments():
    
    if request.method == 'POST':
        data = request.get_json()
            
        time = data.get('time')
        date = data.get('date')
            
        time_date = f"{date} {time}"
            
            
        # Create a new TimeSetter instance with the random code
        new_entry = TimeSetter(time_date=time_date)
        db.session.add(new_entry)
        db.session.commit()  

        return jsonify({"message": "HI"})
        
    if request.method == 'GET':

        appointments = TimeSetter.query.all()

        appointment_list = []

        for appointment in appointments:
            appointment_avl = {
                "time_date": appointment.time_date,
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
