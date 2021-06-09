import os

from dotenv import load_dotenv
from pathlib import Path

load_dotenv()

# app
APP_HOST = os.getenv('APP_HOST')
APP_PORT = int(os.getenv('APP_PORT'))
BASE_DIR = Path(__file__).resolve().parent

#database
DATABASE_NAME = os.getenv('DATABASE_NAME')
DATABASE_USER = os.getenv('DATABASE_USER')
DATABASE_PASSWORD = os.getenv('DATABASE_PASSWORD')
DATABASE_HOST = os.getenv('DATABASE_HOST')
DATABASE_PORT =int(os.getenv('DATABASE_PORT'))