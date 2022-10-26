from fastapi import FastAPI
from model import User, UserLogin, sign_in, login_user, arange, delete_todo, add_todo

app = FastAPI(debug=True)

@app.post('/user/v1/sign_in')
async def sign_in_(body:User):
    return sign_in(body)
   

@app.put('/user/v1/login/')
async def log_in (body:UserLogin):
    if body.username:
        return login_user(body.password, username=body.username)
    elif body.phone:
        return login_user(body.password, phone=body.phone)
    elif body.email:
        return login_user(body.password, email=body.email)
    else:
        print('please fill all the details')

@app.get('/user/v1/{username}')
async def data(username:str):
    return arange(username)

@app.delete('/user/v1/{username}/{id}')
async def delete(username:str, id:str):
    return delete_todo(username, id)

@app.post('/add_todo/user/v1/{username}')
async def add_todos(username:str, title:str, body:str):
    return add_todo(username, title, body)