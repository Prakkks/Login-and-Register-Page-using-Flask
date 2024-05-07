from flask import Flask, request, render_template, redirect,url_for
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField,PasswordField
from wtforms.validators import DataRequired,Email,ValidationError
from flask_sqlalchemy import SQLAlchemy
# import bcrypt
import secrets
from sqlalchemy import Column, String, Integer , MetaData, Table, create_engine


# engine = db.create_engine('mysql://root:1234@localhost:3306/loginproject',echo=True)
secret_key = secrets.token_hex(16)

app = Flask(__name__)

app.config['SECRET_KEY'] = secret_key
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:1234@localhost:3306/loginproject'

db = SQLAlchemy(app)


@app.route('/')
def index(): 
    return "hi"

@app.route('/register', methods=['GET','POST'])
def register():
    metadata= MetaData()
    metadata.reflect(bind=db.engine)
    for table in metadata.tables.values():
        print(f"Table: {table.name}")
        for column in table.c:
            print(f"Column: {column.name}, Type: {column.type}")
        print()
    if request.method == 'POST'  :
        username= request.form['Name']
        email = request.form['Email']
        pass
        

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