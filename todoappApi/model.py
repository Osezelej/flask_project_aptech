from typing import Optional
from unicodedata import name
from pydantic import BaseModel, EmailStr
import psycopg2
from settings import read_from

CONFIGURATION = read_from('db.ini', 'postgres')

class User(BaseModel):
    '''sign in data validation'''
    username: str
    email: EmailStr
    phone: str
    password: str


class UserLogin(BaseModel):
    '''login data validation'''
    username: Optional[str] 
    email: Optional[str] 
    phone: Optional[str]
    password: str

class ApiLogin(BaseModel):
    user_id:str
    password:str

is_sign_in = False # to check if the it is sign in of login function that is to activated


def request_fromdb(column, column_value, password):
    '''accepts the column activated, the column_value and the password \n
     returns the table name'''

    with psycopg2.connect(**CONFIGURATION) as conn: # Open connection with psycopg2
        with conn.cursor() as cur: # Open cursor that holds the sql commands

            auth_script = f'''SELECT * FROM user_login_info
                                WHERE {column} =%s AND password =%s''' # this is the sql commands

            cur.execute(auth_script, (column_value, password)) #this is use to store the sql commands in the cursor
            tablename = None
            try:
                tablename = cur.fetchall()[0][1] # assign the username| table name to the variable tablename
            except IndexError:
                print('connection error ') # print this error message if there is an error
            conn.commit() # this is what execute the functions in the database
        return tablename

def get_data(table:str) -> list:
    '''accepts tablename|username parameter and returns the todos for the users table'''

    with psycopg2.connect(**CONFIGURATION) as conn:
        with conn.cursor() as cur:
            data_script = f'''SELECT * FROM {table}'''
            cur.execute(data_script)
            data = cur.fetchall()
        conn.commit()
    return data

def arange(table:list) -> None:
    '''this accept the tables and arranges it'''
    data = []
    table_column =['id', 'title', 'body', 'schedule']
    for row in get_data(table):
        d = {}
        for w in range(len(table_column)):
            d[table_column[w]] = row[w]
        data.append(d)
    return data
def sign_in(user:User) -> str:
    '''accepts the validated User data'''

    p = len(user.password)
    if p < 8:
        return 'PWDerror'
    if len(user.username) < 5:
        return 'U2error'
    if not user.username.isalnum():
        return 'U1error'
    if len(user.phone) < 10 : # extra validation
        return 'Perror'
    if not  user.phone.isnumeric:
        return 'P1error'
    if user.username[0].isnumeric():
        return 'U3error'

    with psycopg2.connect(**CONFIGURATION) as conn:
        with conn.cursor() as cur:
            auth_script = '''SELECT username FROM user_login_info ORDER BY username'''
            cur.execute(auth_script)
            auth = cur.fetchall()
            check = True
            for names in auth:
                if names[0] == user.username:
                    return 'Uerror'
            if check:
                insert_script = '''INSERT INTO user_login_info(username, email, phone, password)values(%s, %s, %s, %s)''' 
                cur.execute(insert_script, (user.username, user.email, user.phone, user.password))
                

                create_script = f'''CREATE TABLE {user.username}
                            (id BIGSERIAL,
                            header TEXT,
                            body TEXT,
                            schedule TIMESTAMP)'''
                cur.execute(create_script)
        conn.commit()


    return 'sucessfull'


def login_user(password:str, username:str='', phone:str='', email:str='')->None:
    if username: 
        column = 'username'
        table_name = request_fromdb(column=column, column_value=username,password=password)
        if table_name:
           return arange(table_name)
        else:
            print('please there is an error')

    elif phone:
        column = 'phone'
        table_name = request_fromdb(column, phone,password)
        if table_name:
            return arange(table_name)
        else:
            print('there is an error')
    elif email:
        column = 'email'
        table_name = request_fromdb(column, email,password)
        if table_name:
            return arange(table_name)
        else:
            print('there is an error')


def update():
    pass

# username = input('please enter your username: ')
# email = input('please enter your email: ')
# phone = input('please enter your phone number: ')
# password = input('please enter your password: ')

# if is_sign_in:
#     person = User(username=username, email=email, phone=phone, password=password)
#     sign_in(person)
# else:
#     person = UserLogin(username=username, email=email, phone=phone, password=password)


