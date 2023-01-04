from fastapi import FastAPI, Body
from fastapi.responses import HTMLResponse

#### modificamos parametros de la documentacion.
app=FastAPI()
app.title='my first app with fastApi'
app.version='0.0.1'
####
movies = [{
    'id':1,
    'tittle':'Avatar',
    'overview':'en la cosa esa habia un gato mutante',
    'year':2009,
    'rating':7.8,
    'category':'Accion'
},
    {
    'id':2,
    'tittle':'Titanic',
    'overview':'Se hundio el barco ese',
    'year':2000,
    'rating':9.0,
    'category':'Drama'
}]
@app.get('/',tags=['home'])
def message():
    return HTMLResponse('<h1>hello world</h1>')
@app.get('/movies', tags=['movies'])
def getMovies():
    return movies
### parametros query ####  
@app.get('/movies/{id}')
def getMovie(id: int):
    movie=list(filter(lambda movId:movId['id']==id,movies))
    return movie if len(movie)>0 else 'no existe el id '
@app.get('/movies/',tags=[movies])
def getMovieByCategory(category:str, year:int):
    movie=list(filter(lambda mov: mov['category']==category.capitalize(),movies))
    return movie if len(movie)>0 else ' '
    
### post ####
@app.post('/movies',tags=['movies'])
def createMovies(id:int=Body(), tittle:str=Body(), overview:str=Body(), year:int=Body(), rating:int=Body(), category:str=Body()):
    movies.append({
            'id':id,
            'tittle':tittle,
            'overview':overview,
            'year':year,
            'rating':rating,
            'category':category
    })
    return movies