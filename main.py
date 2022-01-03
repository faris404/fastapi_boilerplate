from fastapi import FastAPI
from core.config import settings
from core.app import init_app


app = FastAPI(
   title = settings.TITLE,
   description = settings.DESCRIPTION,
   version = settings.VERSION,
   debug = settings.DEBUG,
)

init_app(app)





