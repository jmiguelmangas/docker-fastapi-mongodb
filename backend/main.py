from fastapi import FastAPI,HTTPException
from models import Movie
from database import get_database

app = FastAPI(version=1.0,title="Proyecto Peliculas")
app.description = "API realizada con FastAPI CRUD basico con lista de peliculas"

db = get_database()

movies_collection = db["movies"]

@app.get("/", tags=["Home"])
def home():
    return {"Message": "Bienvenido al Proyecto de Peliculas"}

@app.get("/movies/", tags=["Movies"])
def show_all_movies():
    movies = list(movies_collection.find())
    for movie in movies:
        movie["_id"] = str(movie["_id"])
    return movies

@app.get("/movie/{movie_title}", tags=["Movies"], status_code=200)
def show_movie(movie_title:str):
    movie_list = []
    movies = list(movies_collection.find())
    found = False
    for movie in movies:
        if movie["title"] == movie_title:
            movie_list.append(movie)
            found = True
            break
    if not found:
        raise HTTPException(status_code=404,detail="Movie Not Found")
    else:
        for movie in movie_list:
            movie["_id"] = str(movie["_id"])
        return movie_list[0]

@app.post("/movie/",tags=["Movies"],status_code=201)
def add_new_movie(movie:Movie):
    movie_found = movies_collection.find_one({"title":movie.title})
    if movie_found is None:
        movies_collection.insert_one(movie.dict())
    else:
        raise HTTPException(status_code=400,detail="Movie already in the database")

@app.put("/movie/{title}",tags=["Movies"],status_code=200, 
description="Update a Movie")
def update_movie(title:str,movie_updated:Movie):
    movie_found = movies_collection.find_one({"title":movie.title})
    if movie_found:
        result = movies_collection.update_one(
            {"title":title},
            {"$set":update_movie.dict()}
        )
        if result.modified_count == 1:
            return {"message": "movie updated"}
        else:
            raise HTTPException(status_code=400,detail="No changes made")
    else:        
        raise HTTPException(status_code=404,detail="Not Found")

@app.delete("/movie/{title}",tags=["Movies"],status_code=200, 
description="Delete a Movie")
def delete_movie(title:str):
    movie_found = movies_collection.find_one({"title":title})
    if movie_found:
        result = movies_collection.delete_one(
            {"title":title}
        )
        if result.deleted_count == 1:
            return {"message": "movie deleted"}
        else:
            raise HTTPException(status_code=400,detail="No changes made")
    else:        
        raise HTTPException(status_code=404,detail="Movie Not Found")

    