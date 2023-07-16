from models.movie import Movie as MovieModel
from schema.movie import Movie


class MovieService:
    def __init__(self, db) -> None:
        self.db = db

    def get_all(self):

        result = self.db.query(MovieModel).all()
        return result

    def get_movie(self, movie_id: int):
        mov = self.db.query(MovieModel).filter(
            MovieModel.id == movie_id).first()
        return mov

    def get_movie_by_category(self, category: str):
        mov = self.db.query(MovieModel).filter(
            MovieModel.category == category).all()
        return mov

    def create_movie(self, movie: Movie):
        new_movie = MovieModel(**movie.dict())
        self.db.add(new_movie)
        self.db.commit()
        self.db.refresh(new_movie)

    def update_movie(self, id: int, data: Movie):
        mov = self.db.query(MovieModel).filter(MovieModel.id == id).first()
        mov.title = data.title
        mov.overview = data.overview
        mov.year = data.year
        mov.rating = data.rating
        mov.category = data.category
        self.db.commit()
        return mov

    def delete_movie(self, id: int):
        mov = self.db.query(MovieModel).filter(MovieModel.id == id).first()
        self.db.delete(mov)
        self.db.commit()
        return mov
