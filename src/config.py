""" Configuration settings for the application """

import os
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL", "data/movies.json")
SECRET_KEY = os.getenv("SECRET_KEY")
DEBUG = os.getenv("DEBUG", "False").lower() in ('true', '1', 't')
TEMPLATE_PATH = os.getenv("TEMPLATE_PATH", "templates")
