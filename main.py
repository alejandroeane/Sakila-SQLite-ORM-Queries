from sqlalchemy import create_engine,func, desc
from sqlalchemy.orm import declarative_base, sessionmaker
from models import *

engine = create_engine('sqlite:///sakila.db', echo=False) 
Base = declarative_base()

Session = sessionmaker(bind=engine)
session = Session()


def ejercicio_1():
    res = session.query(
        Customer.first_name,
        Customer.last_name,
        func.count(Rental.rental_id).label("num_alquileres")
        ).join(Rental).group_by(Customer.customer_id).all()
    
    print(f"{'NOMBRE DEL CLIENTE':<30} | {'Nº ALQUILERES'}")
    print("-" * 50)

    for name, surname, count in res:
        nombre_completo = f"{name} {surname}"
        print(f"{nombre_completo:<30} | {count}")


def ejercicio_2():
    res = session.query(
        Film.title,
        func.count(FilmActor.actor_id).label("num_actores")
    ).join(FilmActor) \
    .group_by(Film.film_id) \
    .having(func.count(FilmActor.actor_id) > 3) \
    .order_by(desc("num_actores")).all()

    print(f"{'TÍTULO':<30} | {'Nº ACTORES'}")
    print("-" * 50)

    for title, count in res:
        print(f"{title:<30} | {count}")


if __name__ == '__main__':
    # Create a switch case to select the exercise to run
    ejercicio_2()