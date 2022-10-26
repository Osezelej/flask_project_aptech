from ast import Delete
from turtle import title
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

class TodoData:
    def __init__(self, data=''):
        self.data = data
        
is_log_in = False

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/dashboard/<username>', methods=['POST'])
def dashboard(username: str):
    global is_log_in
    todos = TodoData()
    form = TodoForm()
    response = requests.get(f'http://127.0.0.1:8000/user/v1/{username}')
    todos.data = response.json()
    
    if not is_log_in:
        flash(f"{username}, you've logged in sucessfully")
        is_log_in = True
    else:
        print('deleted')
        num = request.form.get('todo_id')
        
        print(num)
        if num:
            requests.delete(f'http://127.0.0.1:8000/user/v1/{username}/{num}')
            response = requests.get(f'http://127.0.0.1:8000/user/v1/{username}')
            todos.data = response.json()
            return redirect(url_for('delete'), code=307)
        add_todo = request.form.get('addtodo')
        if add_todo:
            todos.data = []
            print() 
            data = form.data
            data_dict = {
                'title':data['title'],
                'body':data['body']
            }
            response = requests.post(f'http://127.0.0.1:8000/add_todo/user/v1/{username}',params = data_dict)
            response = requests.get(f'http://127.0.0.1:8000/user/v1/{username}')
            todos.data = response.json()

    return render_template('dashboard.html', form=form, data=todos.data)

@app.route('/login', methods=['GET', 'POST'])
def login():
    global is_log_in
    is_log_in = False
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

@app.post('/delete')
def delete():
    title = request.form.get('todo_title')
    return render_template('delete.html', title = title)
if __name__ == '__main__':
    app.run(debug=True)

