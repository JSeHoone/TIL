from pydantic import BaseModel, validator
from fastapi import HTTPException

class NewUserForm(BaseModel):
    email: str
    name : str
    phone : str
    password : str


    @validator("email", "name", "phone", "password")
    def check_empty(cls,v):
        if not v or v.isspace():
            raise HTTPException(status_code=422, detail="필수 황목을 입력해주세요.")
        return v
    
    @validator("phone")
    def check_phone(cls,v):
        phone = v
        if "-" not in v or len(phone) != 13:
            raise HTTPException(status_code=422, detail="올바른 형식의 번호를 입력해주세요.")
        return phone

    @validator("password")
    def validate_password(cls, v):
        if len(v) < 8:
            raise HTTPException(status_code=422, detail="비밀번호는 8자 이상 영문과 숫자를 포함하여 작성해주세요.")
        if not any(char.isdigit() for char in v):
            raise HTTPException(status_code=422, detail="비밀번호는 8자 이상 영문과 숫자를 포함하여 작성해주세요.")
        if not any(char.isalpha() for char in v):
            raise HTTPException(status_code=422, detail="비밀번호는 8자 이상 영문과 숫자를 포함하여 작성해주세요.")
        
        return v
    

class Token(BaseModel):
    access_token:str
    token_type:str
