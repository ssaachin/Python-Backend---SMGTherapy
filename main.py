# from flask import Flask, request, jsonify
# from flask_sqlalchemy import SQLAlchemy
# from flask_pymongo import PyMongo
# import os
# from flask_cors import CORS
# import pyrebase
# from flask_login import LoginManager
# # from flask_mail import Mail, Message

# # app = Flask(__name__, static_folder="./dist", static_url_path='/')
# app = Flask(__name__)

# CORS(app, origins=["https://smgtherapy.netlify.app"])
# # Set the SQLAlchemy configuration using the DATABASE_URL environment variable
# # database_url = os.getenv("DATABASE_URL")
# app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:oHtTmFO0HRJ5l3EKfuRn@containers-us-west-133.railway.app:5870/railway"
# # "postgresql://postgres:oHtTmFO0HRJ5l3EKfuRn@containers-us-west-133.railway.app:5870/railway"

# # app.config["MONGO_URI"] = "mongodb://"+MONGOUSER+":"+MONGOPASSWORD+"@"+MONGOHOST+":"+MONGOPORT+"/"+MONGODBNAME

# # MONGO_URL = os.environ.get("MONGO_URL")
# # MONGO_HOST = os.environ.get("MONGOHOST") 
# # MONGO_PASSWORD = os.environ.get("MONGOPASSWORD")
# # MONGO_PORT = os.environ.get("MONGOPORT")
# # MONGO_USER = os.environ.get("MONGOUSER")

# MONGO_URI = "mongodb://mongo:v3QydupO7uOTmNDQbhex@containers-us-west-106.railway.app:6005/test"

# app.config["MONGO_URI"] = MONGO_URI
# mongo = PyMongo(app)

# appointments = mongo.db.SMG

# @app.route('/appointments')
# def get_appointments():
#     appointments = list(mongo.db.SMG.find())
#     return jsonify(appointments)

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
#     return "Hey"


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


# @app.route('/api/appointment', methods=['POST'])  
# def create_appointment():
#     data = request.get_json()
#     mongo.db.SMG.insert_one(data)
#     return jsonify({'message': 'Appointment created'})


# # @app.route('/appointments')
# # def get_appointments():

# #     appointments = list(mongo.db.appointments.find())
  
# #     return jsonify(appointments)
    
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
from flask_pymongo import PyMongo
import os
from flask_cors import CORS
import pyrebase
from flask_login import LoginManager

app = Flask(__name__)

# Enable CORS for your front-end application
CORS(app, origins=["https://smgtherapy.netlify.app"])

# SQLAlchemy configuration for PostgreSQL
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:oHtTmFO0HRJ5l3EKfuRn@containers-us-west-133.railway.app:5870/railway"
db = SQLAlchemy(app)


MONGO_URL = os.environ.get("MONGO_URL")
MONGO_HOST = os.environ.get("MONGOHOST") 
MONGO_PASSWORD = os.environ.get("MONGOPASSWORD")
MONGO_PORT = os.environ.get("MONGOPORT")
MONGO_USER = os.environ.get("MONGOUSER")
MONGO_COLLECTION = "test"

# PyMongo configuration for MongoDB
MONGO_URI = "mongodb://mongo:v3QydupO7uOTmNDQbhex@containers-us-west-106.railway.app:6005/test"
app.config["MONGO_URI"] = "mongodb://"+ MONGO_USER +":"+ MONGO_PASSWORD +"@"+ MONGO_HOST +":"+ MONGO_PORT +"/"+ MONGO_COLLECTION
app.config["MONGO_URI"] = MONGO_URI
mongo = PyMongo(app)

# Define the SQLAlchemy model
class Feedback(db.Model):
    __tablename__ = 'smg_customer'
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(200), unique=True)
    last_name = db.Column(db.String(200))
    email = db.Column(db.String(200))
    massage_type = db.Column(db.String(200))
    time = db.Column(db.String(20))
    date = db.Column(db.String(20))

    def __init__(self, first_name, last_name, email, massage_type, time, date):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.massage_type = massage_type
        self.time = time
        self.date = date

# Define a route to submit data to PostgreSQL
@app.route('/api/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        data = request.get_json()
        
        firstname = data.get('firstName')
        lastname = data.get('lastName')
        email = data.get('email')
        massagetype = data.get('massageType')
        time = data.get('time')
        date = data.get('date')

        # Create a new Feedback instance and insert it into PostgreSQL
        new_entry = Feedback(first_name=firstname, last_name=lastname, email=email, massage_type=massagetype, time=time, date=date)

        db.session.add(new_entry)
        db.session.commit()  

        return jsonify({"message": "Saved entry in PostgreSQL!"})

# Define a route to create appointments in MongoDB
@app.route('/api/appointment', methods=['POST'])  
def create_appointment():
    data = request.get_json()
    mongo.db.SMG.insert_one(data)
    return jsonify({'message': 'Appointment created in MongoDB'})

# Define a route to retrieve appointments from MongoDB
@app.route('/appointments')
def get_appointments():
    appointments = list(mongo.db.SMG.find())
    return jsonify(appointments)

# Define a route to retrieve clients from PostgreSQL
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
            "time": client.time,
            "date": client.date
        }
        
        client_list.append(client_info)
        
    return jsonify(client_list)

# Define a route for user login
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
