from fastapi import APIRouter

import datetime
from typing import List, Optional

from fastapi import Path, Query
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field

from config.database import Sesion, engine
from models.movie import Movie as MovieModel
from services.movie import MovieService
from schema.movie import Movie

movie_router = APIRouter()


# segundo endpoint

@movie_router.get('/movies', tags=["movies"],
                  response_model=List[Movie],
                  )  # dependencies=[Depends(JWTBearer())]
def get_movies():
    # creamos la sesion
    db = Sesion()

    result = MovieService(db).get_all()
    # consultamos las peliculas
    # mov = db.query(MovieModel).all()
    json_data = jsonable_encoder(result)
    # return JSONResponse(content=mov, status_code=200)
    return JSONResponse(content=json_data, status_code=200)


@movie_router.get('/movies/{movie_id}', tags=["movies"], response_model=Movie)
def get_movie(movie_id: int = Path(ge=1, le=2222)):
    # creamos la sesion
    db = Sesion(bind=engine)
    # consultamos las peliculas
    # mov = db.query(MovieModel).filter(MovieModel.id == movie_id).first()
    mov = MovieService(db).get_movie(movie_id)
    # validamos si existe la pelicula
    if not mov:
        return JSONResponse(content={'message': 'Movie not found'},
                            status_code=404)
    json_data = jsonable_encoder(mov)
    return JSONResponse(content=json_data, status_code=200)


@movie_router.get('/movies/', tags=["movies"])
def get_movies_by_category(category: str = Query(max_length=10, min_length=5),
                           ):  # year: int = Query(le=datetime.date.today().year)

    # creamos la sesion
    db = Sesion()
    # consultamos las peliculas
    # mov = db.query(MovieModel).filter(MovieModel.category ==
    #                                   category, MovieModel.year == year).all()
    mov = MovieService(db).get_movie_by_category(category)
    if not mov:
        return JSONResponse(content={'message': 'Movie not found'},
                            status_code=404)
    json_data = jsonable_encoder(mov)

    return JSONResponse(content=json_data, status_code=200)


@movie_router.post('/movies', tags=["movies"], response_model=list)
def create_movie(movie: Movie) -> JSONResponse:

    # creamos la sesion
    db = Sesion()
    MovieService(db).create_movie(movie)
    # se crea el objeto con los datos del modelo
    # new_movie = MovieModel(**movie.dict())

    # # se agrega el objeto a la sesion
    # db.add(new_movie)

    # # se confirma la transaccion
    # db.commit()
    # movies.append(movie)

    return JSONResponse(content={'message': 'Movie created'}, status_code=201)


@movie_router.put('/movies/{movie_id}', tags=["movies"])
def update_movie(movie_id: int, newMovie: Movie):
    # se crea la session
    db = Sesion()
    result = MovieService(db).get_movie(movie_id)
    # se consulta la pelicula
    # mov = db.query(MovieModel).filter(MovieModel.id == movie_id).first()
    # verificamos si existe la pelicula
    if not result:
        return JSONResponse(content={'message': 'Movie not found'},
                            status_code=404)
    # se actualiza la pelicula
    # mov.title = newMovie.title  # type: ignore
    # mov.overview = newMovie.overview
    # mov.year = newMovie.year
    # mov.rating = newMovie.rating
    # mov.category = newMovie.category
    # # se confirma la transaccion
    # db.commit()
    # # se usa refresh para actualizar los datos
    # db.refresh(mov)
    MovieService(db).update_movie(movie_id, newMovie)

    return JSONResponse(content={'message': 'Movie updated'},
                        status_code=200)


@movie_router.delete('/movies/{movie_id}', tags=["movies"])
def delete_movie(movie_id: int):
    # se crea la session
    db = Sesion(bind=engine)
    # se consulta la pelicula
    mov = MovieService(db).get_movie(movie_id)
    # verificamos si existe la pelicula
    if not mov:
        return JSONResponse(content={'message': 'Movie not found'},
                            status_code=404)
    # se elimina la pelicula
    # db.delete(mov)
    # # se confirma la transaccion
    # db.commit()
    # se usa refresh para actualizar los datos
    # db.refresh(mov)

    MovieService(db).delete_movie(movie_id)
    return JSONResponse(content={'message': 'Movie deleted'})
