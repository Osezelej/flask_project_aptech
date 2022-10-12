import requests
from flask import Flask, render_template, flash, url_for, redirect
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, EmailField
from wtforms.validators import DataRequired, Email


app = Flask(__name__)

# csrf secret key
WTF_CSRF_SECRET_KEY = 'a very secret key that nobody should know'
# flask secret key
app.config['SECRET_KEY'] = 'a very secret key that nobody should know'

class SignIn(FlaskForm):
    username = StringField("Username", validators=[DataRequired(message='Enter your username')])
    email = EmailField('Email', validators= [DataRequired(message='Enter your email')])
    phone = StringField('Phone Number', validators=[DataRequired(message='Enter your phone number')])
    password = PasswordField('Password', validators=[DataRequired(message='Enter password')])
    submit = SubmitField('Submit')

class LoginForm(FlaskForm):
    username = StringField(label='Username/Email/Phone, ', validators=[DataRequired()])
    password = PasswordField(label='Password', validators=[DataRequired()])
    submit = SubmitField('Submit')

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    print(form.data)
    return render_template('login.html', form=form)
 

@app.route('/signin', methods=['GET', 'POST'])
def sign_in():
    form = SignIn()
    sign_in_data = {}
    error = None
    check = 0
    info = ['username', 'email', 'password', 'phone']
    if form.validate_on_submit():
        check += 1
        for i in info:
            sign_in_data[i] = form.data[i]
        response = requests.post('http://127.0.0.1:8000/user/v1/sign_in', json=sign_in_data)
        error = response.json()
        if error != 'sucessfull':
            return render_template('sign_in.html', form=form, error = error)
        else:
            return redirect(url_for('login', methods='GET'))
  
    return  render_template('sign_in.html', form=form, error = error)

if __name__ == '__main__':
    app.run(debug=True)

