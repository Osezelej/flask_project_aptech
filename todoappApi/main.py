from fastapi import FastAPI
from model import User, UserLogin, sign_in, login_user

app = FastAPI(debug=True)

@app.post('/user/v1/sign_in')
async def sign_in_(body:User):
    return sign_in(body)
   

@app.put('/user/v1/login/')
async def log_in (body:UserLogin):
    if body.username:
        return await login_user(body.password, username=body.username)
    elif body.phone:
        return login_user(body.password, phone=body.phone)
    elif body.email:
        return login_user(body.password, email=body.email)
    else:
        print('please fill all the details')




