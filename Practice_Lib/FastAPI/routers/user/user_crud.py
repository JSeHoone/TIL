from passlib.context import CryptContext
from sqlalchemy.orm import Session

from models import User
from routers.user.user_schema import NewUserForm

pwd_context = CryptContext(schemes=["bcrypt"], deprecated = "auto")

def get_user(email:str, db: Session):
    return db.query(User).filter(User.email == email).first()



def create_user(new_user: NewUserForm, db: Session):
    user = User(
        user_name = new_user.name,
        email = new_user.email,
        hashed_pw = pwd_context.hash(new_user.password),
    )

    db.add(user)
    db.commit()


def verify_password(plain_password, hashed_password):
    '''
    Password Decryption
    '''
    return pwd_context.verify(plain_password, hashed_password)
    