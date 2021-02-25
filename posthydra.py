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
    # style = relationship('Offer', backref = 'goods', lazy=True, cascade="all, delete-orphan")

    def __repr__(self):
        return f'{self.id} {self.name} {self.category} {self.shop} {self.description}'

class Offer(Base):
    __tablename__ = 'offers'
    id = Column(Integer, primary_key=True)
    # name_good = Column(String) #, ForeignKey('goods.name')
    name = Column(String) #relationship('Good')
    location = Column(String)
    quantity = Column(Integer)
    price = Column(Integer)
    
    def __repr__(self):
        return f'{self.id} {self.name} {self.location} {self.quantity} {self.price}'


def main():
    engine = create_engine('postgres+psycopg2://postgres:1234@82.146.44.166:5432/postgres')

    Base.metadata.create_all(engine)
    
    Session = sessionmaker(bind=engine)
    
    session = Session()


    # good1 = Good(name=name, category=category, shop=shop, description=description)

    new_good = Good(name='1', category='2', shop='3', description='4')
    # new_offer = Offer(name='glil', location='egs', quantity='2', price='14552')

    session.add(new_good)
    # session.add(new_offer)

    session.commit()

    for good in session.query(Good):
        print(good)

    # for offer in session.query(Offer):
    #     print(offer)
   
    # exists(select([("schema_name")]).select_from("information_schema.schemata").
    #     where("schema_name == 'foo'"))

if __name__ == "__main__":
    main()