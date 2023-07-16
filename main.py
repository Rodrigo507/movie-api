# %%
# path = para validar parametros en la url
# Field: para validar parametros en el body


from fastapi import FastAPI
from fastapi.responses import HTMLResponse

from config.database import Base, engine
from middlewares.error_headler import ErrorHandler
from routers.movie import movie_router
from routers.user import user_router
# from models.user import User as UserModel


app = FastAPI()
app.title = "Mi primer API con FastAPI"
app.version = "1.0.0"
app.description = "Esta es una descripción de mi API"

app.add_middleware(ErrorHandler)
app.include_router(movie_router)
app.include_router(user_router)

Base.metadata.create_all(bind=engine)

# primer endpoint


@app.get("/", tags=["home"])
def message():

    return HTMLResponse(content="<h1>Hola mundo</p>",
                        status_code=200)


# con la flag --reload, se reinicia el servidor cada vez
# que se guarda un cambio
# uvicorn main:app --reload

# con la flag --port, se puede cambiar el puerto
# uvicorn main:app --reload --port 5000

# con la flag --host, se puede cambiar el host
# uvicorn main:app --reload --host 0.0.0.0
# en otro dispositivo de la misma red, se puede acceder
# utilizando la ip del host
