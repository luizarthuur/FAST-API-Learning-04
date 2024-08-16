from typing import List
from pydantic import BaseSettings, AnyHttpUrl 
from sqlalchemy.ext.declarative import declarative_base

class Settings(BaseSettings):

    #Configs gerais utilizadas na aplicação

    API_V1_STR: str = '/api/v1'
    DB_URL: str = 'postgresql+asyncpg://postgres:vistatech3011@localhost:5432/vista-tech-bd'
    DBBaseModel = declarative_base()

    class Config:
        case_sensitive = True

settings = Settings()

