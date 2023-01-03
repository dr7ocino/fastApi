from fastapi import FastAPI
app=FastAPI()
app.title='my first app with fastApi'
app.version='0.0.1'
@app.get('/',tags=['home'])
def message():
    return 'return hola mundo'