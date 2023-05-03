from sqlalchemy import Column
from sqlalchemy.sql.sqltypes import Integer, String

from src.models import Base


class User(Base):
    __tablename__ = "user"
    id = Column("id", Integer, primary_key=True)
    name = Column("name", String(255))
    email = Column("email", String(255))
    password = Column("password", String(255))
