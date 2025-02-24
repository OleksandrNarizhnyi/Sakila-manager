import dotenv
import os
from pymysql.cursors import DictCursor

path_to_env = os.path.join(os.getcwd(), '.env')
dotenv.load_dotenv(dotenv_path=path_to_env)

dbconfig = {
             'host': os.getenv('HOST'),
             'user': os.getenv('USER'),
             'password': os.getenv('PASSWORD'),
             'database': os.getenv('DATABASE'),
             'charset': os.getenv('CHARSET'),
             'cursorclass': DictCursor
         }
