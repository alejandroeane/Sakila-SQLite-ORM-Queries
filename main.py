from sqlalchemy import create_engine, func, desc
from sqlalchemy.orm import declarative_base, sessionmaker
from datetime import datetime, timedelta
from models import *

engine = create_engine('sqlite:///sakila.db', echo=False) 

Session = sessionmaker(bind=engine)
session = Session()


def ejercicio_1():
    res = session.query(
        Customer.first_name,
        Customer.last_name,
        func.count(Rental.rental_id).label("num_alquileres")
        ).join(Rental).group_by(Customer.customer_id).all()
    
    print(f"\n{'NOMBRE DEL CLIENTE':<30} | {'Nº ALQUILERES'}")
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

    print(f"\n{'TÍTULO':<30} | {'Nº ACTORES'}")
    print("-" * 50)

    for title, count in res:
        print(f"{title:<30} | {count}")


def ejercicio_3(film_title: str):
    res = session.query(
        Customer.first_name,
        Customer.last_name,
        Rental.rental_date,
        Rental.return_date
    ).join(Rental, Rental.customer_id == Customer.customer_id) \
    .join(Inventory, Inventory.inventory_id == Rental.inventory_id) \
    .join(Film, Film.film_id == Inventory.film_id) \
    .filter(Film.title == film_title.upper()).all()

    if not res:
        print(f"No se han encontrado alquileres para la película '{film_title}'.")
        return

    print(f"\n{'CLIENTE':<30} | {'FECHA ALQUILER':<30} | {'FECHA DEVOLUCIÓN'}")
    print("-" * 90)

    people_not_returned: list[str] = []

    for name, surname, rental_date, return_date in res:
        client = f"{name} {surname}"
        if return_date is None:
            return_date = "NO DEVUELTO"
            people_not_returned.append(client)
            
        print(f"{client:<30} | {str(rental_date):<30} | {return_date}")

    print("-" * 90)
    print(f"¿Hay alguien que no haya devuelto {film_title} aún?")
    if people_not_returned:
        print(f"-> Sí. Los siguientes clientes aún tienen la película: {', '.join(people_not_returned)}")
    else:
        print("-> No, todos los clientes han devuelto esta película.")


def ejercicio_4(dias: int):
    fecha_limite = datetime.now() - timedelta(days=dias)
    
    res = session.query(
        Customer.first_name,
        Customer.last_name,
        func.max(Rental.rental_date).label("ultimo_alquiler")
        ).outerjoin(Rental) \
        .group_by(Customer.customer_id) \
        .having(func.max(Rental.rental_date) < fecha_limite) \
        .order_by(desc(func.max(Rental.rental_date))).all()
    
    print(f"\n{'CLIENTE':<30} | {'ÚLTIMO ALQUILER'}")
    print("-" * 50)
    
    for name, surname, last_date in res:
        nombre_completo = f"{name} {surname}"
        print(f"{nombre_completo:<30} | {last_date}")


def ejercicio_5():
    res = session.query(
        Film.title
        ).outerjoin(Inventory) \
        .outerjoin(Rental) \
        .group_by(Film.film_id) \
        .having(func.count(Rental.rental_id) == 0).all()
    
    print(f"\n{'PELÍCULAS NUNCA ALQUILADAS'}")
    print("-" * 30)
    if not res:
        print("Todas las películas han sido alquiladas alguna vez.")
        return
    
    for title, in res:
        print(f"{title}")


def ejercicio_6():
    res = session.query(
        Category.name.label("categoria"),
        func.round(func.avg(Film.rental_rate), 2).label("precio_medio")
        ).join(FilmCategory, FilmCategory.category_id == Category.category_id) \
        .join(Film, Film.film_id == FilmCategory.film_id) \
        .group_by(Category.category_id, Category.name) \
        .order_by(func.avg(Film.rental_rate).desc()).all()

    print(f"\n{'CATEGORÍA':<30} | {'PRECIO MEDIO'}")
    print("-" * 50)

    for cat, precio in res:
        print(f"{cat:<30} | ${float(precio):.2f}")


def ejercicio_7():
    pass


def ejercicio_8():
    pass


if __name__ == '__main__':
    while True:
        print("\n" + "="*40)
        print("Menú de Operaciones")
        print("="*40)
        print("1. Mostrar clientes y su número de alquileres")
        print("2. Mostrar películas con más de 3 actores")
        print("3. Buscar alquileres por título de película")
        print("4. Mostrar clientes sin alquiler desde hace X días")
        print("5. Mostrar películas nunca alquiadas")
        print("6. Mostrar precio medio por categoría de película")
        print("7. ")
        print("8. ")
        print("0. Salir")
        print("="*40)
        
        option = input("Elige una opción (0-8): ")
        
        if option == '1':
            ejercicio_1()
        elif option == '2':
            ejercicio_2()
        elif option == '3':
            film = input("Introduce el título de la película (pulse enter para usar RIVER OUTLAW por defecto): ")
            if not film:
                film = "RIVER OUTLAW"
            ejercicio_3(film)
        elif option == '4':
            try:
                dias_input = input("Introduce los días sin alquiler (pulse enter para usar 30 por defecto): ")
                dias = int(dias_input) if dias_input.strip() else 30
            except ValueError:
                dias = 30
            ejercicio_4(dias)
        elif option == '5':
            ejercicio_5()
        elif option == '6':
            ejercicio_6()
        elif option == '0':
            print("Cerrando sesión...")
            break
        else:
            print("Opción no válida.")

    session.close()