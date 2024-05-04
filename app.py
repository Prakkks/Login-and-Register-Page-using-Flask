
from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return "hi"

@app.route('/register', methods=['GET','POST'])
def register():
    if request.method == 'POST':
        pass
    return render_template('register.html')
        
@app.route('/login', methods= ['GET', 'POST'])
def login():
    if request.method == 'POST':
        pass
    return render_template('adminLogin.html')

if __name__ == '__main__':
    app.run(debug =True)