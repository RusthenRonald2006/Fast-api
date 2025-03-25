from fastapi import FastApi


app= FastApi()


@app.get('/')
def get_languages():
    return {"Sucess":"foi"}