from models import *

try:
    f = open('logins.db')
    f.close()
    print("logins.db already exists.")
except:
    Base.metadata.create_all(db)
    print("logins.db successfully created.")