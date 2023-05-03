import os

from alembic.command import upgrade
from alembic.config import Config
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from src.controllers import user
from src.settings import database, get_settings

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.on_event("startup")
def startup():
    database.init_db()
    upgrade(Config(os.path.join(get_settings().BASE_DIR, "alembic.ini")), "head")


app.include_router(user.route)
