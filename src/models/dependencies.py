from sqlalchemy.orm import Session

from src.settings import database


def get_db() -> Session:
    db = database.get_session()
    try:
        yield db
    finally:
        db.close()
