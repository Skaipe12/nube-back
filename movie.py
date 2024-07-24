from fastapi import APIRouter
from fastapi import Path
from fastapi.responses import JSONResponse
import psycopg2
from database import get_connection
from pydantic import BaseModel

class Movie(BaseModel):
    id: int
    title: str
    overview: str
    year: int
    rating: float
    category: str


movie_router = APIRouter()

@movie_router.get('/movies', tags=['movies'], response_model=list[Movie], status_code=200)
def get_movies():
        db = get_connection()
        movies = []
        try:
            # Establece la conexión con la base de datos
            conn = psycopg2.connect(db)
            cur = conn.cursor()
            
            # Ejecuta la consulta
            cur.execute("SELECT * FROM peliculas;")
            
            # Obtiene todos los resultados
            rows = cur.fetchall()
            
            # Procesa los resultados y almacena en una lista de diccionarios
            movies = [{"id": row[0], "titulo": row[1], "overview": row[2], "year": row[3], "rating": row[4], "category": row[5]} for row in rows]
            
            # Cierra el cursor y la conexión
            cur.close()
            conn.close()
        except Exception as e:
            print(f"Error al obtener películas: {e}")
        
        return movies

@movie_router.get('/movies/{id}', tags=['movies'], response_model=Movie)
def get_movie(id: int = Path(ge=1, le=2000)) -> Movie:
    db = get_connection()
    try:
        # Establece la conexión con la base de datos
        conn = psycopg2.connect(db)
        cur = conn.cursor()
        
        # Ejecuta la consulta
        cur.execute(f"SELECT * FROM peliculas WHERE id = {id};")
        
        # Obtiene el resultado
        row = cur.fetchone()
        
        # Procesa el resultado y almacena en un diccionario
        movie = {"id": row[0], "titulo": row[1], "overview": row[2], "year": row[3], "rating": row[4], "category": row[5]}
        
        # Cierra el cursor y la conexión
        cur.close()
        conn.close()
        return movie
    except Exception as e:
        print(f"Error al obtener película: {e}")
    

@movie_router.post('/movies', tags=['movies'], status_code= 201, response_model=Movie)
def create_movie(movie: Movie) -> JSONResponse:
    database = get_connection()
    try:
        # Establece la conexión con la base de datos
        conn = psycopg2.connect(database)
        cur = conn.cursor()
        
        # Ejecuta la consulta
        cur.execute(f"INSERT INTO peliculas (titulo, overview, year, rating, category) VALUES ('{movie.title}', '{movie.overview}', {movie.year}, {movie.rating}, '{movie.category}');")
        # Guarda los cambios
        conn.commit()


    except Exception as e:
        print(f"Error al crear película: {e}")
