from sqlalchemy import *
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

db = create_engine('sqlite:///logins.db')
Session = sessionmaker()
Session.configure(bind=db)
db.session = Session()
db.echo = True # Can be set to False - Keep here to see generated SQL
Base = declarative_base()


class Login(Base):
    __tablename__ = 'logins'

    id = Column(Integer, primary_key=True)
    name = Column(String)

    def __repr__(self):
        return self.id


