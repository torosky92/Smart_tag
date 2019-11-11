import os
import datetime as dt

APP_NAME = os.getenv('APP_NAME', 'st-core')

COUNTRY = os.getenv('COUNTRY')
VERSION = '0.0.0'

BASE_PATH = os.getenv('BASE_PATH', '/api/st-core')

DEBUG = os.getenv('DEBUG', False)
DEPLOYED_AT = dt.datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
