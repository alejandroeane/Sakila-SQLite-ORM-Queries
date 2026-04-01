from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Numeric
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()

class Category(Base):
    __tablename__ = "category"
    category_id = Column(Integer, primary_key=True)
    name = Column(String(25))

class Customer(Base):
    __tablename__ = "customer"
    customer_id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    rentals = relationship("Rental", back_populates="customer")

class Film(Base):
    __tablename__ = "film"
    film_id = Column(Integer, primary_key=True)
    title = Column(String)
    rental_rate = Column(Numeric(4,2))
    length = Column(Integer)

class FilmActor(Base):
    __tablename__ = "film_actor"
    actor_id = Column(Integer, primary_key=True)
    film_id = Column(Integer, ForeignKey('film.film_id'), primary_key=True)

class FilmCategory(Base):
    __tablename__ = "film_category"
    film_id = Column(Integer, ForeignKey('film.film_id'), primary_key=True)
    category_id = Column(Integer, ForeignKey('category.category_id'), primary_key=True)

class Inventory(Base):
    __tablename__ = "inventory"
    inventory_id = Column(Integer, primary_key=True)
    film_id = Column(Integer, ForeignKey('film.film_id'))

class Rental(Base):
    __tablename__ = "rental"
    rental_id = Column(Integer, primary_key=True)
    rental_date = Column(DateTime)
    inventory_id = Column(Integer, ForeignKey('inventory.inventory_id'))
    customer_id = Column(Integer, ForeignKey('customer.customer_id'))
    return_date = Column(DateTime, nullable=True)
    customer = relationship("Customer", back_populates="rentals")
