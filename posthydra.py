from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
import psycopg2
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import exists, select

Base = declarative_base()

class Good(Base):
    __tablename__ = 'goods'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    category = Column(String)
    shop = Column(String)
    description = Column(String)

    def __repr__(self):
        return f'{self.id} {self.name} {self.category} {self.shop} {self.description}'

class Offer(Base):
    __tablename__ = 'offers'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    location = Column(String)
    quantity = Column(Integer)
    price = Column(Integer)
    
    def __repr__(self):
        return f'{self.id} {self.name} {self.location} {self.quantity} {self.price}'


def add_elem(name, category, shop, desc):
    engine = create_engine('postgres+psycopg2://postgres:1234@82.146.44.166:5432/postgres')
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    new_good = Good(name=name, category=category, shop=shop, description=desc)
   
    session.add(new_good)

    session.commit()

    for good in session.query(Good):
        print(good)
