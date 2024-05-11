from flask import Flask, request, render_template, redirect,url_for,jsonify
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField,PasswordField
from wtforms.validators import DataRequired,Email,ValidationError
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import bcrypt
from sqlalchemy import Column, String, Integer , MetaData, Table, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker , session


# engine = db.create_engine('mysql://root:1234@localhost:3306/loginproject',echo=True)



app = Flask(__name__)
# bcrypt = Bcrypt(app)
# app.config['SECRET_KEY'] = secret_key
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:1234@localhost:3306/loginproject'

db = SQLAlchemy(app)

class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String)
    email = db.Column(db.String)
    passwords=db.Column(db.String)
    salt =db.Column(db.String, nullable=False)

@app.route('/')
def add_data():
    return render_template('dashhboard.html')



@app.route('/register', methods=['GET','POST'])
def register():
    if request.method == 'POST':
        
        Name= request.form['Name']
        Emails= request.form['Email']
        hpassword=request.form['Password']
        salt = bcrypt.gensalt()
        hashpassword= bcrypt.hashpw(hpassword.encode('utf-8'),salt)
        new_entry = Users(username=Name,email=Emails,passwords=hashpassword,salt=salt)
        all_users = Users.query.filter_by(email=Emails).first()
        if all_users:
            print(all_users)
            return render_template('register.html',  Email = 'already exist')
        else:   
            db.session.add(new_entry)
            db.session.commit()
            db.session.close()
            return render_template('register.html', Name= Name, Email = Emails)
        

    return render_template('register.html')
        
@app.route('/login', methods=['GET','POST'])
def login(): 
    if request.method == 'POST':
        Emails = request.form['Email'] 
        passwords = request.form['password']
        password=passwords.encode('utf-8')
        user = Users.query.filter_by(email=Emails).first()  
        if user:
            if bcrypt.checkpw(password,user.passwords.encode('utf-8')):
                return render_template('adminLogin.html', message='Login successful')
            else:
                return render_template('adminLogin.html', message='Incorrect Password')

        else:
            return render_template('adminLogin.html', message='User not found')
    return render_template('adminLogin.html')

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

if __name__ == '__main__':
    app.run(debug =True)