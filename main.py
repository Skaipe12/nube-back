from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from movie import movie_router
from fastapi.middleware.cors import CORSMiddleware

# Esta es la configuración de documentación de Swagger
app = FastAPI()
app.title = "Swagger documentation FastAPI"
app.version = "0.0.0"

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Esta es la ruta principal de la aplicación
@app.get('/',tags=['Home'])
def message():
    return HTMLResponse('<h1>Hello World<h1>')

app.include_router(movie_router)




