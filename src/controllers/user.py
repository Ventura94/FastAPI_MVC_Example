from fastapi import APIRouter, Depends
from fernet import Fernet
from sqlalchemy.orm import Session

from src.models import User as UserModel
from src.models.dependencies import get_db
from src.views.users import User as UserView

route = APIRouter()


@route.get("/users", response_model=list[UserView], response_model_exclude={"password"})
def get_users(session: Session = Depends(get_db)):
    return session.query(UserModel).all()


@route.post("/users", response_model=UserView, response_model_exclude={"password"})
def create_user(user: UserView, session: Session = Depends(get_db)):
    key = Fernet.generate_key()
    f = Fernet(key)
    new_user = UserModel(
        name=user.name,
        email=user.email,
        password=f.encrypt(user.password.encode("utf-8")),
    )
    session.add(new_user)
    session.commit()
    session.refresh(new_user)
    return new_user
