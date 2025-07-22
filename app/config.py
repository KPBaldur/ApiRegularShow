from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    app_name: str = "Regular Show API"
    admin_email: str = "kevin.pizarrosanz@gmail.com"

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

settings = Settings()