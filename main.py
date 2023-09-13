from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__, static_folder="./dist")

# Set the SQLAlchemy configuration using the DATABASE_URL environment variable
database_url = os.getenv("DATABASE_URL")
app.config['SQLALCHEMY_DATABASE_URI'] = database_url
# "postgresql://postgres:oHtTmFO0HRJ5l3EKfuRn@containers-us-west-133.railway.app:5870/railway"

# Create the SQLAlchemy database object
db = SQLAlchemy(app)

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



@app.route('/') 
def index():
    return app.send_static_file('./index.html')

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

        # Create a new Feedback instance using the correct column names
        new_entry = Feedback(first_name=firstname, last_name=lastname, email=email, massage_type=massagetype, time=time, date=date)

        db.session.add(new_entry)
        db.session.commit()

        return jsonify({"message": "Saved entry!"})

    # Get other fields

if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))

