from flask import Flask, request, render_template, redirect,url_for
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField,PasswordField
from wtforms.validators import DataRequired,Email,ValidationError
import bcrypt
from flask_mysqldb import MySQL

app = Flask(__name__)

#MYSQL COnfiguaration
app.config['MYSQL_HOST'] ='localhost'
app.config['MYSQL_USER'] ='root'
app.config['MYSQL_PASSWORD'] ='1234'
app.config['MYSQL_DB'] ='loginproject'
app.secret_key = 'your_secret_key_here'

mysql = MySQL(app)

class RegisterForm (FlaskForm):
    name= StringField("Name", validators =[DataRequired()])
    email= StringField("Email", validators =[Email(), DataRequired()])
    password= PasswordField("Password", validators =[ DataRequired()], )
    submit= SubmitField("Submit")

@app.route('/')
def index():
    return "hi"

@app.route('/register', methods=['GET','POST'])
def register():
    if request.method == 'POST':
        pass
    form = RegisterForm()
    if form.validate_on_submit():
        name = form.name.data
        email = form.email.data
        password = form.password.data
        hashed_password = bcrypt.hashpw(password.encode('utf-8'),bcrypt.gensalt())

        cursor = mysql.connection.cursor()
        cursor.execute("INSERT INTO users (name,email,password) VALUES (%s,%s,%s)",(name,email,password))
        mysql.connect.commit()
        cursor.close()

        return redirect(url_for('login'))

    return render_template('register.html', form =form)
        
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