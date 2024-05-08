from flask import Flask, request, render_template, redirect,url_for
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField,PasswordField
from wtforms.validators import DataRequired,Email,ValidationError
from flask_sqlalchemy import SQLAlchemy
# import bcrypt
import secrets
from sqlalchemy import Column, String, Integer , MetaData, Table, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker , session


# engine = db.create_engine('mysql://root:1234@localhost:3306/loginproject',echo=True)
secret_key = secrets.token_hex(16)



app = Flask(__name__)

app.config['SECRET_KEY'] = secret_key
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:1234@localhost:3306/loginproject'

db = SQLAlchemy(app)

class Lient(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String)
    email = db.Column(db.String)

@app.route('/')
def add_data():
    # Create an instance of the Lient class with the data you want to add
    # new_entry = Lient(name='John', email='john@example.com')

    # # Add the instance to the database session and commit
    # db.session.add(new_entry)
    # new_entry = Lient(name='Prakriti', email='prak@gmail.com')
    # db.session.add(new_entry)
    # db.session.commit()

    return 'Data added successfully'



@app.route('/register', methods=['GET','POST'])
def register():  
    Name=''
    Emails=''  
    if request.method == 'POST':
        
        Name= request.form['Name']
        Emails= request.form['Email']
        new_entry = Lient(name=Name,email=Emails)
        db.session.add(new_entry)
        db.session.commit()
        return render_template('register.html', Name= Name, Email = Emails )
        

    return render_template('register.html')
        
@app.route('/login', methods= ['GET', 'POST'])
def login():
    if request.method == 'POST':
        pass
    return render_template('adminLogin.html')

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

if __name__ == '__main__':
    app.run(debug =True)