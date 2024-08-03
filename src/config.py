import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()


class Config:
    # Resolve the full path for DATABASE_URL
    DATABASE_URL = os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..", os.getenv("DATABASE_URL"))
    )
    SECRET_KEY = os.getenv("SECRET_KEY")
    DEBUG = os.getenv("DEBUG", "False").lower() in ["true", "1", "t"]
    TEMPLATE_PATH = os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..", "templates")
    )
