from sqlalchemy.orm import Session
from database import get_db
from fastapi.security import OAuth2PasswordRequestForm
from fastapi import Depends

from fastapi import APIRouter, Response, Request, HTTPException
from routers.user.user_schema import NewUserForm, Token
import routers.user.user_crud as user_crud

from datetime import timedelta

# Access Token 
import os
from dotenv import load_dotenv
from routers.user.utils import create_access_token
load_dotenv()
SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM")
ACCESS_TOKEN_EXPIRE_MINUTES = float(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES"))

app = APIRouter(
    prefix="/user"
)

@app.post(path="/signup")
async def signup(new_user: NewUserForm, db: Session = Depends(get_db)):
    # check user
    user = user_crud.get_user(new_user.email, db)

    if user:
        raise HTTPException(status_code=409, detail="User already exists")
    
    # signup user
    user_crud.create_user(new_user=new_user, db = db)
    
    return HTTPException(status_code=200, detail="Signup seccessful ! ")


@app.post("/login")
async def login(response:Response, login_form: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    
    # Check User
    user = user_crud.get_user(login_form.username, db=db)

    if not user:
        raise HTTPException(status_code=400, detail="Invalid user or password")
    
    # login
    res = user_crud.verify_password(login_form.password, user.hashed_pw)

    # create access token
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(data = {"sub": user.user_name}, expires_delta = access_token_expires)

    # Save cookie
    response.set_cookie(key = "access_token", value = access_token, expires = access_token_expires, httponly = True)

    if not res:
        raise HTTPException(status_code=400, detail="Invalid user or password")
    
    return Token(access_token=access_token, token_type="bearer")


@app.get(path = "/logout")
async def logout(response: Response, request: Request):
    access_token = request.cookies.get("access_token")

    # remove cookie
    response.delete_cookie(key = "access_token")

    return HTTPException(status_code=200, detail = "Logout successful.")