# Actividad SQLite y ORM
### Asignatura: Bases de Datos II
Autores:
- Diego Mateo Fernández (diego.mateofer@alumnos.upm.es) 
- Anton Pogromskyy Mozharskyi (anton.pogromskyy@alumnos.upm.es) 
- Alejandro Escorial Aparicio (alejandro.escorial@alumnos.upm.es) 

### Objetivos:
Aplicar conocimientos referidos a bases de datos SQLite y al sistema Object-Relationship-Model visto con SQLAlchemy para consultar e interactuar con la base de datos de ejemplo de MySQL “Sakila”, que simula un videoclub de alquiler de películas.

### Qué hay que hacer:
Elaborar uno o varios scripts para resolver 8 ejercicios mediante el módulo ORM de SQLAlchemy. Las operaciones que ejecute el programa deben ser formateadas
para que se muestren de manera limpia y ordenada.

1. Muestra el nombre del cliente y el número de películas que ha alquilado (1p).
2. Muestra el título de las películas con más de 3 actores, junto con el número de actores,
ordenadas de mayor a menor (1p).
3. Encuentra los datos de las personas que alquilaron la película “RIVER OUTLAW”, así
como las fechas en las que la alquilaron y devolvieron. ¿Hay alguien que no la haya
devuelto aún? (1p).
4. Muestra los clientes que no han realizado ningún alquiler en los últimos 30 días, junto
con la fecha de su último alquiler (1p). Pista: importar from datetime import datetime,
timedelta para calcular los últimos 30 días.
5. Muestra las películas que nunca han sido alquiladas (1p).
6. Muestra cada categoría con el precio medio del alquiler de sus películas (1p).
7. Aumenta un 10% el precio de alquiler de todas las películas con una duración mayor que
la duración media y muestra su precio antes y después de la actualización (1p). Pista: los
precios se almacenan como DECIMAL, no como FLOAT. Para evitar errores de
redondeo, hay que importar from decimal import Decimal.
8. Inserta una nueva categoría llamada “Premium” y asígnale todas las películas cuyo precio
de alquiler sea mayor que la media (1p).
