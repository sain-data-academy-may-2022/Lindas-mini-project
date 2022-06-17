from textwrap import indent
import pymysql
import os
from dotenv import load_dotenv
from pyrsistent import s

# Load environment variables from .env file

load_dotenv()
host = os.environ.get("mysql_host")
user = os.environ.get("mysql_user")
password = os.environ.get("mysql_pass")
database = os.environ.get("mysql_db")


# Establish a database connection

def open_connection():
    connection = pymysql.connect(
        host,
        user,
        password,
        database
    )
    return connection
