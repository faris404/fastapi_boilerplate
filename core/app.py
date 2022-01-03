from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from tortoise.contrib.fastapi import register_tortoise
from core.config import settings, loggerSettings
from core.routers import routers
import logging


def init_app(app:FastAPI):
   app.mount(
      settings.STATIC_URL, 
      StaticFiles(directory=settings.STATIC_DIR),
      name="static",
   )
   register_db(app)
   register_routers(app)
   register_exceptions(app)
   register_middlewares(app)
   register_logger()

def register_db(app: FastAPI):
   register_tortoise(
      app,
      db_url=settings.DATABASE_URL,
      modules={"models": ['models']},
      generate_schemas=True,
      add_exception_handlers=True,
   )

def register_exceptions(app: FastAPI):
   # app.add_exception_handler(ExceptionClass,handler)
   pass

def register_routers(app: FastAPI):
   for router in routers:
      kwargs = dict()
      if router.get('tags'):
         kwargs['tags'] = router['tags']
      if router.get('prefix'):
         kwargs['prefix'] = router['prefix']
      app.include_router(router['router'],**kwargs)

def register_middlewares(app: FastAPI):
    app.add_middleware(
        CORSMiddleware,
        allow_origins=settings.CORS_ORIGINS,
        allow_credentials=settings.CORS_ALLOW_CREDENTIALS,
        allow_methods=settings.CORS_ALLOW_METHODS,
        allow_headers=settings.CORS_ALLOW_HEADERS,
    )

def register_logger():
   logging.config.dictConfig(loggerSettings)