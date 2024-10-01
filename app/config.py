from pydantic_settings import BaseSettings
from sqlalchemy.engine.url import URL


class Settings(BaseSettings):
    DB_HOST:str
    DB_PORT:int
    DB_USER:str
    DB_PASS:str
    DB_NAME:str
    
    SECRET_KEY:str
    ALGORITHM:str

# для отправки писем
    SMTP_HOST:str
    SMTP_PORT:int
    SMTP_USER:str
    SMTP_PASS:str

    REDIS_HOST:str
    REDIS_PORT:int


    class Config:
        env_file='.env'


settings = Settings()

