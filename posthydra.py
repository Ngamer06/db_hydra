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
    quantity = Column(String)
    price = Column(String)
    
    def __repr__(self):
        return f'{self.id} {self.name} {self.location} {self.quantity} {self.price}'

class Shop(Base):
    __tablename__ = 'shops'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(String)

    def __repr__(self):
        return f'{self.id} {self.name} {self.description}'

class Review(Base):
    __tablename__ = 'reviews'
    id = Column(Integer, primary_key=True)
    shop_name = Column(String)
    author = Column(String)
    text = Column(String)
    name_good = Column(String)
    location = Column(String)

    def __repr__(self):
        return f'{self.id} {self.shop_name} {self.author} {self.text} {self.name_good} {self.location}'

def del_all_tables():
    engine = create_engine('postgres+psycopg2://postgres:1234@82.146.44.166:5432/postgres')
    Base.metadata.drop_all(engine)

def add_elem(name, category, shop, desc):
    engine = create_engine('postgres+psycopg2://postgres:1234@82.146.44.166:5432/postgres')
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    new_good = Good(name=name, category=category, shop=shop, description=desc)

    all_elem = []
    goods_session = session.query(Good.name).all()

    for good in goods_session:
        all_elem.append(good.name)
    
    if str(name) in all_elem:
        print(f'Repeat {name}')
    else:
        print(f'Add elem {name} {category} {shop} {desc}')
        session.add(new_good)
        
    session.commit()

    for good in session.query(Good):
        print(good)
   
def add_offer(name, location, quantity, price):
    engine = create_engine('postgres+psycopg2://postgres:1234@82.146.44.166:5432/postgres')
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
        
    new_offer = Offer(name=name, location=location, quantity=quantity, price=price)
    
    all_offers = []
    offers_session = session.query(Offer.name).all()

    for offer in offers_session:
        all_offers.append(offer.name)
    
    if str(name) in all_offers:
        print(f'Repeat {name}')
    else:
        print(f'Add elem {name} {location} {quantity} {price}')
        session.add(new_offer)
        
    session.commit()

    for offer in session.query(Offer):
        print(offer)

def add_shop(name, desc):
    engine = create_engine('postgres+psycopg2://postgres:1234@82.146.44.166:5432/postgres')
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
        
    new_shop = Shop(name=name, description=desc)
    
    all_shop = []
    shops_session = session.query(Shop.name).all()

    for shop in shops_session:
        all_shop.append(shop.name)
    
    if str(name) in all_shop:
        print(f'Repeat {name}')
    else:
        print(f'Add elem {name} {desc}')
        session.add(new_shop)
        
    session.commit()

    for shop in session.query(Shop):
        print(shop)

def add_review(shop_name, author, text, name_good, location):
    engine = create_engine('postgres+psycopg2://postgres:1234@82.146.44.166:5432/postgres')
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
        
    new_review = Review(shop_name=shop_name, author=author, text=text, name_good=name_good, location=location)
    
    all_review = []
    reviews_session = session.query(Review.text).all()

    for review in reviews_session:
        all_review.append(review.text)
    
    if str(name) in all_review:
        print(f'Repeat {name}')
    else:
        print(f'Add elem {shop_name} {author} {text} {name_good} {location}')
        session.add(new_review)
    
    session.commit()

    for review in session.query(Review):
        print(review)
