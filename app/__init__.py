import logging
from flask import Flask

from app_config import *
from peewee import MySQLDatabase

logging.basicConfig(format="%(asctime)s:%(levelname)s:%(name)s:%(message)s")
logging.getLogger().setLevel(logging.DEBUG)

app = Flask(__name__)

db = MySQLDatabase(DATABASE_NAME,
                   user=DATABASE_USER,
                   password=DATABASE_PASSWORD,
                   host=DATABASE_HOST,
                   port=DATABASE_PORT
                   )


from . api import note
from . api import auth