import os
from dotenv import load_dotenv

# Load environment file
load_dotenv(".env.prod")

DATABASE_URL = os.getenv("DATABASE_URL")
SECRET_KEY = os.getenv("SECRET_KEY")
DEBUG = os.getenv("DEBUG", "False") == "True"

