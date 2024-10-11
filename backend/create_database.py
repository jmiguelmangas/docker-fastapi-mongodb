from database import get_database

db = get_database()

movies_collection = db["movies"]

movies = [
    {
        "title": "Avatar",
        "year": 2001,
        "description": "Located in the near future, a group of soldiers get into a far away planet with some blue guys with strange appeareance",
        "score": 7
    },
    {
        "title": "Robocop",
        "year": 1987,
        "description": "A police man died in act of service and they save his life to become a half robot/human to fight against the bad guys",
        "score": 5
    },
]

movies_collection.insert_many(movies)