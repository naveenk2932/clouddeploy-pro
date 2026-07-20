import os
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()


class Config:
    # Application Configuration
    APP_NAME = os.getenv("APP_NAME", "CloudDeploy Pro")
    APP_ENV = os.getenv("APP_ENV", "development")
    APP_VERSION = os.getenv("APP_VERSION", "1.0.0")

    # Flask Configuration
    SECRET_KEY = os.getenv("SECRET_KEY", "change-this-secret-key")

    # PostgreSQL Configuration
    POSTGRES_DB = os.getenv("POSTGRES_DB", "clouddeploy")
    POSTGRES_USER = os.getenv("POSTGRES_USER", "clouddeploy")
    POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD", "clouddeploy")
    POSTGRES_HOST = os.getenv("POSTGRES_HOST", "postgres")
    POSTGRES_PORT = os.getenv("POSTGRES_PORT", "5432")

    # Database URI (for SQLAlchemy - we'll use this in the next step)
    SQLALCHEMY_DATABASE_URI = (
        f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}"
        f"@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}"
    )

    SQLALCHEMY_TRACK_MODIFICATIONS = False