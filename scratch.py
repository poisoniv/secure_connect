from functions import *
from meraki import meraki
from users import users
from config import config
import json
import ipaddress
import datetime
from models import db, connections
import time
from sqlalchemy import *
from sqlalchemy.orm import sessionmaker, Query
from sqlalchemy.ext.declarative import declarative_base



username = 'tom'
status = connections()
test = status.query.filter(status.username.ilike(username))



print(test)