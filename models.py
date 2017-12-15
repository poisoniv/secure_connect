from sqlalchemy import *
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

db = create_engine('sqlite:///connections.db')
Session = sessionmaker()
Session.configure(bind=db)
db.session = Session()
db.echo = True # Can be set to False - Keep here to see generated SQL
Base = declarative_base()


class connections(Base):
    __tablename__ = 'connections'

    id = Column(Integer, primary_key=True)
    username = Column(String)
    activity = Column(Integer)

    def __repr__(self):
        return self.id


