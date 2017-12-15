from models import *

try:
    f = open('connections.db')
    f.close()
    print("connections.db already exists.")
except:
    Base.metadata.create_all(db)
    print("connections.db successfully created.")