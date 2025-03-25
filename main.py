from fastapi import FastAPI


app= FastAPI()


@app.get('/')
def get_languages():
    return {"Sucess":"foi"}





#uvicorn será responsavel por inicializar o servidor