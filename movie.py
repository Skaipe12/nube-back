from fastapi import APIRouter, Path
from fastapi.responses import JSONResponse
from database import get_connection
from pydantic import BaseModel

class Movie(BaseModel):
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
        conn = db.cursor()
        conn.execute("SELECT * FROM peliculas;")
        rows = conn.fetchall()
        movies = [{"id": row[0], "title": row[1], "overview": row[2], "year": row[3], "rating": row[4], "category": row[5]} for row in rows]
        conn.close()
    except Exception as e:
        print(f"Error al obtener películas: {e}")
    
    return movies

@movie_router.get('/movies/{id}', tags=['movies'], response_model=Movie)
def get_movie(id: int = Path(ge=1, le=2000)) -> Movie:
    db = get_connection()
    try:
        conn = db.cursor()
        conn.execute(f"SELECT * FROM peliculas WHERE id = {id};")
        row = conn.fetchone()
        movie = {"id": row[0], "title": row[1], "overview": row[2], "year": row[3], "rating": row[4], "category": row[5]}
        conn.close()
        return movie
    except Exception as e:
        print(f"Error al obtener película: {e}")
    
@movie_router.post('/movies', tags=['movies'], status_code=201)
def create_movie(movie: Movie) -> JSONResponse:
    db = get_connection()
    try:
        conn = db.cursor()
        conn.execute(f"INSERT INTO peliculas (title, overview, year, rating, category) VALUES ('{movie.title}', '{movie.overview}', {movie.year}, {movie.rating}, '{movie.category}');")
        db.commit()
        conn.close()
    except Exception as e:
        print(f"Error al crear película: {e}")
