from email.quoprimime import body_check
import requests
from flask import Flask, render_template, flash, url_for, redirect, request
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, EmailField, TextAreaField
from wtforms.validators import DataRequired, Email, length

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
    username = StringField(label='Username', validators=[DataRequired()])
    password = PasswordField(label='Password', validators=[DataRequired()])
    submit = SubmitField('Submit')
class TodoForm(FlaskForm):
    title = StringField(validators=[DataRequired(), length(min=4)])
    body = TextAreaField(validators=[DataRequired(), length(min=4)])
    submit = SubmitField('Submit')


@app.route('/')
def home():
    return render_template('home.html')

@app.route('/dashboard/<username>', methods=['POST'])
def dashboard(username: str):
    form = TodoForm()
    response = requests.get(f'http://127.0.0.1:8000/user/v1/{username}')
    data = response.json()
    flash(f"{username}, you've logged in sucessfully")
    return render_template('dashboard.html', form=form, data=data)

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    form = LoginForm()
    user_entry = {}
#    login_list = ["username", "phone", "Email", "password"]
    if request.method == 'POST':
        data = form.data
        if data['username']:
            if (data['username'].isalnum() or data['username'].isalpha()) and not data['username'][0].isnumeric():
                print(data['username'])
                user_entry['username'] = data['username']
                user_entry['password'] = data['password']
                response = requests.put('http://127.0.0.1:8000/user/v1/login/', json=user_entry)
                api_error = response.json()
                if api_error == 'Uerror':
                    error = 'Enter the correct username or Password '
                else:
                    return redirect(url_for('dashboard', username = data['username'] ), code=307)
                
            else:
                error = 'Enter a valid username'
        else:
            error = 'Enter a valid username'
            return render_template('login.html', form=form)

    return render_template('login.html', form=form, error=error)
 

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

