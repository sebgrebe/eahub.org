import os

from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, Text, Unicode
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column('uid', Integer, primary_key=True)
    name = Column(Unicode)
    mail = Column(Unicode)

class Group(Base):
    __tablename__ = 'migrate_map_ea_group_migration'
    id = Column('destid1', Integer, primary_key=True)
    name = Column('sourceid1', Unicode)

engine = create_engine(
    'mysql+mysqldb://eahub@eahub:{password}@eahub.mysql.database.azure.com/eahub?charset=utf8'.format(
        password=os.environ['DATABASE_PASSWORD']
    )    
)

Base.metadata.bind = engine

